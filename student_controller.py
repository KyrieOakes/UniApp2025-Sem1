from database import Database
from student import Student
from subject import Subject

db = Database()

def student_menu():
    while True:
        print("\n== Student Menu ==")
        print("1 - Sign up")
        print("2 - Log in")
        print("0 - Back")

        pick = input("Your pick: ")

        if pick == "1":
            signup()
        elif pick == "2":
            login()
        elif pick == "0":
            break
        else:
            print("Try again lol")

def signup():
    print("\n-- Register --")
    name = input("Name: ")
    email = input("Email (must be @university.com): ")
    pw = input("Password (Cap letter + 5 letters + 3 numbers): ")

    if not email.endswith("@university.com"):
        print("Email format wrong.")
        return

    if len(pw) < 8 or not pw[0].isupper():
        print("Password rules not met.")
        return

    if db.get_student_by_email(email):
        print("Already used email.")
        return

    stu = Student(name, email, pw)
    db.add_student(stu)
    print(f"Welcome {name}, your ID is {stu.id}")

def login():
    print("\n-- Log in --")
    email = input("Email: ")
    pw = input("Password: ")

    student = db.get_student_by_email(email)
    if student and student.password == pw:
        print(f"Hey {student.name}!")
        course_menu(student)
    else:
        print("Login failed.")

def course_menu(student):
    while True:
        print("\n== Course Things ==")
        print("1 - Enrol")
        print("2 - Drop")
        print("3 - See subjects")
        print("4 - Change pass")
        print("0 - Log out")

        pick = input("What now? ")

        if pick == "1":
            add_subject(student)
        elif pick == "2":
            drop_subject(student)
        elif pick == "3":
            show_subjects(student)
        elif pick == "4":
            update_pw(student)
        elif pick == "0":
            print("Bye.")
            break
        else:
            print("Try a real option")

def add_subject(student):
    if len(student.subjects) >= 4:
        print("4 subjects max.")
        return

    name = input("ID for new subject: ")
    for s in student.subjects:
        if s.id == name:
            print("Already got that one.")
            return

    new = Subject(name)
    student.subjects.append(new)
    db.update_student(student)
    print(f"{name} added! Mark: {new.mark}, Grade: {new.grade}")

def drop_subject(student):
    name = input("ID to remove: ")
    for s in student.subjects:
        if s.id == name:
            student.subjects.remove(s)
            db.update_student(student)
            print(f"{name} gone.")
            return
    print("Not found.")

def show_subjects(student):
    if not student.subjects:
        print("You got none.")
        return
    print("\n-- Your Subjects --")
    for s in student.subjects:
        print(f"{s.id} - {s.mark} - {s.grade}")

def update_pw(student):
    new = input("New password: ")
    if new == "":
        print("Nope, can't be blank.")
        return
    student.password = new
    db.update_student(student)
    print("Changed.")