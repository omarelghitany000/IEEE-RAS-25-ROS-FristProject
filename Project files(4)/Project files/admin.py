from student import Student
from course import Course


def admin_menu(admins, students,courses):
    print("\n--- Admin Menu ---")
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    for admin in admins:
        if admin.username == username and admin.password == password:
            print("Login successful.")
    while True:
        print("\n--- Admin Menu ---:")
        print("1.View all students")
        print("2. Add Student")
        print("3. Add Course")
        print("4. Enroll Student in Course")
        print("5. Assign Grade")
        print("6. Record Attendance")
        print("7. logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            for student in students:
                print(student)
        elif choice == '2':        
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            students.append(student)
            print("Student added.")

        elif choice == '3':
            name = input("Enter course name: ")
            course_id = input("Enter course ID: ")
            course = Course(name, course_id)
            courses.append(course)
            print("Course added.")

        elif choice == '4':
            sid = input("Enter student ID: ")
            cid = input("Enter course ID: ")

            student = next((s for s in students if s.student_id == sid), None)
            course = next((c for c in courses if c.course_id == cid), None)

            if student and course:
                student.enroll(course)
                print("Student enrolled.")
            else:
                print("Invalid student or course ID.")

        elif choice == '5':
            sid = input("Enter student ID: ")
            cid = input("Enter course ID: ")
            grade = input("Enter grade: ")

            student = next((s for s in students if s.student_id == sid), None)

            if student:
                student.add_grade(cid, grade)
                print("Grade assigned.")
            else:
                print("Student not found.")

        elif choice == '6':
            sid = input("Enter student ID: ")
            cid = input("Enter course ID: ")

            student = next((s for s in students if s.student_id == sid), None)

            if student:
                student.record_attendance(cid)
                print("Attendance recorded.")
            else:
                print("Student not found.")

        elif choice == '7':
            print("Logging out...")
            break
        else:
            print("Invalid choice.")
