class Attendance:
    def __init__(self):
        self.attendance_record = {}  # {student_id: [course_name1, course_name2, ...]}

    def mark_attendance(self, student_id, course_name):
        if student_id in self.attendance_record:
            self.attendance_record[student_id].append(course_name)
        else:
            self.attendance_record[student_id] = [course_name]
        print(f"Attendance marked for student {student_id} in course {course_name}")

    def view_attendance(self, student_id):
        if student_id in self.attendance_record:
            print(f"Attendance for student {student_id}: {self.attendance_record[student_id]}")
        else:
            print("No attendance record for this student.")
