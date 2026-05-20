import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import datetime

# --- Database Initialization ---
def setup_database():
    conn = sqlite3.connect('medical_system.db')
    cursor = conn.cursor()
    
    # Patient Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        contact TEXT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    
    # Diagnosis Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS diagnoses (
        diagnosis_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        symptoms TEXT,
        predicted_disease TEXT,
        date TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
    )
    ''')
    
    # Doctor Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS doctors (
        doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        specialization TEXT,
        contact TEXT
    )
    ''')
    
    conn.commit()
    conn.close()

# --- Main Application ---
class MedicalDiagnosisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Diagnosis System")
        self.root.geometry("700x550")
        self.root.configure(bg="#f4f4f9")
        
        self.current_user_id = None
        self.current_user_name = None
        
        setup_database()
        self.show_main_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_main_screen(self):
        self.clear_screen()
        
        # Header
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        header_frame.pack(fill=tk.X)
        header_label = tk.Label(header_frame, text="Medical Diagnosis System", fg="white", bg="#2c3e50", font=("Helvetica", 24, "bold"))
        header_label.pack(pady=20)
        
        # Content
        content_frame = tk.Frame(self.root, bg="#f4f4f9")
        content_frame.pack(expand=True)
        
        tk.Label(content_frame, text="Welcome! Please Login or Register", bg="#f4f4f9", font=("Helvetica", 14)).pack(pady=20)
        
        tk.Button(content_frame, text="Patient Login", font=("Helvetica", 12), width=20, bg="#3498db", fg="white", command=self.show_login_screen).pack(pady=10)
        tk.Button(content_frame, text="Patient Registration", font=("Helvetica", 12), width=20, bg="#2ecc71", fg="white", command=self.show_register_screen).pack(pady=10)
        tk.Button(content_frame, text="Exit System", font=("Helvetica", 12), width=20, bg="#e74c3c", fg="white", command=self.root.quit).pack(pady=10)

    def show_register_screen(self):
        self.clear_screen()
        
        header_frame = tk.Frame(self.root, bg="#2ecc71", height=60)
        header_frame.pack(fill=tk.X)
        tk.Label(header_frame, text="Patient Registration", fg="white", bg="#2ecc71", font=("Helvetica", 18, "bold")).pack(pady=15)
        
        form_frame = tk.Frame(self.root, bg="#f4f4f9")
        form_frame.pack(pady=20)
        
        # Form Fields
        tk.Label(form_frame, text="Full Name:", bg="#f4f4f9").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.reg_name = tk.Entry(form_frame, width=30)
        self.reg_name.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(form_frame, text="Age:", bg="#f4f4f9").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.reg_age = tk.Entry(form_frame, width=30)
        self.reg_age.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(form_frame, text="Gender:", bg="#f4f4f9").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.reg_gender = ttk.Combobox(form_frame, values=["Male", "Female", "Other"], width=27)
        self.reg_gender.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(form_frame, text="Contact No:", bg="#f4f4f9").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.reg_contact = tk.Entry(form_frame, width=30)
        self.reg_contact.grid(row=3, column=1, padx=10, pady=10)
        
        tk.Label(form_frame, text="Username:", bg="#f4f4f9").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.reg_user = tk.Entry(form_frame, width=30)
        self.reg_user.grid(row=4, column=1, padx=10, pady=10)
        
        tk.Label(form_frame, text="Password:", bg="#f4f4f9").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.reg_pass = tk.Entry(form_frame, width=30, show="*")
        self.reg_pass.grid(row=5, column=1, padx=10, pady=10)
        
        btn_frame = tk.Frame(self.root, bg="#f4f4f9")
        btn_frame.pack()
        tk.Button(btn_frame, text="Register", font=("Helvetica", 12), bg="#2ecc71", fg="white", width=15, command=self.register_patient).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Back", font=("Helvetica", 12), bg="#95a5a6", fg="white", width=15, command=self.show_main_screen).grid(row=0, column=1, padx=10)

    def register_patient(self):
        name = self.reg_name.get()
        age = self.reg_age.get()
        gender = self.reg_gender.get()
        contact = self.reg_contact.get()
        username = self.reg_user.get()
        password = self.reg_pass.get()
        
        if not all([name, age, gender, contact, username, password]):
            messagebox.showerror("Error", "All fields are required!")
            return
            
        try:
            conn = sqlite3.connect('medical_system.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO patients (name, age, gender, contact, username, password) VALUES (?, ?, ?, ?, ?, ?)",
                           (name, age, gender, contact, username, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration successful! You can now login.")
            self.show_main_screen()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_login_screen(self):
        self.clear_screen()
        
        header_frame = tk.Frame(self.root, bg="#3498db", height=60)
        header_frame.pack(fill=tk.X)
        tk.Label(header_frame, text="Patient Login", fg="white", bg="#3498db", font=("Helvetica", 18, "bold")).pack(pady=15)
        
        form_frame = tk.Frame(self.root, bg="#f4f4f9")
        form_frame.pack(pady=40)
        
        tk.Label(form_frame, text="Username:", bg="#f4f4f9", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.login_user = tk.Entry(form_frame, font=("Helvetica", 12), width=25)
        self.login_user.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(form_frame, text="Password:", bg="#f4f4f9", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.login_pass = tk.Entry(form_frame, font=("Helvetica", 12), width=25, show="*")
        self.login_pass.grid(row=1, column=1, padx=10, pady=10)
        
        btn_frame = tk.Frame(self.root, bg="#f4f4f9")
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Login", font=("Helvetica", 12), bg="#3498db", fg="white", width=15, command=self.login_patient).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Back", font=("Helvetica", 12), bg="#95a5a6", fg="white", width=15, command=self.show_main_screen).grid(row=0, column=1, padx=10)

    def login_patient(self):
        username = self.login_user.get()
        password = self.login_pass.get()
        
        conn = sqlite3.connect('medical_system.db')
        cursor = conn.cursor()
        cursor.execute("SELECT patient_id, name FROM patients WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            self.current_user_id = result[0]
            self.current_user_name = result[1]
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def show_dashboard(self):
        self.clear_screen()
        
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=60)
        header_frame.pack(fill=tk.X)
        tk.Label(header_frame, text=f"Dashboard - {self.current_user_name}", fg="white", bg="#2c3e50", font=("Helvetica", 18, "bold")).pack(pady=15)
        
        content_frame = tk.Frame(self.root, bg="#f4f4f9")
        content_frame.pack(expand=True, pady=20)
        
        tk.Button(content_frame, text="New Diagnosis", font=("Helvetica", 14), width=25, bg="#9b59b6", fg="white", command=self.show_diagnosis_screen).pack(pady=15)
        tk.Button(content_frame, text="View Medical History", font=("Helvetica", 14), width=25, bg="#e67e22", fg="white", command=self.show_history_screen).pack(pady=15)
        tk.Button(content_frame, text="Logout", font=("Helvetica", 14), width=25, bg="#7f8c8d", fg="white", command=self.logout).pack(pady=15)

    def show_diagnosis_screen(self):
        self.clear_screen()
        
        header_frame = tk.Frame(self.root, bg="#9b59b6", height=60)
        header_frame.pack(fill=tk.X)
        tk.Label(header_frame, text="Symptom Analysis", fg="white", bg="#9b59b6", font=("Helvetica", 18, "bold")).pack(pady=15)
        
        form_frame = tk.Frame(self.root, bg="#f4f4f9")
        form_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        
        tk.Label(form_frame, text="Select your symptoms:", bg="#f4f4f9", font=("Helvetica", 12, "bold")).pack(pady=10)
        
        self.symptoms_vars = {
            "Fever": tk.BooleanVar(),
            "Cough": tk.BooleanVar(),
            "Headache": tk.BooleanVar(),
            "Fatigue": tk.BooleanVar(),
            "Nausea": tk.BooleanVar(),
            "Shortness of Breath": tk.BooleanVar(),
            "Sore Throat": tk.BooleanVar()
        }
        
        cb_frame = tk.Frame(form_frame, bg="#f4f4f9")
        cb_frame.pack()
        
        for idx, (symptom, var) in enumerate(self.symptoms_vars.items()):
            ttk.Checkbutton(cb_frame, text=symptom, variable=var).grid(row=idx//3, column=idx%3, padx=15, pady=10, sticky="w")
            
        btn_frame = tk.Frame(form_frame, bg="#f4f4f9")
        btn_frame.pack(pady=30)
        
        tk.Button(btn_frame, text="Analyze", font=("Helvetica", 12), bg="#9b59b6", fg="white", width=15, command=self.analyze_symptoms).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Back to Dashboard", font=("Helvetica", 12), bg="#95a5a6", fg="white", width=15, command=self.show_dashboard).grid(row=0, column=1, padx=10)

    def analyze_symptoms(self):
        selected_symptoms = [sym for sym, var in self.symptoms_vars.items() if var.get()]
        
        if not selected_symptoms:
            messagebox.showwarning("Warning", "Please select at least one symptom.")
            return
            
        symptoms_str = ", ".join(selected_symptoms)
        
        # Simple rule-based prediction logic
        prediction = "Unknown (Please consult a doctor)"
        
        if "Fever" in selected_symptoms and "Cough" in selected_symptoms and "Shortness of Breath" in selected_symptoms:
            prediction = "Possible COVID-19 / Pneumonia"
        elif "Fever" in selected_symptoms and "Headache" in selected_symptoms and "Fatigue" in selected_symptoms:
            prediction = "Viral Fever / Flu"
        elif "Sore Throat" in selected_symptoms and "Cough" in selected_symptoms:
            prediction = "Common Cold"
        elif "Nausea" in selected_symptoms and "Headache" in selected_symptoms:
            prediction = "Migraine / Food Poisoning"
        elif "Fever" in selected_symptoms:
            prediction = "Mild Fever"
            
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Save to database
        conn = sqlite3.connect('medical_system.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO diagnoses (patient_id, symptoms, predicted_disease, date) VALUES (?, ?, ?, ?)",
                       (self.current_user_id, symptoms_str, prediction, current_date))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Diagnosis Result", f"Symptoms: {symptoms_str}\n\nPredicted Illness: {prediction}\n\nPlease note: This is a preliminary analysis. Consult a medical professional for accurate diagnosis.")
        self.show_dashboard()

    def show_history_screen(self):
        self.clear_screen()
        
        header_frame = tk.Frame(self.root, bg="#e67e22", height=60)
        header_frame.pack(fill=tk.X)
        tk.Label(header_frame, text="Medical History & Reports", fg="white", bg="#e67e22", font=("Helvetica", 18, "bold")).pack(pady=15)
        
        # Setup Treeview
        tree_frame = tk.Frame(self.root)
        tree_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        columns = ("Date", "Symptoms", "Predicted Disease")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=10)
        self.tree.heading("Date", text="Date & Time")
        self.tree.heading("Symptoms", text="Symptoms")
        self.tree.heading("Predicted Disease", text="Predicted Disease")
        
        self.tree.column("Date", width=150)
        self.tree.column("Symptoms", width=250)
        self.tree.column("Predicted Disease", width=200)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Load Data
        conn = sqlite3.connect('medical_system.db')
        cursor = conn.cursor()
        cursor.execute("SELECT date, symptoms, predicted_disease FROM diagnoses WHERE patient_id=? ORDER BY date DESC", (self.current_user_id,))
        records = cursor.fetchall()
        conn.close()
        
        for record in records:
            self.tree.insert("", tk.END, values=record)
            
        tk.Button(self.root, text="Back to Dashboard", font=("Helvetica", 12), bg="#95a5a6", fg="white", width=20, command=self.show_dashboard).pack(pady=10)

    def logout(self):
        self.current_user_id = None
        self.current_user_name = None
        self.show_main_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = MedicalDiagnosisApp(root)
    root.mainloop()
