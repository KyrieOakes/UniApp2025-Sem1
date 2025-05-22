import tkinter as tk
from tkinter import messagebox
from database import Database
from subject import Subject

db = Database()

def open_enrolment_window(student):
    win = tk.Tk() 
    win.title("Enrolment Stuff")
    win.geometry("400x300")

    box = tk.Frame(win)
    box.pack(pady=10)

    def update_list():
        for thing in box.winfo_children():
            thing.destroy()
        tk.Label(box, text=f"Picked Subjects ({len(student.subjects)}/4):").pack()
        for sbj in student.subjects:
            tk.Label(box, text=f"ID: {sbj.id}, Mark: {sbj.mark}, Grade: {sbj.grade}").pack()

    def do_enrol():
        if len(student.subjects) >= 4:
            messagebox.showwarning("Nope", "Max is 4 subjects.")
            return
        sid = sub_input.get()
        if sid.strip() == "":
            # Show error message if something goes wrong
            messagebox.showerror("Uhh...", "Type something!")
            return
        for s in student.subjects:
            if s.id == sid:
                # Show success message after enrolment
                messagebox.showinfo("Oops", "Already got that one.")
                return
        newsub = Subject(sid)
        student.subjects.append(newsub)
        db.update_student(student)
        messagebox.showinfo("Done", f"{sid} added.")
        sub_input.delete(0, tk.END)
        update_list()

    def change_pw():
        new_pw = pw_input.get()
        if new_pw == "":
            messagebox.showerror("Nah", "Type a password.")
            return
        student.password = new_pw
        db.update_student(student)
        messagebox.showinfo("Nice", "Password updated.")
        pw_input.delete(0, tk.END)

    def withdraw_box():
        w = tk.Toplevel()
        w.title("Remove Course")
        w.geometry("300x150")

        tk.Label(w, text="Which ID to remove?").pack(pady=5)
        id_input = tk.Entry(w)
        id_input.pack()

        def go_remove():
            target = id_input.get()
            for s in student.subjects:
                if s.id == target:
                    student.subjects.remove(s)
                    db.update_student(student)
                    messagebox.showinfo("Removed", f"{target} is gone.")
                    w.destroy()
                    update_list()
                    return
            messagebox.showerror("No match", "That ID doesn't exist.")

        tk.Button(w, text="Remove", command=go_remove).pack(pady=10)

    tk.Label(win, text=f"Hey {student.name}!").pack()

    tk.Label(win, text="Enter subject ID:").pack()
    sub_input = tk.Entry(win)
    sub_input.pack()

    tk.Button(win, text="Add", command=do_enrol).pack(pady=5)
    tk.Button(win, text="Withdraw", command=withdraw_box).pack(pady=5)

    tk.Label(win, text="Change Password:").pack()
    pw_input = tk.Entry(win, show="*")
    pw_input.pack()

    tk.Button(win, text="Update Password", command=change_pw).pack(pady=5)

    update_list()
    win.mainloop()
