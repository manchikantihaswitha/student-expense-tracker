
import tkinter as tk
from tkinter import messagebox
import json
import os
FILE_NAME="expenses.json"
print(os.path.abspath(FILE_NAME))
if os.path.exists(FILE_NAME):
    with open(FILE_NAME,"r") as file:
        expenses=json.load(file)
else:
    expenses=[]
total=sum(item[2] for item in expenses)

def add_expense():
    global total

    name = name_entry.get()
    category = category_entry.get()
    amount_text = amount_entry.get()

    if not name or not category or not amount_text:
        messagebox.showerror("Error", "Fill all fields!")
        return

    try:
        amount = float(amount_text)
        if amount <= 0:
            messagebox.showerror("Error", "Enter a positive amount!")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount!")
        return

    expenses.append([name,category,amount])
    total+=amount
    with open(FILE_NAME, "w") as file:
     json.dump(expenses,file,indent=4)

    total_label.config(text=f"Total Spent: ₹{total:.2f}")
    messagebox.showinfo("Success", "Expense added!")

    name_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)


def view_expenses():
    result = ""

    for item in expenses:
        result += (
            f"Name: {item[0]}\n"
            f"Category: {item[1]}\n"
            f"Amount: ₹{item[2]:.2f}\n"
            "--------------------\n"
        )

    if not result:
        result = "No expenses added yet!"
    else:
        result+=f"\nTOTAL AMOUNT SPENT:{total:.2f}"
    messagebox.showinfo("All Expenses", result)


root = tk.Tk()
root.title("Student Expense Tracker")
root.geometry("420x500")
root.configure(bg="#F1F5F9")

heading = tk.Label(
    root, text="Student Expense Tracker",
    font=("Arial", 18, "bold"),
    bg="#F1F5F9", fg="#1E3A8A"
)
heading.pack(pady=15)

total_label = tk.Label(
    root, text="Total Spent: ₹0.00",
    font=("Arial", 16, "bold"),
    bg="#DCFCE7", fg="#166534",
    padx=15, pady=10
)
total_label.pack(pady=10)

tk.Label(root, text="Expense Name", bg="#F1F5F9").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

tk.Label(root, text="Category", bg="#F1F5F9").pack()
category_entry = tk.Entry(root, width=30)
category_entry.pack(pady=5)

tk.Label(root, text="Amount (₹)", bg="#F1F5F9").pack()
amount_entry = tk.Entry(root, width=30)
amount_entry.pack(pady=5)

tk.Button(
    root, text="Add Expense",
    command=add_expense,
    bg="#2563EB", fg="white",
    width=20
).pack(pady=10)

tk.Button(
    root, text="View Expenses",
    command=view_expenses,
    bg="#059669", fg="white",
    width=20
).pack(pady=5)

tk.Button(
    root, text="Exit",
    command=root.destroy,
    bg="#DC2626", fg="white",
    width=20
).pack(pady=5)

root.mainloop()