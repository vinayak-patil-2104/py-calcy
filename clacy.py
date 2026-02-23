import tkinter as tk

root = tk.Tk()
root.title("Calculator")

expression = ""

def press(key):
    global expression
    expression += str(key)
    entry.set(expression)

def evaluate():
    global expression
    try:
        result = eval(expression)
        entry.set(result)
        expression = str(result)
    except:
        entry.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    entry.set("")

# --- Display ---
entry = tk.StringVar()
tk.Entry(root, textvariable=entry, font=("Arial", 20), justify="right", bd=10).grid(row=0, column=0, columnspan=4)

# --- Buttons ---
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row, col = 1, 0
for btn in buttons:
    if btn == "=":
        tk.Button(root, text=btn, width=5, height=2, command=evaluate).grid(row=row, column=col)
    else:
        tk.Button(root, text=btn, width=5, height=2, command=lambda b=btn: press(b)).grid(row=row, column=col)
    col += 1
    if col == 4:
        col = 0
        row += 1

tk.Button(root, text="Clear", width=22, height=2, command=clear).grid(row=row, column=0, columnspan=4)

root.mainloop()