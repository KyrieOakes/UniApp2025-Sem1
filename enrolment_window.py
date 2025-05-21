import tkinter as tk
from tkinter import messagebox
from database import Database
from subject import Subject

db = Database()

def open_enrolment_window(student):
    root = tk.Tk()
    root.title("Enrolment System")
    root.geometry("400x300")

    subject_frame = tk.Frame(root)
    subject_frame.pack(pady=10)

    def refresh_subject_list():
        for widget in subject_frame.winfo_children():
            widget.destroy()
        tk.Label(subject_frame, text=f"Enrolled Subjects ({len(student.subjects)}/4):").pack()
        for sub in student.subjects:
            tk.Label(subject_frame, text=f"ID: {sub.id}, Mark: {sub.mark}, Grade: {sub.grade}").pack()

    def enrol_subject():
        if len(student.subjects) >= 4:
            messagebox.showwarning("Limit Reached", "You can only enrol in up to 4 subjects.")
            return
        subject_name = subject_entry.get()
        if subject_name == "":
            messagebox.showerror("Error", "Subject name cannot be empty.")
            return
        for s in student.subjects:
            if s.id == subject_name:  # Prevent duplicate by ID input
                messagebox.showinfo("Duplicate", "Subject with same ID already enrolled.")
                return
        new_subject = Subject(subject_name)
        student.subjects.append(new_subject)
        db.update_student(student)
        messagebox.showinfo("Success", f"{subject_name} enrolled.")
        subject_entry.delete(0, tk.END)
        refresh_subject_list()

    def change_password():
        new_pw = password_entry.get()
        if new_pw == "":
            messagebox.showerror("Error", "Password cannot be empty.")
            return
        student.password = new_pw
        db.update_student(student)
        messagebox.showinfo("Success", "Password changed.")
        password_entry.delete(0, tk.END)

    def open_withdraw_window():
        win = tk.Toplevel()
        win.title("Withdraw Subject")
        win.geometry("300x150")

        tk.Label(win, text="Enter subject ID to remove:").pack(pady=5)
        entry = tk.Entry(win)
        entry.pack()

        def remove():
            subject_id = entry.get()
            for sub in student.subjects:
                if sub.id == subject_id:
                    student.subjects.remove(sub)
                    db.update_student(student)
                    messagebox.showinfo("Removed", f"Subject with ID {subject_id} removed.")
                    win.destroy()
                    refresh_subject_list()
                    return
            messagebox.showerror("Not Found", f"No subject with ID {subject_id} found.")

        tk.Button(win, text="Remove", command=remove).pack(pady=10)

    tk.Label(root, text=f"Hi {student.name}, welcome!").pack()

    tk.Label(root, text="Enter subject ID:").pack()
    subject_entry = tk.Entry(root)
    subject_entry.pack()

    tk.Button(root, text="Enrol", command=enrol_subject).pack(pady=5)
    tk.Button(root, text="Withdraw Subject", command=open_withdraw_window).pack(pady=5)

    tk.Label(root, text="Change Password:").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    tk.Button(root, text="Change Password", command=change_password).pack(pady=5)

    refresh_subject_list()
    root.mainloop()
