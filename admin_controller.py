from database import Database

def admin_menu():
    db = Database()

    while True:
        print("\nAdmin System (c/g/p/r/s/x):")
        print("(c) clear database: Clear all data on students.data")
        print("(g) group students: Groups students by grade")
        print("(p) partition students: Partition students to PASS/FAIL categories")
        print("(r) remove student: Remove a student by ID")
        print("(s) show: Show all students")
        print("(x) exit")

        choice = input("Enter your choice: ").lower()

        if choice == 'c':
            print("Clearing students database")
            confirm = input("Are you sure you want to clear the database (Y)ES/(N)O: ").lower()
            if confirm == 'y':
                db.clear_all()
                print("Students data cleared")
            else:
                print("Operation cancelled. No data was deleted.")

        elif choice == 'g':
            print("\nGrade Grouping")
            groups = db.group_students_by_grade()
            if not groups:
                print("< Nothing to Display >")
            else:
                for grade, students in sorted(groups.items()):
                    for s in students:
                        avg = round(s.average_mark(), 2)
                        print(f"{grade} --> [{s.name} :: {s.id} --> GRADE: {s.grade()} - MARK: {avg}]")

        elif choice == 'p':
            print("\nPASS/FAIL Partition")
            partitions = db.partition_students()
            if not partitions['pass'] and not partitions['fail']:
                print("< Nothing to Display >")
            else:
                print("FAIL -->")
                if not partitions['fail']:
                    print("[]")
                else:
                    for s in partitions['fail']:
                        print(f"{s.name} :: {s.id} --> GRADE: {s.grade()} - MARK: {s.average_mark():.2f}")
                print("PASS -->")
                if not partitions['pass']:
                    print("[]")
                else:
                    for s in partitions['pass']:
                        print(f"{s.name} :: {s.id} --> GRADE: {s.grade()} - MARK: {s.average_mark():.2f}")

        elif choice == 'r':
            sid = input("Remove by ID: ")
            try:
                db.remove_student_by_id(sid)
                print(f"Removing Student {sid} Account")
            except KeyError:
                print(f"student {sid} does not exist")

        elif choice == 's':
            print("Student List")
            students = db.list_all()
            if not students:
                print("< Nothing to Display >")
            else:
                for s in students:
                    print(f"{s.name} :: {s.id} --> Email: {s.email}")

        elif choice == 'x':
            break

        else:
            print("Invalid input. Please try again.")