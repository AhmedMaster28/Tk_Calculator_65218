# tk_calculator.py

import tkinter as tk
from tkinter import messagebox

# Function Definitions
def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_var.set(f"Result: {num1 + num2}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_var.set(f"Result: {num1 - num2}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_var.set(f"Result: {num1 * num2}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            raise ZeroDivisionError
        result_var.set(f"Result: {num1 / num2}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math error", "Cannot divide by zero.")

# GUI Setup
root = tk.Tk()
root.title("Simple Calculator")

# Widgets
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, pady=5)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, pady=5)

tk.Button(root, text="Add", width=10, command=add).grid(row=2, column=0, pady=5)
tk.Button(root, text="Subtract", width=10, command=subtract).grid(row=2, column=1, pady=5)
tk.Button(root, text="Multiply", width=10, command=multiply).grid(row=3, column=0, pady=5)
tk.Button(root, text="Divide", width=10, command=divide).grid(row=3, column=1, pady=5)

result_var = tk.StringVar()
result_var.set("Result:")
tk.Label(root, textvariable=result_var, font=("Arial", 12)).grid(row=4, columnspan=2, pady=10)

# Run the application
root.mainloop()
