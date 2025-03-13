import tkinter as tk
from tkinter import messagebox

def append_to_expression(symbol):
    current_text = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current_text + str(symbol))

def calculate():
    try:
        expression = entry_display.get()
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid expression: {e}")

def clear():
    entry_display.delete(0, tk.END)


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")


entry_display = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry_display.grid(row=0, column=0, columnspan=4)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1)
]

operators = [
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                       command=lambda text=text: append_to_expression(text))
    button.grid(row=row, column=col, padx=5, pady=5)


for (text, row, col) in operators:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                       command=lambda text=text: append_to_expression(text))
    button.grid(row=row, column=col, padx=5, pady=5)


button_equal = tk.Button(root, text="=", width=5, height=2, font=("Arial", 14), command=calculate)
button_equal.grid(row=5, column=3, padx=5, pady=5)

button_clear = tk.Button(root, text="C", width=5, height=2, font=("Arial", 14), command=clear)
button_clear.grid(row=5, column=2, padx=5, pady=5)

root.mainloop()
