class Student:
    def __init__(self, name: str, student_id: str):
        self._name = name
        self._student_id = student_id

class Course:
    def __init__(self, course_name: str):
        self._course_name = course_name
        self._students = [] 

    def add_student(self, student: Student) -> None:
        self._students.append(student)# Write a short Python code snippet showing a Course adding a Student object to a list. 