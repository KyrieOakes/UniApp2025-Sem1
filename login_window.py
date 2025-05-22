import tkinter as tk
from tkinter import messagebox
from database import Database
from enrolment_window import open_enrolment_window

def windows():
    db = Database()
   
    def try_login():
        em = email_in.get()
        pw = pw_in.get()
        if em == "" or pw == "":
            # Show error popup if login fails
            messagebox.showerror("Oops", "Fill both fields plz")
            return
            # Search the student by email from database

        student = db.get_student_by_email(em)
        if student and student.password == pw:
            root.destroy()
            # If password is correct, login successful
            open_enrolment_window(student)
        else:
            messagebox.showerror("Nope", "Wrong info")
            # Show error popup if login fails

    root = tk.Tk()
    root.title("Log in here")
    root.geometry("300x150")

    tk.Label(root, text="Email:").pack()
    # Text entry box for entering email
    email_in = tk.Entry(root)
    email_in.pack()

    tk.Label(root, text="Password:").pack()
    pw_in = tk.Entry(root, show="*")
    pw_in.pack()

    tk.Button(root, text="Login", command=try_login).pack(pady=5)

    root.mainloop()
