import tkinter as tk

root = tk.Tk()
root.title("ماشین حساب")
root.geometry("320x420")
root.config(bg="white")
root.resizable(False, False)

expression = ""


def press(num):
    global expression
    expression += str(num)
    equation.set(expression)


def equal_press():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("خطا")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)


equation = tk.StringVar()

entry_field = tk.Entry(
    root, textvariable=equation, font=("Arial", 20), bd=0, bg="#f5f5f5", justify="right"
)
entry_field.grid(
    row=0, column=0, columnspan=4, ipadx=8, ipady=20, padx=5, pady=5, sticky="nsew"
)

btn_style = {
    "font": ("Arial", 16),
    "bd": 0,
    "bg": "#e0e0e0",
    "fg": "black",
    "width": 5,
    "height": 2,
}
op_style = {
    "font": ("Arial", 16),
    "bd": 0,
    "bg": "#4a90e2",
    "fg": "white",
    "width": 5,
    "height": 2,
}

buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("C", 4, 2),
    ("+", 4, 3),
    ("⌫", 5, 0),
    ("=", 5, 1),
]

for text, row, col in buttons:
    style = btn_style
    cmd = lambda t=text: press(t)

    if text in {"+", "-", "*", "/", "="}:
        style = op_style

    if text == "C":
        cmd = clear
    elif text == "=":
        cmd = equal_press
    elif text == "⌫":
        cmd = backspace

    btn = tk.Button(root, text=text, command=cmd, **style)

    if text == "=":
        btn.grid(row=row, column=col, padx=3, pady=3, sticky="nsew", columnspan=3)
    else:
        btn.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
