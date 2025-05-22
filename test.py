from student import Student
from subject import Subject
from database import Database

def print_header(title: str):
    print(f"\n=== {title} ===")


def main():
    # Use test database file to avoid overwriting real data
    db = Database(path='students.data')

    # Clear the database
    print_header('Clear the database')
    db.clear_all()
    print('Database has been cleared.')

    # Add students
    print_header('Add new students with subjects')

    def create_student(name, email, password):
        s = Student(name=name, email=email, password=password)
        for _ in range(4):  # Each student gets 4 subjects
            subj = s.enroll()
        db.add_student(s)
        print(f" {s.name} added | ID={s.id} | Avg={s.average_mark():.2f} | Status={s.grade()}")
        return s

    s1 = create_student('Zhang San', 'zhangsan@university.com', 'Abcde123')
    s2 = create_student('Li Si', 'lisi@university.com', 'Qwert123')
    s3 = create_student('Alice Smith', 'alice@university.com', 'Alice123')
    s4 = create_student('Bob Lee', 'bob@university.com', 'BobLee123')
    s5 = create_student('Charlie Brown', 'charlie@university.com', 'Charlie321')
    # List all students
    print_header('List all students')
    for stu in db.list_all():
        avg = stu.average_mark()
        status = 'Pass' if stu.passed() else 'Fail'
        print(f"ID={stu.id}, Name={stu.name}, Avg Mark={avg:.2f}, Status={status}")

    # Retrieve student by email
    print_header('Get student by email')
    stu = db.get_student_by_email('zhangsan@university.com')
    print(f"Student found: {stu.name} (ID={stu.id})")

    # Enroll a subject
    print("Subjects enrolled by current student:")
    for sub in stu.subjects:
        print(f"Subject ID={sub.id}, Mark={sub.mark}, Grade={sub.grade}")

    # Change password
    print_header('Change the password')
    stu.change_password('Xyzabc123')
    db.update_student(stu)
    print(f"Updated password: {stu.password}")

    # Remove subject
    print_header('Remove subject')
    if stu.subjects:
        sub_id = stu.subjects[0].id
        stu.remove_subject(sub_id)
        db.update_student(stu)
        print(f"Removed subject -> {sub_id}")
    else:
        print('No subject found.')

    # Partition by pass/fail
    print_header('Pass / Fail')
    parts = db.partition_students()
    print('Students who pass the exam:', [s.name for s in parts['pass']])
    print('Students who fail the exam:', [s.name for s in parts['fail']])

    # Group students by WAM (Weighted Average Mark)
    print_header('Group by WAM')
    groups = db.group_students_by_grade()
    for avg, studs in groups.items():
        print(f"Average grade {avg}: {[s.name for s in studs]}")

    # Delete student
    print_header('Delete student')
    db.remove_student_by_id(s2.id)
    print(f"Deleted student ID={s2.id}")
    print('Current student list:', [s.name for s in db.list_all()])


    # print_header('Delete all - db')
    # db.clear_all()
    # print('Database is empty')

if __name__ == '__main__':
    main()
