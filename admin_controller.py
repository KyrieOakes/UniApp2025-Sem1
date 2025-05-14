from database import Database

def admin_menu():
    db = Database()  

    while True:
        print("\n--- Admin Menu ---")
        print("(s) Show all students")
        print("(g) Group students by grade")
        print("(p) Partition students (PASS/FAIL)")
        print("(r) Remove a student by ID")
        print("(c) Clear all student data")
        print("(x) Exit")

        choice = input("Enter your choice: ").lower()

        if choice == 's':
            students = db.list_all()
            if not students:
                print("No students found.")
            else:
                print("\n--- Student List ---")
                for s in students:
                    print(s)
        elif choice == 'g':
            groups = db.group_students_by_grade()
            if not groups:
                print("No students to group.")
            else:
                print("\n--- Grouped Students by Grade ---")
                for grade, students in sorted(groups.items()):
                    print(f"\nGrade: {grade}")
                    for s in students:
                        print(f"  {s}")
        elif choice == 'p':
            partitions = db.partition_students()
            if not partitions['pass'] and not partitions['fail']:
                print("No students to partition.")
            else:
                print("\n--- PASS Students ---")
                for s in partitions['pass']:
                    print(f"  {s}")
                print("\n--- FAIL Students ---")
                for s in partitions['fail']:
                    print(f"  {s}")
        elif choice == 'r':
            student_id = input("Enter the student ID to remove: ")
            try:
                db.remove_student_by_id(student_id)
                print(f"Student {student_id} removed successfully.")
            except KeyError as e:
                print(f"Error: {e}")
        elif choice == 'c':
            confirm = input("Are you sure you want to delete ALL student records? (yes/no): ").lower()
            if confirm == 'yes':
                db.clear_all()
                print("All student records have been cleared.")
            else:
                print("Operation cancelled. No data was deleted.")
        elif choice == 'x':
            print("Exiting admin system.")
            break
        else:
            print("Invalid input. Please try again.")