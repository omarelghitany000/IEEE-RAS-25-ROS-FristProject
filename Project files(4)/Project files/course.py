from student import Student  
class Course:
    def __init__(self, name, credit_hours, department):
        self.name = name
        self.credit_hours = credit_hours
        self.department = department
        self.students = {}  # student_id → [True, False, ...]

    def add_student(self, student: Student):
        if student.student_id not in self.students:
            self.students[student.student_id] = []
            student.register_course(self.name)
        else:
            print(f"Student {student.name} is already in this course.")

    def mark_attendance(self, student_id, present=True):
        if student_id in self.students:
            self.students[student_id].append(present)
            print(f"Attendance marked for {student_id}: {'Present' if present else 'Absent'}")
        else:
            print(f"Student ID {student_id} is not registered in this course.")


    def to_dict(self):
        return {
            "name": self.name,
            "course_id": self.course_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["course_id"])
