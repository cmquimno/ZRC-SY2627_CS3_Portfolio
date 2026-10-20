class CD:
    def __init__(self, name):
        self.name = name

    def display_director(self):
        print("Campus Director: ", self.name)

    def manage_campus(self):
        print(self.name, "manages the campus.")

class CID(CD):
    def __init__(self, name, division_name, budget, faculty_count):
        super().__init__(name)
        self.division_name = division_name
        self.budget = budget
        self.faculty_count = faculty_count

    def display_cid(self):
        print("Division:", self.division_name)

    def show_faculty(self):
        print("Faculty Count:", self.faculty_count)

class AcademicCoordinator(CID):
    def __init__(self, name, division_name, budget, faculty_count, subject):
        super().__init__(name, division_name, budget, faculty_count)
        self.subject = subject

    def display_subject(self):
        print("Subject:", self.subject)

class SubjectCoordinator(AcademicCoordinator):
    def __init__(self, name, division_name, budget, faculty_count, subject, section):
        super().__init__(name, division_name, budget, faculty_count, subject)
        self.section = section

    def display_section(self):
        print("Section:", self.section)

class DepartmentHead(CID):
    def __init__(self, name, division_name, budget, faculty_count, department):
        super().__init__(name, division_name, budget, faculty_count)
        self.department = department

    def display_department(self):
        print("Department:", self.department)

class FacultyMember(CID):
    def __init__(self, name, division_name, budget, faculty_count, specialization):
        super().__init__(name, division_name, budget, faculty_count)
        self.specialization = specialization

    def display_specialization(self):
        print("Specialization:", self.specialization)

class SSD(CD):
    def __init__(self, name, division_name, staff_count):
        super().__init__(name)
        self.division_name = division_name
        self.staff_count = staff_count

    def display_ssd(self):
        print("Division:", self.division_name)

    def show_staff(self):
        print("Staff Count:", self.staff_count)

class GuidanceCounselor(SSD):
    def __init__(self, name, division_name, staff_count, counselor_name):
        super().__init__(name, division_name, staff_count)
        self.counselor_name = counselor_name

    def display_counselor(self):
        print("Guidance Counselor:", self.counselor_name)