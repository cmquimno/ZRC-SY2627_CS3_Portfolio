# Parent Class
class Patient:
    def __init__(self, name: str, bill_amount: float):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_bill_amount(self) -> float:
        return self.__bill_amount

    def set_bill_amount(self, bill_amount: float):
        self.__bill_amount = bill_amount

    def calculate_bill(self) -> float:
        return self.__bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient")

# Child Class 1: Senior Citizens
class SeniorPatient(Patient):
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)

    def calculate_bill(self) -> float:
        return self.get_bill_amount() * 0.80

    def display_patient_type(self):
        print("Patient Type:Senior Citizen")

# Child Class 2: PhilHealth Members
class PhilHealthPatient(Patient):
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)

    def calculate_bill(self) -> float:
        return self.get_bill_amount() * 0.85

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")

if __name__ == "__main__":
    print("Hospital Billing System")
    print("-----------------------")

    patients = [
        Patient("Juan Dela Cruz", 15000.00),
        SeniorPatient("Maria Santos", 15000.00),
        PhilHealthPatient("Pedro Reyes", 15000.00)
    ]

    for p in patients:
        print(f"Patient Name:  {p.get_name()}")
        p.display_patient_type()
        print(f"Original Bill: ₱{p.get_bill_amount():,.2f}")
        print(f"Final Bill: ₱{p.calculate_bill():,.2f}\n")