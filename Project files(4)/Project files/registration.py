import json
# from college_b import College
from typing import Dict, List, Optional, Tuple
# from course import Course
# from college import College



# ===========================================================================================================================
def register_student():
        id = int(input(f"Enter Student ID: "))
        name = str(input(f"Enter Student Name: "))
        level = int(input(f"Enter Student Level: "))
        college = str(input(f"Enter Stedent College: "))
        try:
            with open('data_b.json', 'r+') as file:
                data = json.load(file)
                # data_2 = json.dumps(data,indent=2)
                # print (data_2)
                
                # Check if student already exists
                if any(s['id'] == id for s in data["students"]):
                     print (f"Student with ID {id} already exists")
                else:
                        
                    # Create new student record
                    new_student = {
                        "id": id,
                        "name": name,
                        "level": level,
                        "college": college,
                        "courses": [],
                        "attendance": {},
                        "grades": {}
                    }
                    
                    data["students"].append(new_student)
                    
                    # Save changes
                    file.seek(0)
                    json.dump(data, file, indent=4)
                    file.truncate()
                    
                    print(f"Student registered successfully")
                
        except FileNotFoundError:
            # Initialize new data file if doesn't exist
            initial_data = {
                'students': [{
                    "id": id,
                    "name": name,
                    "level": level,
                    "college": college,
                    "courses": [],
                    "attendance": {},
                    "grades": {}
                }],
                "professors": [],
                "courses": [],
                "colleges": []
            }
            with open('data_b.json', 'w') as file:
                json.dump(initial_data, file, indent=4)
        
            return True, "Student registered successfully (new file created)"
            
        except Exception as e:
            return False, f"Error saving student: {str(e)}"


def register_course(student_id: str, course_id: str):

        try:
            # with open('data_b.json', 'r+') as file:
            #     data = json.load(file)
                
            #     # Find student
            #     student = next((s for s in data['students'] if s['id'] == student_id), None)
            #     # print (student)
            #     if not student:
            #         print (f"Student not found")
                
            #     # Check maximum course limit (7 courses)
            #     if len(student['courses']) >= 7:
            #         print(f"Maximum course limit (7) reached")
            #     else:
            #     # Use College class to handle registration with all validations
            #         return 
                College.register_student_for_course(student_id, course_id)
                
        except Exception as e:
            return False, f"Course registration error: {str(e)}"
# ===========================================================================================================================



# ===========================================================================================================================
#  Drop a course for a student
    # @staticmethod
def drop_course(student_id: str, course_id: str ) :
        try:
            with open('data_b.json', 'r+') as file:
                data = json.load(file)
                
                # Find student
                student = next((s for s in data['students'] if s['id'] == student_id), None)
                if not student:
                    print (f"Student not found")
                
                # Check if registered for the course
                if course_id not in student['courses']:
                    print (f"Student is not registered for this course")
                
                # Remove course from student's records
                student['courses'].remove(course_id)
                
                if course_id in student['attendance']:
                    del student['attendance'][course_id]
                
                if course_id in student['grades']:
                    del student['grades'][course_id]
                
                # Save changes
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
                
                return True, f"Course dropped successfully"
                
        except Exception as e:
            return False, f"Error dropping course: {str(e)}"
# ===========================================================================================================================




# ===========================================================================================================================
#  Get all courses a student is registered for
def get_student_courses(student_id) :
        """
        Get all courses a student is registered for
        
        Args:
            student_id: Student ID
            data_file: JSON data file path
            
        Returns:
            Tuple of (success status, list of courses or error message)
        """
        try:
            with open('data_b.json', 'r') as file:
                data = json.load(file)
                
                student = next((s for s in data['students'] if s['id'] == student_id), None)
                if not student:
                    return False, "Student not found"
                
                registered_courses = []
                for course_id in student['courses']:
                    course = next((c for c in data['courses'] if c['id'] == course_id), None)
                    if course:
                        registered_courses.append(course)
                
                return True, registered_courses
                
        except Exception as e:
            return False, f"Error getting student courses: {str(e)}"
# ===========================================================================================================================



# ===========================================================================================================================
#   Get all available courses for a student based on their college and level
def get_available_courses(student_id: str, 
                            data_file: str = 'data.json') -> Tuple[bool, List[Dict] | str]:
        try:
            with open(data_file, 'r') as file:
                data = json.load(file)
                
                student = next((s for s in data['students'] if s['id'] == student_id), None)
                if not student:
                    return False, "Student not found"
                
                college = College(student['college'])
                return college.get_available_courses(student['level'], data_file)
                
        except Exception as e:
            return False, f"Error getting available courses: {str(e)}"
 # ===========================================================================================================================       



# ===========================================================================================================================

# Registration.register_student("002", "Ahmed sayed" ,2 ,"Ele.Engineering" )
# Registration.register_course("ST001", "MATH201")
