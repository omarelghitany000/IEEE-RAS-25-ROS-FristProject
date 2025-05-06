import json
import os
courses = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Computer']
students = list(range(1001, 3000))

def load_data():
    try:
        with open('data_b.json', 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"attendance": [], "grades": [], "professors": []}
    return data   

def save_data(data):
    try:
        with open('data_b.json', 'w') as f:
            json.dump(data, f, indent=300)
            print(f"Data saved.")
            #print(f"Saved to:",os.path.abspath('data.json'))
    except IOError as e:
        print(f"Error saving data: {e}")

def load_professors():
    try:
        with open('data_b.json', 'r') as f:
            data = json.load(f)
            #print("DATA:",data)
            professors_data= data.get("professors", [])
            return [Professor(p["name"], p.get("course", ""), p["id"]) for p in professors_data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading professors: {e}")
        return []        



class Professor:
    def __init__(self,name,course,id):
        self.name = name
        self.course = course
        self.id = id
        self.courses = courses
    def __take_attendance__(self):
        data = load_data()
        attendance_status = ["present","absent"]
        student_id = int(input("Entere student ID: "))
        try: 
            if student_id in students:
                status = input("Enter date if present: ")
                if status not in attendance_status:
                    print(f"Invalid status!")
                    return
                attendance_record = {"course":self.course,"student_id":student_id,"status":status}
                #print(f"Before append: ",data)
                data["attendance"].append(attendance_record)
                save_data(data)
                #print(f"After append: ",data)
                print(f"{student_id}'s status is {status} in {self.course} ")
            else:
                print(f"there is no student with this ID!")           
        except ValueError:
            print(f"this course is not found in courses !") 
                          
    def assign_grades(self):
        data = load_data()
        student_id = int(input("Entere student ID: "))
        while True:
            try:
                grade = float(input("Enter a grade: "))
                break
            except ValueError as V:
             print(f"{V} Enter a valid numder")
        if student_id in students:
            grade_record = { "course":self.course,"student_id":student_id,"grade":grade}
            #print(f"Before append: ",data)
            data["grades"].append(grade_record)
            save_data(data)
            #print(f"After append: ",data)
            print(f"Grade {grade} succefully assigned to student: {student_id} for course:{self.course} ")
        else:
            print(f"there is no student with this ID!")   
    
               
    def __assign_course__(self):
        course = input("Enter course name: ")
        try:
         if course in self.courses:
            print(f"course is already exist!")
         else:
            self.courses.append(course)
            print(f"This course {course} has been added to the professor {self.name}.")    
        except ValueError:
            print(f"this course is not found in courses !")


def login(professors_list):
    try:
        prof_id = int(input("Enter your Professor ID: "))
    except ValueError:
        print(f"please enter a valid numeric ID.")
        return None
    for prof in professors_list:
        if prof.id == prof_id:
            print(f"Welcome Dr. {prof.name}!")
            return prof
    print("Invalid ID. Try again.")
    return None

if __name__ == "__main__":
    professors_list= load_professors()
    for prof in professors_list:
        print(prof.id,prof.name)
    print("--- Professor's System ---")
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
                elif choice == '2':
                    professor_logged.assign_grades()
                elif choice == '3':
                    professor_logged.__assign_course__()    
                elif choice == '4':
                    print(f"Logging out Dr. {professor_logged.name}...\n")
                    break
                else:
                    print("Invalid choice. Try again.")

