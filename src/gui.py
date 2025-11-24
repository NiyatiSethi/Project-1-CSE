import tkinter as tk
from tkinter import ttk
from database import add_faculty, get_all_faculty, update_faculty, delete_faculty

def start_app():
    root = tk.Tk()
    root.title("Faculty Data Manager")
    root.geometry("850x600")

    top_frame = tk.Frame(root)
    top_frame.pack(pady=10)

    tk.Label(top_frame, text="Name").grid(row=0, column=0)
    name_entry = tk.Entry(top_frame)
    name_entry.grid(row=0, column=1, padx=5)

    tk.Label(top_frame, text="Department").grid(row=1, column=0)
    dept_entry = tk.Entry(top_frame)
    dept_entry.grid(row=1, column=1, padx=5)

    tk.Label(top_frame, text="Qualification").grid(row=2, column=0)
    qual_entry = tk.Entry(top_frame)
    qual_entry.grid(row=2, column=1, padx=5)

    tk.Label(top_frame, text="Experience").grid(row=3, column=0)
    exp_entry = tk.Entry(top_frame)
    exp_entry.grid(row=3, column=1, padx=5)

    message = tk.Label(root, text="", fg="red")
    message.pack()

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    # Add Faculty
    def save_record():
        name = name_entry.get().strip()
        dept = dept_entry.get().strip()
        qual = qual_entry.get().strip()
        exp = exp_entry.get().strip()

        # Validation checks
        if not name or not dept or not qual or not exp:
            message.config(text="All fields are required", fg="red")
            return
        
        if any(char.isdigit() for char in name):
            message.config(text="Name cannot contain numbers", fg="red")
            return

        if not exp.isdigit():
            message.config(text="Experience must be a number", fg="red")
            return

        add_faculty(name, dept, qual, exp)
        load_records()
        message.config(text="Record added successfully!", fg="green")

    tk.Button(btn_frame, text="Add Faculty", width=15, command=save_record).grid(row=0, column=0, padx=10)

    selected_id = None
    # Table
    columns = ("id", "name", "dept", "qual", "exp")
    table = ttk.Treeview(root, columns=columns, show="headings")

    for col in columns:
        table.heading(col, text=col.title())

    table.pack(fill="both", expand=True, pady=10)

    # Load Records
    def load_records():
        for row in table.get_children():
            table.delete(row)

        for item in get_all_faculty():
            table.insert("", tk.END, values=item)

    load_records()

    # Row Selection
    def select_row(event):
        nonlocal selected_id
        current = table.focus()

        if current:
            values = table.item(current, "values")
            selected_id = values[0]

            # Fill inputs
            name_entry.delete(0, tk.END)
            dept_entry.delete(0, tk.END)
            qual_entry.delete(0, tk.END)
            exp_entry.delete(0, tk.END)

            name_entry.insert(0, values[1])
            dept_entry.insert(0, values[2])
            qual_entry.insert(0, values[3])
            exp_entry.insert(0, values[4])

    table.bind("<<TreeviewSelect>>", select_row)

    # Update record
    def update_record():
        if selected_id:
            name = name_entry.get().strip()
            dept = dept_entry.get().strip()
            qual = qual_entry.get().strip()
            exp = exp_entry.get().strip()

            if not name or not dept or not qual or not exp:
                message.config(text="Please fill all fields before updating", fg="red")
                return
            
            if any(char.isdigit() for char in name):
                message.config(text="Name cannot contain numbers", fg="red")
                return

            if not exp.isdigit():
                message.config(text="Experience must be a number", fg="red")
                return

            update_faculty(selected_id, name, dept, qual, exp)
            load_records()
            message.config(text="Record updated successfully!", fg="green")

    tk.Button(btn_frame, text="Update Faculty", width=15, command=update_record).grid(row=0, column=1, padx=10)

    # Delete record
    def delete_record():
        if selected_id:
            delete_faculty(selected_id)
            load_records()
            name_entry.delete(0, tk.END)
            dept_entry.delete(0, tk.END)
            qual_entry.delete(0, tk.END)
            exp_entry.delete(0, tk.END)
            message.config(text="Record deleted successfully!", fg="green")

    tk.Button(btn_frame, text="Delete Faculty", width=15, command=delete_record).grid(row=0, column=2, padx=10)

    root.mainloop()