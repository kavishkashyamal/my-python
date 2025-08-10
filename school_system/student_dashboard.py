import json

#school data
school_details_file = "D:\maths and physics project\Python\Projects\school_system\school_details.json"
student_details = "D:\maths and physics project\Python\Projects\school_system\student_details.json"

with open(school_details_file, 'r') as school_details_file:
    school_data = json.load(school_details_file)

with open(student_details, 'r') as student_file:
    student_data = json.load(student_file)


print(f"Hello welcome to {school_data['name']} 's Managment System.")
print("Login......")



uname_input = input("Enter your username : ")
password_input = input("Enter your password here : ")

def login_check():
    user_found = False

    for user in student_data:
        if user['uname'] == uname_input:
            user_found = True
            if user['password'] == password_input:
                print(f"Welcome back...")
                print("Student details____")
                print(f"Name : {user['name']}")
                print(f"Username : {user['uname']}")
                print(f"Email : {user['email']}")
                print(f"Is Active : {user['isActive']}")
                return
            else:
                print("Incorrect password. Try again.")
                return
    if not user_found:
        print("Username not found.")
        print(f"Contact {school_data['name']} office or IT support.")
    
login_check()