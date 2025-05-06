import json
import os
#from professor import assign_grades 
courses = ['math', 'physics', 'chemistry', 'biology', 'english', 'history', 'computer']
students = list(range(1001, 3000))

class Grading:
    def __init__(self):
        pass
    def load_grades_from_file(self):
        try:
            with open('data_b.json', 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"attendance": [], "grades": [], "professors": []}
        return data   
    def save_data(self,data):
        try:
            with open('data_b.json', 'w') as f:
                json.dump(data, f, indent=300)
                print(f"Data saved.")
                #print(f"Saved to:",os.path.abspath('data_b.json'))
        except IOError as e:
            print(f"Error saving data: {e}")
    def __assign_grades__(self):
        course_name = input("Enter course name: ")
        student_id = int(input("Enter student ID: "))
        while True:
            try:
                grade = float(input("Enter a grade: "))
                break
            except ValueError as V:
             print(f"{V} Enter a valid numder")
        if course_name in courses:
            if student_id in students:
                if grade>= 0 and grade<=100 :
                    data = self.load_grades_from_file()
                    updated = False
                    for item in data["grades"]:
                        if item["course"] == course_name and item["student_id"] == student_id:
                            item["grade"] = grade
                            updated = True
                            break
                    if not updated:
                        data["grades"].append({
                            "course": course_name,
                            "student_id": student_id,
                            "grade": grade
                        })

                    self.save_data(data)
                    print(f"Grade {grade} succefully assigned to student: {student_id} for course:{course_name} ")
                else:
                    print(f"the grade must be between 0 and 100!")
            else:
                print(f"there is no student with this ID!") 
        else:
            print(f"this course is not found in courses !")    

    def convert_to_GPA (self,grade):
            if grade >=90:
                return 4.0
            elif grade >=80:
                return 3.0
            elif grade >=70:
                return 2.0
            elif grade >=60:
                return 1.0
            else:
                return 0.0
    def calculate_gpa(self):
        student_ID = int(input("Enter student ID: "))
        total_gpa = 0
        total_courses = 0
        data = self.load_grades_from_file()
        try:
            for item in data.get("grades", []):
                if item["student_id"] == student_ID:
                    grade = item["grade"]
                    course = item["course"]   
                    gpa_point = self.convert_to_GPA(grade)
                    total_gpa += gpa_point
                    total_courses +=1
                    print(f"{course}: Grade= {grade}, GPA point={gpa_point}")  
            if total_courses ==0:
                print(f"No grades for this student!")
                return
            GPA = total_gpa / total_courses    
            print(f"\nGPA for student {student_ID} is : {GPA:.2f}")          
        except ZeroDivisionError:  
            print(f"{ZeroDivisionError}")  


if __name__ == "__main__":
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
        elif choice == '2':
            grading_system.calculate_gpa()   
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")