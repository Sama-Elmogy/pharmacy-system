class Drug:
    def __init__(self, name, production_date, expiration_date):
        self.name = name
        self.production_date = production_date
        self.expiration_date = expiration_date

class MedicalSystem:
    def __init__(self):
        self.doctor_ids = [1, 2, 3]  # Example doctor IDs
        self.drugs = []

    def add_disease(self):
        # Placeholder function for adding diseases
        pass

    def edit_drug_details(self):
        # Placeholder function for editing drug details
        pass

    def undo_disease(self):
        # Placeholder function for undoing disease
        pass

    def get_drugs(self):
        # Placeholder function to get drugs
        for drug in self.drugs:
            print(f"Drug Name: {drug.name}")
            print(f"Production Date: {drug.production_date}")
            print(f"Expiration Date: {drug.expiration_date}")
            print("------------------------")

    def doctor_menu(self):
        while True:
            print("\nDoctor Options:")
            print("1. Add Disease and Drugs")
            print("2. Edit Drug Details")
            print("3. Undo Disease")
            print("4. Exit Doctor Menu")

            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.add_disease()
            elif choice == "2":
                self.edit_drug_details()
            elif choice == "3":
                self.undo_disease()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def run(self):
        while True:
            print("\nWelcome to the Medical System!")
            print("1. Doctor")
            print("2. Patient")
            print("3. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                doctor_id = input("Enter your Doctor ID: ").strip()
                if int(doctor_id) in self.doctor_ids:
                    print("Doctor ID validated. You can now add diseases and drugs.")
                    self.doctor_menu()
                else:
                    print("Invalid Doctor ID! Please enter a valid ID.")

            elif choice == "2":
                self.get_drugs()

            elif choice == "3":
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

# Main execution block
if __name__ == "__main__":
    system = MedicalSystem()
    system.run()
