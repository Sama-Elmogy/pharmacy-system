import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from itertools import cycle


# Define the Drug and Disease classes
class Drug:
    def __init__(self, name, effective_ingredient, production_date, expiration_date):
        self.name = name
        self.effective_ingredient = effective_ingredient
        self.production_date = production_date
        self.expiration_date = expiration_date


class Disease:
    def __init__(self, name):
        self.name = name
        self.drug_list = []


class MedicalSystem:
    def __init__(self):
        self.diseases = []

        # Prepopulate with 5 diseases and 7 drugs each
        disease_names = ["Flu", "Cold", "Covid-19", "Malaria", "Cancer"]
        drug_names = ["DrugA", "DrugB", "DrugC", "DrugD", "DrugE", "DrugF", "DrugG"]

        for disease_name in disease_names:
            disease = Disease(disease_name)
            for i, drug_name in enumerate(drug_names):
                effective_ingredient = f"Ingredient{i + 1}"
                production_date = "2023-01-01"
                expiration_date = "2025-01-01"
                drug = Drug(drug_name, effective_ingredient, production_date, expiration_date)
                disease.drug_list.append(drug)
            self.diseases.append(disease)

    def find_disease(self, disease_name):
        for disease in self.diseases:
            if disease.name == disease_name:
                return disease
        return None

    def add_disease(self, disease_name, drugs_info):
        disease = self.find_disease(disease_name)
        if not disease:
            disease = Disease(disease_name)
            self.diseases.append(disease)

        for drug_info in drugs_info:
            drug = Drug(*drug_info)
            disease.drug_list.append(drug)

    def edit_drug_details(self, disease_name, drug_name, new_details):
        disease = self.find_disease(disease_name)
        if not disease:
            return False
        for drug in disease.drug_list:
            if drug.name == drug_name:
                drug.name, drug.effective_ingredient, drug.production_date, drug.expiration_date = new_details
                return True
        return False

    def get_drugs(self, disease_name):
        disease = self.find_disease(disease_name)
        if not disease:
            return None
        return [(drug.name, drug.effective_ingredient, drug.production_date, drug.expiration_date) for drug in
                disease.drug_list]


# Create the GUI class using tkinter
class MedicalSystemGUI:
    def __init__(self, root, medical_system):
        self.root = root
        self.medical_system = medical_system
        self.root.title("Medical System")
        self.root.geometry("1000x800")  # Set window size (10*10 scaling, 1000x800 for visibility)

        self.main_menu()

    def main_menu(self):
        self.clear_window()

        # Display the doctor image
        try:
            doctor_image = PhotoImage(file="doctor.png")  # Ensure the doctor.png file is in the same directory
            doctor_label = tk.Label(self.root, image=doctor_image)
            doctor_label.image = doctor_image  # Keep a reference to avoid garbage collection
            doctor_label.pack(pady=10)
        except Exception as e:
            print(f"Error loading doctor image: {e}")

        # Display the patient image
        try:
            patient_image = PhotoImage(file="patient.png")  # Ensure the patient.png file is in the same directory
            patient_label = tk.Label(self.root, image=patient_image)
            patient_label.image = patient_image  # Keep a reference to avoid garbage collection
            patient_label.pack(pady=10)
        except Exception as e:
            print(f"Error loading patient image: {e}")

        tk.Label(self.root, text="Welcome to the Medical System!", font=("Arial", 16)).pack(pady=10)

        self.doctor_button = tk.Button(self.root, text="Doctor", command=self.doctor_menu, bg="lightblue", fg="black",
                                       font=("Arial", 12))
        self.doctor_button.pack(pady=10, ipadx=20, ipady=10)

        self.patient_button = tk.Button(self.root, text="Patient", command=self.patient_menu, bg="lightgreen",
                                        fg="black", font=("Arial", 12))
        self.patient_button.pack(pady=10, ipadx=20, ipady=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, bg="red", fg="white",
                                     font=("Arial", 12))
        self.exit_button.pack(pady=10, ipadx=20, ipady=10)

    def doctor_menu(self):
        self.clear_window()

        tk.Label(self.root, text="Doctor Menu", font=("Arial", 16)).pack(pady=10)

        self.add_disease_button = tk.Button(self.root, text="Add Disease and Drugs", command=self.add_disease,
                                            bg="lightyellow", font=("Arial", 12))
        self.add_disease_button.pack(pady=10, ipadx=20, ipady=10)

        self.edit_drug_button = tk.Button(self.root, text="Edit Drug Details", command=self.edit_drug, bg="lightblue",
                                          font=("Arial", 12))
        self.edit_drug_button.pack(pady=10, ipadx=20, ipady=10)

        self.undo_disease_button = tk.Button(self.root, text="Undo Disease", command=self.undo_disease, bg="lightcoral",
                                             font=("Arial", 12))
        self.undo_disease_button.pack(pady=10, ipadx=20, ipady=10)

        self.exit_button = tk.Button(self.root, text="Back to Main Menu", command=self.main_menu, bg="gray",
                                     font=("Arial", 12))
        self.exit_button.pack(pady=10, ipadx=20, ipady=10)

    def add_disease(self):
        self.clear_window()

        tk.Label(self.root, text="Enter Disease and Drug Details", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Disease Name:", font=("Arial", 12)).pack(pady=5)
        self.disease_name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.disease_name_entry.pack(pady=5)

        self.drug_entries = []

        for i in range(5):
            tk.Label(self.root, text=f"Drug {i + 1} Name:", font=("Arial", 12)).pack(pady=5)
            drug_name_entry = tk.Entry(self.root, font=("Arial", 12))
            drug_name_entry.pack(pady=5)
            self.drug_entries.append(drug_name_entry)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_disease, bg="lightgreen",
                                       font=("Arial", 12))
        self.submit_button.pack(pady=10, ipadx=20, ipady=10)

        self.back_button = tk.Button(self.root, text="Back to Doctor Menu", command=self.doctor_menu, bg="lightgray",
                                     font=("Arial", 12))
        self.back_button.pack(pady=5, ipadx=20, ipady=10)

    def submit_disease(self):
        disease_name = self.disease_name_entry.get()
        drugs_info = [(entry.get(), "Ingredient", "2023-01-01", "2025-01-01") for entry in self.drug_entries]

        self.medical_system.add_disease(disease_name, drugs_info)
        messagebox.showinfo("Success", "Disease and drugs added successfully!")
        self.doctor_menu()

    def edit_drug(self):
        self.clear_window()

        tk.Label(self.root, text="Edit Drug Details", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Disease Name:", font=("Arial", 12)).pack(pady=5)
        self.disease_name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.disease_name_entry.pack(pady=5)

        tk.Label(self.root, text="Drug Name:", font=("Arial", 12)).pack(pady=5)
        self.drug_name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.drug_name_entry.pack(pady=5)

        tk.Label(self.root, text="New Drug Name:", font=("Arial", 12)).pack(pady=5)
        self.new_drug_name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.new_drug_name_entry.pack(pady=5)

        tk.Label(self.root, text="New Ingredient:", font=("Arial", 12)).pack(pady=5)
        self.new_ingredient_entry = tk.Entry(self.root, font=("Arial", 12))
        self.new_ingredient_entry.pack(pady=5)

        tk.Label(self.root, text="New Production Date:", font=("Arial", 12)).pack(pady=5)
        self.new_production_date_entry = tk.Entry(self.root, font=("Arial", 12))
        self.new_production_date_entry.pack(pady=5)

        tk.Label(self.root, text="New Expiration Date:", font=("Arial", 12)).pack(pady=5)
        self.new_expiration_date_entry = tk.Entry(self.root, font=("Arial", 12))
        self.new_expiration_date_entry.pack(pady=5)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_edit_drug, bg="lightblue",
                                       font=("Arial", 12))
        self.submit_button.pack(pady=10, ipadx=20, ipady=10)

        self.back_button = tk.Button(self.root, text="Back to Doctor Menu", command=self.doctor_menu, bg="lightgray",
                                     font=("Arial", 12))
        self.back_button.pack(pady=5, ipadx=20, ipady=10)

    def submit_edit_drug(self):
        disease_name = self.disease_name_entry.get()
        drug_name = self.drug_name_entry.get()
        new_details = (
            self.new_drug_name_entry.get(),
            self.new_ingredient_entry.get(),
            self.new_production_date_entry.get(),
            self.new_expiration_date_entry.get()
        )

        if self.medical_system.edit_drug_details(disease_name, drug_name, new_details):
            messagebox.showinfo("Success", "Drug details updated successfully!")
        else:
            messagebox.showerror("Error", "Drug not found.")
        self.doctor_menu()

    def patient_menu(self):
        self.clear_window()

        tk.Label(self.root, text="Patient Menu", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Enter Disease Name:", font=("Arial", 12)).pack(pady=5)
        self.disease_name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.disease_name_entry.pack(pady=5)

        self.search_button = tk.Button(self.root, text="Search Drugs", command=self.search_drugs, bg="lightgreen",
                                       font=("Arial", 12))
        self.search_button.pack(pady=10, ipadx=20, ipady=10)

        self.exit_button = tk.Button(self.root, text="Back to Main Menu", command=self.main_menu, bg="gray",
                                     font=("Arial", 12))
        self.exit_button.pack(pady=10, ipadx=20, ipady=10)

    def search_drugs(self):
        disease_name = self.disease_name_entry.get()
        drugs = self.medical_system.get_drugs(disease_name)

        self.clear_window()

        if drugs is None:
            messagebox.showerror("Error", "Disease not found.")
            self.patient_menu()
            return

        tk.Label(self.root, text=f"Drugs for {disease_name}:", font=("Arial", 16)).pack(pady=10)

        # Create a Listbox and Scrollbar to display drugs
        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = tk.Listbox(self.root, width=60, height=15, yscrollcommand=scrollbar.set, font=("Arial", 22, 'bold'))
        listbox.pack(pady=10)

        # Define three white and burgundy colors
        burgundy_colors = cycle(['#E9D6D1', '#D6A6A1', '#6F2C3F'])  # Light to dark shades of white and burgundy

        for drug in drugs:
            drug_str = f"{drug[0]}: {drug[1]}, {drug[2]} to {drug[3]}"
            listbox.insert(tk.END, drug_str)
            listbox.itemconfig(tk.END, {'bg': next(burgundy_colors)})

        scrollbar.config(command=listbox.yview)

        self.exit_button = tk.Button(self.root, text="Back to Patient Menu", command=self.patient_menu, bg="lightgray",
                                     font=("Arial", 12))
        self.exit_button.pack(pady=10, ipadx=20, ipady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


def run_medical_system():
    root = tk.Tk()
    medical_system = MedicalSystem()
    app = MedicalSystemGUI(root, medical_system)
    root.mainloop()


if __name__ == "__main__":
    run_medical_system()
