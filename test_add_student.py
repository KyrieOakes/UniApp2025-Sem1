from student import Student
from database import Database

def add_test_student():
    try:
        test_student = Student(
            name="Alice Tester",
            email="alice.tester@university.com",
            password="Start12345"
        )

        db = Database()
        db.add_student(test_student)

        print(f"Test student added:\n{test_student}")

    except Exception as e:
        print(f"Failed to add test student: {e}")

if __name__ == "__main__":
    add_test_student()
