# ============================================================
# BOARD EXAM QUESTIONNAIRE - MAIN APPLICATION
# ============================================================

import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

# ============================================================
# COLOR PALETTE & STYLES (DARK THEME)
# ============================================================
BG_DARK = "#0F1115"
PANEL_MAIN = "#1C212B"
PANEL_SEC = "#242A35"
INPUT_BTN = "#2A303B"
BORDER_COLOR = "#3A414D"
PRIMARY_COLOR = "#C62828"
PRIMARY_HOVER = "#E53935"
SUCCESS_COLOR = "#2E7D32"
SUCCESS_HOVER = "#388E3C"
ERROR_COLOR = "#C62828"
WARNING_COLOR = "#F9A825"
TEXT_WHITE = "#FFFFFF"
TEXT_MUTED = "#A7AFBC"

# ============================================================
# QUESTION DATABASE (30 PRACTICE QUESTIONS ACROSS SUBJECTS)
# ============================================================
RAW_QUESTIONS = [
    {
        "id": 1,
        "subject": "Structural Engineering",
        "topic": "Foundations",
        "difficulty": "Easy",
        "question": "What is the primary structural purpose of a footing in a building?",
        "choices": [
            "Transfer structural loads to the soil and distribute bearing pressure",
            "Increase the overall height and architectural aesthetic of the building",
            "Prevent water ingress through the roof structure",
            "Provide temporary shoring during floor construction"
        ],
        "answer": 0,
        "explanation": "A footing is a foundation element that transfers structural loads from columns or walls directly to the supporting soil, ensuring the load does not exceed the allowable soil bearing capacity."
    },
    {
        "id": 2,
        "subject": "Structural Engineering",
        "topic": "Loads",
        "difficulty": "Easy",
        "question": "Which of the following describes a 'Dead Load' on a structure?",
        "choices": [
            "Occupants, moveable furniture, and temporary equipment",
            "Permanent gravity loads from structural members and fixed materials",
            "Lateral forces induced by wind gusts or earthquakes",
            "Dynamic loads caused by machinery vibration"
        ],
        "answer": 1,
        "explanation": "Dead loads consist of the weight of all materials of construction incorporated into the building, including walls, floors, roofs, ceilings, stairways, and fixed service equipment."
    },
    {
        "id": 3,
        "subject": "Structural Engineering",
        "topic": "Reinforced Concrete",
        "difficulty": "Medium",
        "question": "Why is steel rebar embedded on the tension side of reinforced concrete beams?",
        "choices": [
            "Concrete is weak in tension, while steel provides high tensile strength",
            "Steel increases the compressive capacity of concrete threefold",
            "Steel prevents alkali-silica reaction in concrete aggregates",
            "Steel reduces the overall dead weight of the concrete beam"
        ],
        "answer": 0,
        "explanation": "Concrete exhibits strong compressive strength but relatively low tensile strength. Steel reinforcement is positioned in tension zones to resist tensile forces and control cracking."
    },
    {
        "id": 4,
        "subject": "Structural Engineering",
        "topic": "Mechanics",
        "difficulty": "Medium",
        "question": "What is defined as the internal force per unit area within a structural material?",
        "choices": [
            "Strain",
            "Stress",
            "Moment of Inertia",
            "Modulus of Rupture"
        ],
        "answer": 1,
        "explanation": "Stress is the internal resistance offered by a unit area of a body from which a member is made to an externally applied load (Force / Area)."
    },
    {
        "id": 5,
        "subject": "Structural Engineering",
        "topic": "Flexure",
        "difficulty": "Hard",
        "question": "In a simply supported beam carrying a uniform load, where does the maximum bending moment occur?",
        "choices": [
            "At both end supports",
            "At the quarter points",
            "At the mid-span",
            "At the point of contraflexure"
        ],
        "answer": 2,
        "explanation": "For a simply supported beam with a uniform load (w), shear is zero at mid-span and the bending moment reaches its maximum value of (w * L^2) / 8 at mid-span."
    },
    {
        "id": 6,
        "subject": "Geotechnical Engineering",
        "topic": "Soil Mechanics",
        "difficulty": "Medium",
        "question": "What parameter measures the maximum load per unit area that soil can support without shear failure?",
        "choices": [
            "Ultimate Bearing Capacity",
            "Specific Gravity",
            "Permeability Coefficient",
            "Optimum Moisture Content"
        ],
        "answer": 0,
        "explanation": "Ultimate bearing capacity is the intensity of loading at which the soil beneath a foundation fails in shear."
    },
    {
        "id": 7,
        "subject": "Geotechnical Engineering",
        "topic": "Soil Properties",
        "difficulty": "Easy",
        "question": "Atterberg limits are used to determine the plastic consistency of which soil type?",
        "choices": [
            "Coarse Sand",
            "Gravel",
            "Fine-grained soils (Clays and Silts)",
            "Crushed Rock"
        ],
        "answer": 2,
        "explanation": "Atterberg limits (Liquid Limit, Plastic Limit, Plasticity Index) quantify the critical water contents of fine-grained silts and clays."
    },
    {
        "id": 8,
        "subject": "Mathematics",
        "topic": "Algebra",
        "difficulty": "Easy",
        "question": "What is the slope of the line given by the equation 3x + 4y = 12?",
        "choices": [
            "3/4",
            "-3/4",
            "4/3",
            "-4/3"
        ],
        "answer": 1,
        "explanation": "Converting 3x + 4y = 12 into slope-intercept form (y = mx + b) yields y = -3/4 x + 3. Thus, the slope m = -3/4."
    },
    {
        "id": 9,
        "subject": "Mathematics",
        "topic": "Trigonometry",
        "difficulty": "Easy",
        "question": "In a right triangle, which trigonometric ratio represents the opposite side over the hypotenuse?",
        "choices": [
            "Cosine",
            "Tangent",
            "Sine",
            "Secant"
        ],
        "answer": 2,
        "explanation": "Sine (sin) of an angle in a right triangle is defined as Opposite / Hypotenuse (SOH)."
    },
    {
        "id": 10,
        "subject": "Mathematics",
        "topic": "Calculus",
        "difficulty": "Medium",
        "question": "What is the derivative of f(x) = x^3 - 5x + 7 with respect to x?",
        "choices": [
            "3x^2 - 5",
            "3x^2 - 5x",
            "x^2 - 5",
            "3x^3 - 5"
        ],
        "answer": 0,
        "explanation": "Applying the power rule d/dx(x^n) = n*x^(n-1): d/dx(x^3) = 3x^2, d/dx(-5x) = -5, and d/dx(7) = 0. Result: 3x^2 - 5."
    },
    {
        "id": 11,
        "subject": "Construction",
        "topic": "Concrete Technology",
        "difficulty": "Easy",
        "question": "What test is performed on fresh concrete to measure its consistency and workability?",
        "choices": [
            "Slump Test",
            "Proctor Test",
            "Core Drill Test",
            "Charpy Impact Test"
        ],
        "answer": 0,
        "explanation": "The slump test measures the consistency and workability of fresh concrete prior to placement."
    },
    {
        "id": 12,
        "subject": "Construction",
        "topic": "Formwork & Curing",
        "difficulty": "Medium",
        "question": "What is the minimum standard moist curing period recommended for normal Portland cement concrete?",
        "choices": [
            "24 hours",
            "3 days",
            "7 days",
            "28 days"
        ],
        "answer": 2,
        "explanation": "A minimum of 7 days moist curing is standard for type I Portland cement concrete to develop adequate strength."
    },
    {
        "id": 13,
        "subject": "Surveying",
        "topic": "Leveling",
        "difficulty": "Easy",
        "question": "In differential leveling, what is the term for a sight taken on a point of known elevation?",
        "choices": [
            "Foresight (FS)",
            "Backsight (BS)",
            "Intermediate Sight (IS)",
            "Turning Point (TP)"
        ],
        "answer": 1,
        "explanation": "A Backsight (BS) is the first rod reading taken after setting up the instrument at a point of known or assumed elevation."
    },
    {
        "id": 14,
        "subject": "Surveying",
        "topic": "Bearings & Azimuths",
        "difficulty": "Medium",
        "question": "If a line has a magnetic bearing of S 45° E, what is its equivalent whole-circle azimuth from North?",
        "choices": [
            "45°",
            "135°",
            "225°",
            "315°"
        ],
        "answer": 1,
        "explanation": "In the SE quadrant, Azimuth = 180° - Bearing. Therefore, Azimuth = 180° - 45° = 135°."
    },
    {
        "id": 15,
        "subject": "Hydraulics",
        "topic": "Fluid Mechanics",
        "difficulty": "Medium",
        "question": "Which principle states that an increase in the speed of a fluid occurs simultaneously with a decrease in pressure?",
        "choices": [
            "Pascal's Law",
            "Archimedes' Principle",
            "Bernoulli's Principle",
            "Torricelli's Law"
        ],
        "answer": 2,
        "explanation": "Bernoulli's principle states an increase in fluid velocity occurs simultaneously with a drop in static pressure or potential energy."
    },
    {
        "id": 16,
        "subject": "Hydraulics",
        "topic": "Flow Measurement",
        "difficulty": "Hard",
        "question": "What device is commonly installed in a open channel to measure volumetric water flow rate?",
        "choices": [
            "Weir / Parshall Flume",
            "Manometer",
            "Piezometer",
            "Pitot Tube"
        ],
        "answer": 0,
        "explanation": "Weirs and flumes are calibrated open-channel structures used to compute volumetric flow based on head water depth."
    },
    {
        "id": 17,
        "subject": "Building Technology",
        "topic": "Building Envelope",
        "difficulty": "Easy",
        "question": "What is the primary function of a vapor barrier installed in roof or wall assemblies?",
        "choices": [
            "Prevent structural deflection under wind loads",
            "Block moisture vapor migration into insulation and structural frames",
            "Enhance sound transmission class (STC) ratings",
            "Improve fire resistance duration of wall assemblies"
        ],
        "answer": 1,
        "explanation": "Vapor retarders or barriers prevent moist air from diffusing into building envelopes where condensation could occur."
    },
    {
        "id": 18,
        "subject": "Building Laws and Standards",
        "topic": "Code Compliance",
        "difficulty": "Medium",
        "question": "What is the minimum clear width typically required for egress doors in commercial assemblies?",
        "choices": [
            "600 mm",
            "710 mm",
            "900 mm",
            "1200 mm"
        ],
        "answer": 2,
        "explanation": "Standard accessibility and building safety codes specify a minimum clear opening width of 900 mm (or 32/36 inches) for egress doors."
    },
    {
        "id": 19,
        "subject": "Professional Practice",
        "topic": "Ethics & Contracts",
        "difficulty": "Easy",
        "question": "In construction management, what document outlines the legally binding agreement between owner and contractor?",
        "choices": [
            "Owner-Contractor Agreement",
            "Bill of Quantities",
            "Shop Drawing Submittal",
            "Site Inspection Log"
        ],
        "answer": 0,
        "explanation": "The formal contract agreement executed by the owner and contractor sets the legally binding terms, scope, and price."
    },
    {
        "id": 20,
        "subject": "Professional Practice",
        "topic": "Project Scheduling",
        "difficulty": "Medium",
        "question": "What does CPM stand for in project scheduling and project management?",
        "choices": [
            "Critical Path Method",
            "Construction Project Management",
            "Cost Performance Matrix",
            "Contractual Progress Method"
        ],
        "answer": 0,
        "explanation": "Critical Path Method (CPM) is a step-by-step project management technique for process planning that defines critical and non-critical tasks."
    },
    {
        "id": 21,
        "subject": "Transportation",
        "topic": "Pavement Design",
        "difficulty": "Medium",
        "question": "Which layer in a flexible pavement structure directly supports the asphalt surface course?",
        "choices": [
            "Subgrade",
            "Subbase Course",
            "Base Course",
            "Bedding Sand"
        ],
        "answer": 2,
        "explanation": "The base course lies directly beneath the surface layer and provides load distribution over the subbase and subgrade."
    },
    {
        "id": 22,
        "subject": "Materials",
        "topic": "Steel Properties",
        "difficulty": "Easy",
        "question": "What is the approximate density of structural carbon steel?",
        "choices": [
            "1,000 kg/m³",
            "2,400 kg/m³",
            "7,850 kg/m³",
            "11,300 kg/m³"
        ],
        "answer": 2,
        "explanation": "The standard design density used for structural carbon steel is 7,850 kg/m³ (78.5 kN/m³)."
    },
    {
        "id": 23,
        "subject": "Environmental Engineering",
        "topic": "Wastewater",
        "difficulty": "Medium",
        "question": "What parameter indicates the amount of dissolved oxygen needed by aerobic biological organisms to break down organic material?",
        "choices": [
            "BOD (Biochemical Oxygen Demand)",
            "pH Level",
            "Turbidity Index",
            "Total Suspended Solids (TSS)"
        ],
        "answer": 0,
        "explanation": "BOD measures the amount of oxygen consumed by microorganisms while decomposing organic matter under aerobic conditions."
    },
    {
        "id": 24,
        "subject": "Architecture",
        "topic": "Architectural History",
        "difficulty": "Easy",
        "question": "Which Classical order of Greek architecture is characterized by scroll-like volutes on its capital?",
        "choices": [
            "Doric",
            "Ionic",
            "Corinthian",
            "Tuscan"
        ],
        "answer": 1,
        "explanation": "The Ionic order is distinguished by capital ornaments shaped like spiral scrolls (volutes)."
    },
    {
        "id": 25,
        "subject": "Building Utilities",
        "topic": "Electrical",
        "difficulty": "Easy",
        "question": "What electrical unit measures electric current flow?",
        "choices": [
            "Volt",
            "Ampere",
            "Ohm",
            "Watt"
        ],
        "answer": 1,
        "explanation": "Electric current is measured in Amperes (A), representing the flow rate of electric charge."
    },
    {
        "id": 26,
        "subject": "Building Utilities",
        "topic": "Plumbing",
        "difficulty": "Medium",
        "question": "What component in a plumbing fixture trap prevents sewer gases from entering living spaces?",
        "choices": [
            "Water Seal",
            "Check Valve",
            "Cleanout Plug",
            "Air Gap"
        ],
        "answer": 0,
        "explanation": "The water seal trapped inside a U/P-trap acts as a liquid barrier against sewer gas migration."
    },
    {
        "id": 27,
        "subject": "Architectural Design",
        "topic": "Design Principles",
        "difficulty": "Easy",
        "question": "In architectural design composition, what is 'Scale'?",
        "choices": [
            "The physical color balance of materials",
            "The proportional relationship of an element's size relative to a standard or human body",
            "The acoustic insulation rating of an interior space",
            "The structural capacity of load-bearing walls"
        ],
        "answer": 1,
        "explanation": "Scale refers to the size of a building element or space relative to a known unit of measure, often human scale."
    },
    {
        "id": 28,
        "subject": "History and Theory",
        "topic": "Modern Architecture",
        "difficulty": "Medium",
        "question": "Who famously coined the architectural doctrine 'Form follows function'?",
        "choices": [
            "Frank Lloyd Wright",
            "Louis Sullivan",
            "Le Corbusier",
            "Mies van der Rohe"
        ],
        "answer": 1,
        "explanation": "Louis Sullivan, known as the 'father of skyscrapers', coined the phrase 'Form follows function'."
    },
    {
        "id": 29,
        "subject": "Construction Methods",
        "topic": "Earthworks",
        "difficulty": "Easy",
        "question": "What piece of heavy equipment is primarily used for leveling, grading, and spreading soil or base materials?",
        "choices": [
            "Motor Grader",
            "Tower Crane",
            "Pile Driver",
            "Concrete Pump"
        ],
        "answer": 0,
        "explanation": "A motor grader features a long blade used to create flat surface grading during earthwork operations."
    },
    {
        "id": 30,
        "subject": "Engineering Science",
        "topic": "Thermodynamics",
        "difficulty": "Medium",
        "question": "Which law of thermodynamics states that energy cannot be created or destroyed, only transformed?",
        "choices": [
            "Zeroth Law",
            "First Law",
            "Second Law",
            "Third Law"
        ],
        "answer": 1,
        "explanation": "The First Law of Thermodynamics is the Law of Conservation of Energy, stating energy is conserved."
    }
]

# Extract unique subjects
ALL_SUBJECTS = sorted(list(set(q["subject"] for q in RAW_QUESTIONS)))

# ============================================================
# MAIN APPLICATION CLASS
# ============================================================
class BoardExamQuestionnaireApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BOARD EXAM QUESTIONNAIRE")
        self.root.geometry("1400x850")
        self.root.minsize(1100, 700)
        self.root.configure(bg=BG_DARK)

        # State Variables
        self.favorites = set()
        self.bookmarks = set()
        self.answers_history = {} # question_id -> {selected, is_correct}
        
        # Settings
        self.setting_subject = "ALL SUBJECTS"
        self.setting_difficulty = "All"
        self.setting_mode = "Review" # Review or Exam
        self.setting_timer_option = "Timer OFF" # OFF, 30m, 60m, 90m, 120m
        self.setting_randomize = True
        self.setting_question_limit = "All"

        # Quiz Run Variables
        self.active_questions = []
        self.current_index = 0
        self.user_answers = {} # q_index -> choice_index
        self.user_evaluated = {} # q_index -> True/False
        self.time_remaining_sec = 0
        self.timer_running = False

        # Configure Fonts
        self.font_title = ("Segoe UI", 16, "bold")
        self.font_subtitle = ("Segoe UI", 12, "bold")
        self.font_header = ("Segoe UI", 14, "bold")
        self.font_body = ("Segoe UI", 11)
        self.font_body_bold = ("Segoe UI", 11, "bold")
        self.font_small = ("Segoe UI", 9)
        self.font_qtext = ("Segoe UI", 13, "bold")

        self.setup_ui()

        # Keyboard Bindings
        self.root.bind("1", lambda e: self.key_select_choice(0))
        self.root.bind("2", lambda e: self.key_select_choice(1))
        self.root.bind("3", lambda e: self.key_select_choice(2))
        self.root.bind("4", lambda e: self.key_select_choice(3))
        self.root.bind("<Return>", lambda e: self.key_next_or_submit())
        self.root.bind("r", lambda e: self.reset_quiz_run())
        self.root.bind("R", lambda e: self.reset_quiz_run())
        self.root.bind("f", lambda e: self.toggle_favorite_current())
        self.root.bind("F", lambda e: self.toggle_favorite_current())
        self.root.bind("b", lambda e: self.toggle_bookmark_current())
        self.root.bind("B", lambda e: self.toggle_bookmark_current())

        # Start default view
        self.show_dashboard_view()

    # ============================================================
    # UI SETUP & LAYOUT
    # ============================================================
    def setup_ui(self):
        # Top Header Bar
        self.top_bar = tk.Frame(self.root, bg=PANEL_MAIN, height=50)
        self.top_bar.pack(side="top", fill="x")

        lbl_app_title = tk.Label(
            self.top_bar, text="BOARD EXAM QUESTIONNAIRE",
            font=self.font_title, fg=TEXT_WHITE, bg=PANEL_MAIN, padx=15
        )
        lbl_app_title.pack(side="left", fill="y")

        self.lbl_disclaimer = tk.Label(
            self.top_bar,
            text="Practice questionnaire for review purposes. Verify technical answers with official codes.",
            font=self.font_small, fg=WARNING_COLOR, bg=PANEL_MAIN, padx=10
        )
        self.lbl_disclaimer.pack(side="right", fill="y")

        # Container Frame below header
        self.container = tk.Frame(self.root, bg=BG_DARK)
        self.container.pack(side="bottom", fill="both", expand=True)

        # Left Sidebar Navigation
        self.sidebar = tk.Frame(self.container, bg=PANEL_MAIN, width=220)
        self.sidebar.pack(side="left", fill="y", padx=(0, 2))
        self.sidebar.pack_propagate(False)

        # Main Workspace Area
        self.main_container = tk.Frame(self.container, bg=BG_DARK)
        self.main_container.pack(side="right", fill="both", expand=True, padx=15, pady=15)

        self.build_sidebar_buttons()

    def build_sidebar_buttons(self):
        nav_items = [
            ("Dashboard", self.show_dashboard_view),
            ("Start Quiz / Review", self.start_quiz_session),
            ("Subjects", self.show_subjects_view),
            ("Favorites", self.show_favorites_view),
            ("Bookmarks", self.show_bookmarks_view),
            ("Review Wrong", self.show_wrong_answers_view),
            ("Search", self.show_search_view),
            ("Settings", self.show_settings_view)
        ]

        tk.Frame(self.sidebar, bg=PANEL_MAIN, height=10).pack()

        for label, cmd in nav_items:
            btn = tk.Button(
                self.sidebar, text=label, font=self.font_body_bold,
                fg=TEXT_WHITE, bg=PANEL_SEC, activebackground=PRIMARY_COLOR,
                activeforeground=TEXT_WHITE, bd=0, relief="flat",
                anchor="w", padx=15, pady=10, cursor="hand2", command=cmd
            )
            btn.pack(fill="x", pady=2, padx=5)

    def clear_main_container(self):
        self.stop_timer()
        for widget in self.main_container.winfo_children():
            widget.destroy()

    # ============================================================
    # VIEW 1: DASHBOARD
    # ============================================================
    def show_dashboard_view(self):
        self.clear_main_container()

        title = tk.Label(self.main_container, text="DASHBOARD & PERFORMANCE SUMMARY", font=self.font_header, fg=TEXT_WHITE, bg=BG_DARK)
        title.pack(anchor="w", pady=(0, 15))

        # Stat cards grid
        cards_frame = tk.Frame(self.main_container, bg=BG_DARK)
        cards_frame.pack(fill="x", pady=10)

        total_q = len(RAW_QUESTIONS)
        ans_q = len(self.answers_history)
        correct_q = sum(1 for v in self.answers_history.values() if v.get("is_correct"))
        incorrect_q = ans_q - correct_q
        avg_pct = (correct_q / ans_q * 100) if ans_q > 0 else 0.0

        stats = [
            ("QUESTIONS AVAILABLE", str(total_q), "#2196F3"),
            ("ANSWERED", str(ans_q), "#9C27B0"),
            ("CORRECT", str(correct_q), SUCCESS_COLOR),
            ("INCORRECT", str(incorrect_q), ERROR_COLOR),
            ("AVERAGE ACCURACY", f"{avg_pct:.1f}%", WARNING_COLOR),
            ("FAVORITES", str(len(self.favorites)), "#E91E63"),
            ("BOOKMARKS", str(len(self.bookmarks)), "#00BCD4")
        ]

        for i, (label, val, color) in enumerate(stats):
            card = tk.Frame(cards_frame, bg=PANEL_MAIN, highlightbackground=BORDER_COLOR, highlightthickness=1, padx=15, pady=15)
            card.grid(row=i//4, column=i%4, sticky="nsew", padx=5, pady=5)
            cards_frame.grid_columnconfigure(i%4, weight=1)

            tk.Label(card, text=label, font=self.font_small, fg=TEXT_MUTED, bg=PANEL_MAIN).pack(anchor="w")
            tk.Label(card, text=val, font=("Segoe UI", 20, "bold"), fg=color, bg=PANEL_MAIN).pack(anchor="w", pady=(5, 0))

        # Quick Action Banner
        action_panel = tk.Frame(self.main_container, bg=PANEL_MAIN, highlightbackground=BORDER_COLOR, highlightthickness=1, padx=20, pady=20)
        action_panel.pack(fill="x", pady=20)

        tk.Label(action_panel, text="Ready for Review?", font=self.font_header, fg=TEXT_WHITE, bg=PANEL_MAIN).pack(anchor="w")
        tk.Label(action_panel, text="Start a new custom practice session based on your current settings.", font=self.font_body, fg=TEXT_MUTED, bg=PANEL_MAIN).pack(anchor="w", pady=(0, 10))

        btn_start = tk.Button(
            action_panel, text="START PRACTICE QUIZ NOW", font=self.font_body_bold,
            fg=TEXT_WHITE, bg=PRIMARY_COLOR, activebackground=PRIMARY_HOVER,
            bd=0, padx=20, pady=10, cursor="hand2", command=self.start_quiz_session
        )
        btn_start.pack(anchor="w")

    # ============================================================
    # QUIZ ENGINE & NAVIGATION
    # ============================================================
    def prepare_quiz_questions(self):
        questions = [q.copy() for q in RAW_QUESTIONS]

        # Filter Subject
        if self.setting_subject != "ALL SUBJECTS":
            questions = [q for q in questions if q["subject"] == self.setting_subject]

        # Filter Difficulty
        if self.setting_difficulty != "All":
            questions = [q for q in questions if q["difficulty"] == self.setting_difficulty]

        if not questions:
            return []

        # Shuffle Questions if enabled
        if self.setting_randomize:
            random.shuffle(questions)

        # Apply Question Limit
        if self.setting_question_limit != "All":
            try:
                limit = int(self.setting_question_limit)
                questions = questions[:limit]
            except ValueError:
                pass

        # Shuffle choices for each question while preserving correct answer mapping
        if self.setting_randomize:
            for q in questions:
                self.shuffle_choices(q)

        return questions

    def shuffle_choices(self, question):
        choices = question["choices"]
        correct_idx = question["answer"]
        correct_choice_text = choices[correct_idx]

        combined = list(enumerate(choices))
        random.shuffle(combined)

        new_choices = []
        new_correct_idx = 0
        for new_pos, (old_idx, text) in enumerate(combined):
            new_choices.append(text)
            if old_idx == correct_idx:
                new_correct_idx = new_pos

        question["choices"] = new_choices
        question["answer"] = new_correct_idx

    def start_quiz_session(self):
        self.active_questions = self.prepare_quiz_questions()

        if not self.active_questions:
            messagebox.showwarning("No Questions", "No questions matched your current filter criteria!")
            return

        self.current_index = 0
        self.user_answers = {}
        self.user_evaluated = {}

        # Setup Timer
        if self.setting_mode == "Exam" and self.setting_timer_option != "Timer OFF":
            minutes = int(self.setting_timer_option.replace("m", "").replace(" minutes", "").strip())
            self.time_remaining_sec = minutes * 60
            self.timer_running = True
        else:
            self.timer_running = False

        self.render_quiz_view()

    def render_quiz_view(self):
        self.clear_main_container()

        if not self.active_questions:
            return

        q = self.active_questions[self.current_index]

        # Top Bar Info: Subject, Progress, Score, Timer
        info_panel = tk.Frame(self.main_container, bg=PANEL_MAIN, padx=15, pady=10)
        info_panel.pack(fill="x", pady=(0, 10))

        # Subject & Details
        lbl_subj = tk.Label(info_panel, text=f"{q['subject'].upper()} ({q['topic']})", font=self.font_body_bold, fg=PRIMARY_HOVER, bg=PANEL_MAIN)
        lbl_subj.pack(side="left")

        # Timer Display (if running)
        self.lbl_timer = tk.Label(info_panel, text="", font=self.font_body_bold, fg=WARNING_COLOR, bg=PANEL_MAIN)
        self.lbl_timer.pack(side="right", padx=10)
        if self.timer_running:
            self.update_timer_tick()

        # Score & Progress Counter
        total_q = len(self.active_questions)
        score_val = sum(1 for idx, evaluated in self.user_evaluated.items() if evaluated)
        lbl_progress = tk.Label(
            info_panel,
            text=f"Question {self.current_index + 1} of {total_q}  |  Score: {score_val}/{len(self.user_answers)}",
            font=self.font_body, fg=TEXT_WHITE, bg=PANEL_MAIN
        )
        lbl_progress.pack(side="right", padx=15)

        # Progress Bar
        pct = ((self.current_index + 1) / total_q)
        progress_frame = tk.Frame(self.main_container, bg=PANEL_SEC, height=8)
        progress_frame.pack(fill="x", pady=(0, 15))
        progress_fill = tk.Frame(progress_frame, bg=PRIMARY_COLOR, height=8, width=int(1150 * pct))
        progress_fill.pack(side="left")

        # Main Question Card
        q_card = tk.Frame(self.main_container, bg=PANEL_MAIN, highlightbackground=BORDER_COLOR, highlightthickness=1, padx=20, pady=20)
        q_card.pack(fill="both", expand=True)

        # Header tag: Difficulty + Bookmark/Favorite controls
        top_q_frame = tk.Frame(q_card, bg=PANEL_MAIN)
        top_q_frame.pack(fill="x")

        lbl_diff = tk.Label(top_q_frame, text=f"Difficulty: {q['difficulty']}", font=self.font_small, fg=TEXT_MUTED, bg=PANEL_MAIN)
        lbl_diff.pack(side="left")

        # Bookmark & Favorite Buttons
        q_id = q["id"]
        fav_text = "★ FAVORITE" if q_id in self.favorites else "☆ FAVORITE"
        bm_text = "🔖 BOOKMARKED" if q_id in self.bookmarks else "🔖 BOOKMARK"

        btn_fav = tk.Button(top_q_frame, text=fav_text, font=self.font_small, fg=WARNING_COLOR, bg=PANEL_SEC, bd=0, padx=8, pady=2, cursor="hand2", command=self.toggle_favorite_current)
        btn_fav.pack(side="right", padx=5)

        btn_bm = tk.Button(top_q_frame, text=bm_text, font=self.font_small, fg=TEXT_WHITE, bg=PANEL_SEC, bd=0, padx=8, pady=2, cursor="hand2", command=self.toggle_bookmark_current)
        btn_bm.pack(side="right")

        # Question Text
        lbl_q_num = tk.Label(q_card, text=f"QUESTION {self.current_index + 1}", font=self.font_body_bold, fg=TEXT_MUTED, bg=PANEL_MAIN)
        lbl_q_num.pack(anchor="w", pady=(10, 5))

        lbl_q_text = tk.Label(q_card, text=q["question"], font=self.font_qtext, fg=TEXT_WHITE, bg=PANEL_MAIN, wraplength=1000, justify="left")
        lbl_q_text.pack(anchor="w", pady=(0, 20))

        # Choices Area
        self.choice_btns = []
        labels = ["A", "B", "C", "D"]

        already_answered = self.current_index in self.user_answers
        user_choice = self.user_answers.get(self.current_index, None)

        for i, choice_text in enumerate(q["choices"]):
            btn_bg = INPUT_BTN
            btn_fg = TEXT_WHITE

            # Highlight logic if answered in Review mode
            if already_answered and self.setting_mode == "Review":
                if i == q["answer"]:
                    btn_bg = SUCCESS_COLOR
                elif i == user_choice and user_choice != q["answer"]:
                    btn_bg = ERROR_COLOR

            btn = tk.Button(
                q_card, text=f"  {labels[i]}.   {choice_text}", font=self.font_body,
                fg=btn_fg, bg=btn_bg, activebackground=PRIMARY_HOVER, activeforeground=TEXT_WHITE,
                bd=1, relief="solid", anchor="w", padx=15, pady=12, cursor="hand2",
                command=lambda idx=i: self.select_choice(idx)
            )
            btn.pack(fill="x", pady=5)
            
            if already_answered:
                btn.config(state="disabled")

            self.choice_btns.append(btn)

        # Feedback & Explanation Panel (Review Mode or Answered)
        self.exp_frame = tk.Frame(q_card, bg=PANEL_SEC, padx=15, pady=15, highlightbackground=BORDER_COLOR, highlightthickness=1)
        
        if already_answered and self.setting_mode == "Review":
            self.show_explanation_panel(user_choice, q)

        # Bottom Action Bar
        action_bar = tk.Frame(self.main_container, bg=BG_DARK)
        action_bar.pack(fill="x", pady=(15, 0))

        btn_prev = tk.Button(action_bar, text="PREVIOUS", font=self.font_body_bold, fg=TEXT_WHITE, bg=PANEL_MAIN, bd=0, padx=20, pady=10, cursor="hand2", command=self.previous_question)
        btn_prev.pack(side="left")
        if self.current_index == 0:
            btn_prev.config(state="disabled")

        if self.current_index == len(self.active_questions) - 1:
            btn_next = tk.Button(action_bar, text="FINISH & SUBMIT", font=self.font_body_bold, fg=TEXT_WHITE, bg=SUCCESS_COLOR, bd=0, padx=20, pady=10, cursor="hand2", command=self.finish_quiz)
        else:
            btn_next = tk.Button(action_bar, text="NEXT QUESTION", font=self.font_body_bold, fg=TEXT_WHITE, bg=PRIMARY_COLOR, bd=0, padx=20, pady=10, cursor="hand2", command=self.next_question)
            if not already_answered:
                btn_next.config(state="disabled")

        btn_next.pack(side="right")
        self.btn_next_ref = btn_next

    def select_choice(self, choice_idx):
        if self.current_index in self.user_answers:
            return # Prevent multiple answers

        q = self.active_questions[self.current_index]
        is_correct = (choice_idx == q["answer"])

        self.user_answers[self.current_index] = choice_idx
        self.user_evaluated[self.current_index] = is_correct

        # Record to persistent global history
        self.answers_history[q["id"]] = {"selected": choice_idx, "is_correct": is_correct}

        # Disable all choices
        for btn in self.choice_btns:
            btn.config(state="disabled")

        # Review Mode behavior
        if self.setting_mode == "Review":
            for i, btn in enumerate(self.choice_btns):
                if i == q["answer"]:
                    btn.config(bg=SUCCESS_COLOR)
                elif i == choice_idx and not is_correct:
                    btn.config(bg=ERROR_COLOR)

            self.show_explanation_panel(choice_idx, q)

        # Enable Next Button
        if hasattr(self, "btn_next_ref"):
            self.btn_next_ref.config(state="normal")

    def show_explanation_panel(self, choice_idx, q):
        self.exp_frame.pack(fill="x", pady=15)
        for w in self.exp_frame.winfo_children():
            w.destroy()

        is_correct = (choice_idx == q["answer"])
        labels = ["A", "B", "C", "D"]

        status_str = "✓ CORRECT" if is_correct else "✗ INCORRECT"
        status_color = SUCCESS_COLOR if is_correct else ERROR_COLOR

        lbl_status = tk.Label(self.exp_frame, text=status_str, font=self.font_header, fg=status_color, bg=PANEL_SEC)
        lbl_status.pack(anchor="w")

        if not is_correct:
            lbl_your = tk.Label(self.exp_frame, text=f"Your Answer: {labels[choice_idx]}. {q['choices'][choice_idx]}", font=self.font_body, fg=ERROR_COLOR, bg=PANEL_SEC)
            lbl_your.pack(anchor="w", pady=(2, 0))

        lbl_corr = tk.Label(self.exp_frame, text=f"Correct Answer: {labels[q['answer']]}. {q['choices'][q['answer']]}", font=self.font_body_bold, fg=SUCCESS_COLOR, bg=PANEL_SEC)
        lbl_corr.pack(anchor="w", pady=(2, 5))

        lbl_exp_heading = tk.Label(self.exp_frame, text="Explanation:", font=self.font_body_bold, fg=TEXT_WHITE, bg=PANEL_SEC)
        lbl_exp_heading.pack(anchor="w", pady=(5, 0))

        lbl_exp_body = tk.Label(self.exp_frame, text=q["explanation"], font=self.font_body, fg=TEXT_MUTED, bg=PANEL_SEC, wraplength=950, justify="left")
        lbl_exp_body.pack(anchor="w")

    def next_question(self):
        if self.current_index < len(self.active_questions) - 1:
            self.current_index += 1
            self.render_quiz_view()

    def previous_question(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.render_quiz_view()

    def finish_quiz(self):
        self.stop_timer()
        self.show_results_view()

    def update_timer_tick(self):
        if not self.timer_running:
            return

        if self.time_remaining_sec <= 0:
            self.timer_running = False
            messagebox.showinfo("Time Expired", "The exam timer has expired. Submitting your answers now!")
            self.finish_quiz()
            return

        m, s = divmod(self.time_remaining_sec, 60)
        h, m = divmod(m, 60)
        time_str = f"TIME REMAINING: {h:02d}:{m:02d}:{s:02d}"

        if hasattr(self, "lbl_timer") and self.lbl_timer.winfo_exists():
            self.lbl_timer.config(text=time_str)

        self.time_remaining_sec -= 1
        self.root.after(1000, self.update_timer_tick)

    def stop_timer(self):
        self.timer_running = False

    # Keyboard shortcut handlers
    def key_select_choice(self, idx):
        if hasattr(self, "choice_btns") and idx < len(self.choice_btns):
            self.select_choice(idx)

    def key_next_or_submit(self):
        if self.current_index in self.user_answers:
            if self.current_index == len(self.active_questions) - 1:
                self.finish_quiz()
            else:
                self.next_question()

    def reset_quiz_run(self):
        self.start_quiz_session()

    def toggle_favorite_current(self):
        if self.active_questions:
            q_id = self.active_questions[self.current_index]["id"]
            if q_id in self.favorites:
                self.favorites.remove(q_id)
            else:
                self.favorites.add(q_id)
            self.render_quiz_view()

    def toggle_bookmark_current(self):
        if self.active_questions:
            q_id = self.active_questions[self.current_index]["id"]
            if q_id in self.bookmarks:
                self.bookmarks.remove(q_id)
            else:
                self.bookmarks.add(q_id)
            self.render_quiz_view()

    # ============================================================
    # VIEW: RESULTS SCREEN
    # ============================================================
    def show_results_view(self):
        self.clear_main_container()

        total = len(self.active_questions)
        correct = sum(1 for idx, evaluated in self.user_evaluated.items() if evaluated)
        incorrect = total - correct
        pct = (correct / total * 100) if total > 0 else 0.0

        card = tk.Frame(self.main_container, bg=PANEL_MAIN, highlightbackground=BORDER_COLOR, highlightthickness=1, padx=30, pady=30)
        card.pack(fill="both", expand=True)

        tk.Label(card, text="BOARD EXAM REVIEW RESULTS", font=self.font_header, fg=TEXT_WHITE, bg=PANEL_MAIN).pack()
        tk.Label(card, text="========================================", font=self.font_body, fg=BORDER_COLOR, bg=PANEL_MAIN).pack()

        tk.Label(card, text=f"{pct:.1f}%", font=("Segoe UI", 42, "bold"), fg=SUCCESS_COLOR if pct >= 70 else ERROR_COLOR, bg=PANEL_MAIN).pack(pady=10)
        tk.Label(card, text=f"FINAL SCORE: {correct} / {total}", font=self.font_subtitle, fg=TEXT_WHITE, bg=PANEL_MAIN).pack()

        # Metrics Breakdown
        metrics_frame = tk.Frame(card, bg=PANEL_MAIN)
        metrics_frame.pack(pady=20)

        m_correct = tk.Frame(metrics_frame, bg=PANEL_SEC, padx=20, pady=10)
        m_correct.pack(side="left", padx=10)
        tk.Label(m_correct, text="CORRECT", font=self.font_small, fg=TEXT_MUTED, bg=PANEL_SEC).pack()
        tk.Label(m_correct, text=str(correct), font=self.font_header, fg=SUCCESS_COLOR, bg=PANEL_SEC).pack()

        m_incorrect = tk.Frame(metrics_frame, bg=PANEL_SEC, padx=20, pady=10)
        m_incorrect.pack(side="left", padx=10)
        tk.Label(m_incorrect, text="INCORRECT", font=self.font_small, fg=TEXT_MUTED, bg=PANEL_SEC).pack()
        tk.Label(m_incorrect, text=str(incorrect), font=self.font_header, fg=ERROR_COLOR, bg=PANEL_SEC).pack()

        # Action Buttons
        btn_box = tk.Frame(card, bg=PANEL_MAIN)
        btn_box.pack(pady=20)

        tk.Button(btn_box, text="RETRY QUIZ", font=self.font_body_bold, fg=TEXT_WHITE, bg=PRIMARY_COLOR, bd=0, padx=20, pady=10, cursor="hand2", command=self.start_quiz_session).pack(side="left", padx=10)
        tk.Button(btn_box, text="REVIEW WRONG ANSWERS", font=self.font_body_bold, fg=TEXT_WHITE, bg=INPUT_BTN, bd=0, padx=20, pady=10, cursor="hand2", command=self.show_wrong_answers_view).pack(side="left", padx=10)
        tk.Button(btn_box, text="RETURN TO DASHBOARD", font=self.font_body_bold, fg=TEXT_WHITE, bg=PANEL_SEC, bd=0, padx=20, pady=10, cursor="hand2", command=self.show_dashboard_view).pack(side="left", padx=10)

    # ============================================================
    # VIEW: SUBJECTS
    # ============================================================
    def show_subjects_view(self):
        self.clear_main_container()

        tk.Label(self.main_container, text="BOARD EXAM SUBJECTS", font=self.font_header, fg=TEXT_WHITE, bg=BG_DARK).pack(anchor="w", pady=(0, 15))

        subjects_grid = tk.Frame(self.main_container, bg=BG_DARK)
        subjects_grid.pack(fill="both", expand=True)

        for i, subj in enumerate(ALL_SUBJECTS):
            count = sum(1 for q in RAW_QUESTIONS if q["subject"] == subj)
            
            card = tk.Frame(subjects_grid, bg=PANEL_MAIN, highlightbackground=BORDER_COLOR, highlightthickness=1, padx=15, pady=15)
            card.grid(row=i//3, column=i%3, sticky="nsew", padx=5, pady=5)
            subjects_grid.grid_columnconfigure(i%3, weight=1)

            tk.Label(card, text=subj, font=self.font_body_bold, fg=TEXT_WHITE, bg=PANEL_MAIN).pack(anchor="w")
            tk.Label(card, text=f"{count} Practice Questions", font=self.font_small, fg=TEXT_MUTED, bg=PANEL_MAIN).pack(anchor="w", pady=(2, 10))

            btn = tk.Button(
                card, text="Filter & Review", font=self.font_small, fg=TEXT_WHITE, bg=PRIMARY_COLOR, bd=0, padx=10, pady=5, cursor="hand2",
                command=lambda s=subj: self.quick_filter_subject(s)
            )
            btn.pack(anchor="w")

    def quick_filter_subject(self, subj):
        self.setting_subject = subj
        self.start_quiz_session()

    # ============================================================
    # VIEW: FAVORITES & BOOKMARKS
    # ============================================================
    def show_favorites_view(self):
        fav_questions = [q for q in RAW_QUESTIONS if q["id"] in self.favorites]
        self.render_question_list_view("FAVORITE QUESTIONS", fav_questions)

    def show_bookmarks_view(self):
        bm_questions = [q for q in RAW_QUESTIONS if q["id"] in self.bookmarks]
        self.render_question_list_view("BOOKMARKED QUESTIONS", bm_questions)

    def show_wrong_answers_view(self):
        wrong_ids = [q_id for q_id, res in self.answers_history.items() if not res["is_correct"]]
        wrong_questions = [q for q in RAW_QUESTIONS if q["id"] in wrong_ids]
        self.render_question_list_view("INCORRECTLY ANSWERED QUESTIONS", wrong_questions)

    def render_question_list_view(self, title_text, question_list):
        self.clear_main_container()

        tk.Label(self.main_container, text=title_text, font=self.font_header, fg=TEXT_WHITE, bg=BG_DARK).pack(anchor="w", pady=(0, 15))

        if not question_list:
            tk.Label(self.main_container, text="No questions found in this category.", font=self.font_body, fg=TEXT_MUTED, bg=BG_DARK).pack(anchor="w")
            return

        scroll_frame = tk.Frame(self.main_container, bg=BG_DARK)
        scroll_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(scroll_frame, bg=BG_DARK, highlightthickness=0)
        scrollbar = ttk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
        scrollable_inner = tk.Frame(canvas, bg=BG_DARK)

        scrollable_inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_inner, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        labels = ["A", "B", "C", "D"]
        for q in question_list:
            card = tk.Frame(scrollable_inner, bg=PANEL_MAIN, highlightbackground=BORDER_COLOR, highlightthickness=1, padx=15, pady=15)
            card.pack(fill="x", pady=5, expand=True)

            tk.Label(card, text=f"[{q['subject']}] - {q['topic']} ({q['difficulty']})", font=self.font_small, fg=PRIMARY_HOVER, bg=PANEL_MAIN).pack(anchor="w")
            tk.Label(card, text=q["question"], font=self.font_body_bold, fg=TEXT_WHITE, bg=PANEL_MAIN, wraplength=900, justify="left").pack(anchor="w", pady=(5, 10))

            tk.Label(card, text=f"Correct Answer: {labels[q['answer']]}. {q['choices'][q['answer']]}", font=self.font_body, fg=SUCCESS_COLOR, bg=PANEL_MAIN).pack(anchor="w")
            tk.Label(card, text=f"Explanation: {q['explanation']}", font=self.font_small, fg=TEXT_MUTED, bg=PANEL_MAIN, wraplength=900, justify="left").pack(anchor="w", pady=(2, 0))

    # ============================================================
    # VIEW: SEARCH
    # ============================================================
    def show_search_view(self):
        self.clear_main_container()

        tk.Label(self.main_container, text="SEARCH QUESTION BANK", font=self.font_header, fg=TEXT_WHITE, bg=BG_DARK).pack(anchor="w", pady=(0, 15))

        search_bar_frame = tk.Frame(self.main_container, bg=BG_DARK)
        search_bar_frame.pack(fill="x", pady=(0, 15))

        self.ent_search = tk.Entry(search_bar_frame, font=self.font_body, bg=PANEL_MAIN, fg=TEXT_WHITE, insertbackground=TEXT_WHITE, bd=1, relief="solid")
        self.ent_search.pack(side="left", fill="x", expand=True, padx=(0, 10), ipady=8)
        self.ent_search.bind("<Return>", lambda e: self.perform_search())

        btn_search = tk.Button(
            search_bar_frame, text="SEARCH", font=self.font_body_bold, fg=TEXT_WHITE, bg=PRIMARY_COLOR,
            activebackground=PRIMARY_HOVER, bd=0, padx=20, pady=8, cursor="hand2", command=self.perform_search
        )
        btn_search.pack(side="right")

        self.search_results_container = tk.Frame(self.main_container, bg=BG_DARK)
        self.search_results_container.pack(fill="both", expand=True)

    def perform_search(self):
        for widget in self.search_results_container.winfo_children():
            widget.destroy()

        query = self.ent_search.get().strip().lower()
        if not query:
            return

        results = [
            q for q in RAW_QUESTIONS
            if query in q["question"].lower()
            or query in q["subject"].lower()
            or query in q["topic"].lower()
            or query in q["explanation"].lower()
        ]

        self.render_question_list_view(f"SEARCH RESULTS FOR '{query}' ({len(results)} found)", results)

    # ============================================================
    # VIEW: SETTINGS
    # ============================================================
    def show_settings_view(self):
        self.clear_main_container()

        tk.Label(self.main_container, text="QUESTIONNAIRE SETTINGS", font=self.font_header, fg=TEXT_WHITE, bg=BG_DARK).pack(anchor="w", pady=(0, 15))

        card = tk.Frame(self.main_container, bg=PANEL_MAIN, highlightbackground=BORDER_COLOR, highlightthickness=1, padx=20, pady=20)
        card.pack(fill="x")

        # Subject Filter
        tk.Label(card, text="Default Subject Filter:", font=self.font_body_bold, fg=TEXT_WHITE, bg=PANEL_MAIN).grid(row=0, column=0, sticky="w", pady=10)
        cb_subj = ttk.Combobox(card, values=["ALL SUBJECTS"] + ALL_SUBJECTS, state="readonly", font=self.font_body)
        cb_subj.set(self.setting_subject)
        cb_subj.grid(row=0, column=1, sticky="w", padx=20)
        cb_subj.bind("<<ComboboxSelected>>", lambda e: setattr(self, 'setting_subject', cb_subj.get()))

        # Difficulty Filter
        tk.Label(card, text="Difficulty Level:", font=self.font_body_bold, fg=TEXT_WHITE, bg=PANEL_MAIN).grid(row=1, column=0, sticky="w", pady=10)
        cb_diff = ttk.Combobox(card, values=["All", "Easy", "Medium", "Hard"], state="readonly", font=self.font_body)
        cb_diff.set(self.setting_difficulty)
        cb_diff.grid(row=1, column=1, sticky="w", padx=20)
        cb_diff.bind("<<ComboboxSelected>>", lambda e: setattr(self, 'setting_difficulty', cb_diff.get()))

        # Mode Selection
        tk.Label(card, text="Quiz Mode:", font=self.font_body_bold, fg=TEXT_WHITE, bg=PANEL_MAIN).grid(row=2, column=0, sticky="w", pady=10)
        cb_mode = ttk.Combobox(card, values=["Review", "Exam"], state="readonly", font=self.font_body)
        cb_mode.set(self.setting_mode)
        cb_mode.grid(row=2, column=1, sticky="w", padx=20)
        cb_mode.bind("<<ComboboxSelected>>", lambda e: setattr(self, 'setting_mode', cb_mode.get()))

        # Timer Selection
        tk.Label(card, text="Exam Timer:", font=self.font_body_bold, fg=TEXT_WHITE, bg=PANEL_MAIN).grid(row=3, column=0, sticky="w", pady=10)
        cb_timer = ttk.Combobox(card, values=["Timer OFF", "30 minutes", "60 minutes", "90 minutes", "120 minutes"], state="readonly", font=self.font_body)
        cb_timer.set(self.setting_timer_option)
        cb_timer.grid(row=3, column=1, sticky="w", padx=20)
        cb_timer.bind("<<ComboboxSelected>>", lambda e: setattr(self, 'setting_timer_option', cb_timer.get()))

        # Questions Per Quiz
        tk.Label(card, text="Questions Per Session:", font=self.font_body_bold, fg=TEXT_WHITE, bg=PANEL_MAIN).grid(row=4, column=0, sticky="w", pady=10)
        cb_limit = ttk.Combobox(card, values=["5", "10", "20", "30", "All"], state="readonly", font=self.font_body)
        cb_limit.set(self.setting_question_limit)
        cb_limit.grid(row=4, column=1, sticky="w", padx=20)
        cb_limit.bind("<<ComboboxSelected>>", lambda e: setattr(self, 'setting_question_limit', cb_limit.get()))

# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = BoardExamQuestionnaireApp(root)
    root.mainloop()