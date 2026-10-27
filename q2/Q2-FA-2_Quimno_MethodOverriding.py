# Parent Class
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        # ERROR HANDLING 
        if bill_amount < 0:
            self.__bill_amount = 0.0
        else:
            self.__bill_amount = float(bill_amount)

    # GETTER/SETTER 
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # GETTER/SETTER
    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        # ERROR HANDLING 
        if bill_amount >= 0:
            self.__bill_amount = float(bill_amount)
        else:
            print("Error: Bill amount cannot be negative.")

    # CORE LOGIC
    def calculate_bill(self):
        return self.__bill_amount

# Child Class 1: Senior Citizens
class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)  # Reuses parent constructor structure

    # METHOD OVERRIDING 
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80

# Child Class 2: PhilHealth Members
class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    # METHOD OVERRIDING 
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85

if __name__ == "__main__":
    print("Hospital Billing System")
    print("-----------------------")

    regular_patient = Patient("Juan Dela Cruz", 15000.00)
    senior_patient = SeniorPatient("Maria Santos", 15000.00)
    philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000.00)

    patients = [regular_patient, senior_patient, philhealth_patient]

    for p in patients:
        print(f"Patient Name:  {p.get_name()}")
        print(f"Original Bill: ₱{p.get_bill_amount():,.2f}")
        print(f"Final Bill: ₱{p.calculate_bill():,.2f}")
        print()
