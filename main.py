from student_controller import student_menu
from login_window import windows

if __name__ == "__main__":
    check = int(input("Are you a student?\nPlease enter:\n1 for student\n0 for admin\n"))

    if check not in [0, 1]:
        check = int(input("Invalid input. Please enter:\n1 for student\n0 for admin\n"))

    match check:
        case 1:
            windows()
        case 0:
            student_menu()
