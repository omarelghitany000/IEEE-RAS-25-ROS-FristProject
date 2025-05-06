import json
from registration import register_student,register_course


def load_data():
    try:
        with open('data_b.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        
        #  Initialize new data file if doesn't exist
                data = {

        "colleges": [
            {
            "name": [],
            "departments": [],
            "courses": []
            },
            {
            "name": [],
            "departments": [],
            "courses": []
            }
        ],
        "courses": [],
        "professors": [],
        "students": [],
        "admins": []
        }

    return data

def save_data(data):
    try:
        with open('data_b.json', 'w') as file:
            json.dump(data, file, indent=300)
            print(f"Data saved.")
            #print(f"Saved to:",os.path.abspath('data_b.json'))
    except IOError as e:
        print(f"Error saving data: {e}")

def load_student():
    try:
        with open('data_b.json', 'r') as file:
            data = json.load(file)
            #print("DATA:",data)
            student_data= data.get("students", [])
            return [Student( int(s["id"]), s["name"], int(s["level"]), s["college"], s.get("courses","") ) for s in student_data]
        
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading Students: {e}")
        return []



class Student:
    def __init__(self, id: int, name: str, level: int, college: str, courses:str):
        self.id = id
        self.name = name
        self.level = level
        self.college = college
        self.courses = courses

        self.max_courses = 7


    def Register_student(self):
        return register_student()

    def Register_courses(self):
        return register_course()

        

    def view_attendance(self,studet_name):
        pass


    def view_grades(self):
        pass


    def calculate_GPA(self):
        pass




def login(student_list):
    try:
        stu_id = input(f"Enter your Student ID: ")
    except ValueError:
        print(f"please enter a valid numeric ID.")
        return None
    for stu in student_list:
        if stu_id == stu_id:
            print(f"Welcome {stu.name} !!")
            return stu
    print("Invalid ID. Try again.")
    return None





def main():
    student_list= load_student()
    for stu in student_list:
        print(stu.id,stu.name)

    print("==== student Interface ====")
    print()
    print ("1. Register New Student\n2. Login\n")
    chose = input(f"Enter your choise: ")
    while True:
        if chose == "1":
            register_student()
        elif chose == "2":
                    student_logged = login(student_list)
        if student_logged:
            while True:
                print ("\n1. Register Cources\n2. Attendance\n3. Grades\n4. GPA Clc\n5. Logout\n")
                choice = input(f"How Can I Help YOU: ")
                if choice == "1":
                    register_course()
                elif choice == "2":
                    # Attendance
                    pass    
                elif choice == "3":
                    # grades
                    break
                elif choice == "4":
                    # grades
                    break
                elif choice == "5":
                    print(f"Logging out {student_logged.name}...\n")
                    main() 
                else:
                    print("Invalid choice. Try again.")
                    continue
        else:
            print("Invalid choice. Try again.")
            continue


if __name__ == "__main__":
    main()