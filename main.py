from student_controller import student_menu
from login_window import windows
from admin_controller import admin_menu

def main():
    while True:
        print("\n=== University System ===")
        print("Please choose an option:")
        print("(1) Student - CLI")
        print("(2) Student - GUI")
        print("(3) Admin")
        print("(0) Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            student_menu()
        elif choice == 2:
            windows()
        elif choice == 3:
            admin_menu()
        elif choice == 0:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()