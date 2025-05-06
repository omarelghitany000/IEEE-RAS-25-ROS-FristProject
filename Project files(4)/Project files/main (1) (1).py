# from student_menu import student_menu
# from admin_menu import admin_menu

# from student import Student
# from admin import Admin
# from professor import Professor

import json
from student import load_data, save_data, load_student,login
from registration import register_course, register_student
from professor import load_professors
from Grading import Grading


def main():
    print ("----------------------------------")
    print ("WeLCOME TO THE UNIVERSITY SYSTEM")
    print ("----------------------------------")

    print ("\n1. STUDENT\n2. PROF\n3. ADMIN\n4. END")
    print()

    choice = input("Enter your choice: ")

    while True:

        if choice == "1":


            student_list= load_student()
            for stu in student_list:
                print(stu.id,stu.name)

            print("==== student Interface ====")
            print()
            print ("1. Register New Student\n2. Login\n")
            chose = input(f"Enter your choise: ")
            while True:
                if chose == "1":
                    register_student
                elif chose == "2":
                            student_logged = login(student_list)
                if student_logged:
                    while True:
                        print ("\n1. Register Cources\n2. Attendance\n3. Grading system\n4. Logout\n")
                        choice = input(f"How Can I Help YOU: ")
                        if choice == "1":
                            register_course
                            break
                        elif choice == "2":
                            # Attendance
                            pass    
                        elif choice == "3":
                            print("\n--- Grading System ---")
                            grading_system = Grading()
                            while True:
                                print("\nMain Menu")
                                print("1. Assign Grades")
                                print("2. Calculate GPA")
                                print("3. Exit")
                                choice = input("Enter your choice (1-3): ")

                                if choice == '1':
                                    grading_system.__assign_grades__()
                                    break
                                elif choice == '2':
                                    grading_system.calculate_gpa()
                                    break 
                                elif choice == '3':
                                    print("Goodbye!")
                                    break
                                else:
                                    print("Invalid choice. Try again.")
                                    continue
                            break
                            
                        elif choice == "4":
                            print(f"Logging out {student_logged.name}...\n")
                            break
                        else:
                            print("Invalid choice. Try again.")
                            continue
                else:
                    print("Invalid choice. Try again.")
                    continue
#=======================================================================================================================

        elif choice == "2":

            professors_list= load_professors()
            for prof in professors_list:
                print(prof.id,prof.name)
            print("==== Professor Interface ====")
            while True:
                professor_logged = login(professors_list)
                if professor_logged:
                    while True:
                        print("\nMain Menu")
                        print("1. Take Attendance")
                        print("2. Assign Grades")
                        print("3. Assign Course")
                        print("4. Logout")
                        choice = input("Enter your choice (1-4): ")
                        if choice == '1':
                            professor_logged.__take_attendance__()
                            break
                        elif choice == '2':
                            professor_logged.assign_grades()
                            break
                        elif choice == '3':
                            professor_logged.__assign_course__()
                            break  
                        elif choice == '4':
                            print(f"Logging out Dr. {professor_logged.name}...\n")
                            break
                        else:
                            print("Invalid choice. Try again.")
                            continue



#=======================================================================================================================


        elif choice == "3":

            print("==== Admin Interface ====")
            print("\n--- Admin Menu ---:")
            print ()
            print("1.View all students")
            print("2. Add Student")
            print("3. Add Course")
            print("4. Enroll Student in Course")
            print("5. Assign Grade")
            print("6. Record Attendance")
            print("7. logout")

            cho = input("Enter input: ") 
            while True:
                if cho == "1":
                    pass
                if cho == "2":
                    pass
                if cho == "1":
                    pass
                if cho == "1":
                    pass
                if cho == "1":
                    pass
                if cho == "1":
                    pass
                if cho == "1":
                    pass

        elif choice == "4":
            print ("===== closed ======")
            break

        else:
            print("Invalid choice. Try again.")
            continue

if __name__ == "__main__":
    main()
