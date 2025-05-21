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
    print_header('Add new students')
    s1 = Student(name='Zhang San', email='zhangsan@university.com', password='Abcde123')
    db.add_student(s1)
    print(f"Added student: ID={s1.id}, Name={s1.name}, Email={s1.email}")

    s2 = Student(name='Li Si', email='lisi@university.com', password='Qwert123')
    db.add_student(s2)
    print(f"Added student: ID={s2.id}, Name={s2.name}, Email={s2.email}")

    # Additional demo students
    s3 = Student(name='Alice Smith', email='alice@university.com', password='Alice123')
    db.add_student(s3)
    print(f"Added student: ID={s3.id}, Name={s3.name}, Email={s3.email}")

    s4 = Student(name='Bob Lee', email='bob@university.com', password='BobLee123')
    db.add_student(s4)
    print(f"Added student: ID={s4.id}, Name={s4.name}, Email={s4.email}")

    s5 = Student(name='Charlie Brown', email='charlie@university.com', password='Charlie321')
    db.add_student(s5)
    print(f"Added student: ID={s5.id}, Name={s5.name}, Email={s5.email}")

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
    subject = stu.enroll()
    print(f"Enrolled successfully: Subject ID={subject.id}, Mark={subject.mark}, Grade={subject.grade}")

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
