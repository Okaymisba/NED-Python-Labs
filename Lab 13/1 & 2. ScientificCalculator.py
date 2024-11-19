import tkinter as tk
import math

root = tk.Tk()
root.title("Simple Scientific Calculator")
root.geometry("300x400")
root.configure(bg="white")

display = tk.Entry(root, font=("Arial", 18), bg="black", fg="white", bd=10, insertwidth=2, width=14, justify="right")
display.grid(row=0, column=0, columnspan=4)


def add_to_display(value): display.insert(tk.END, value)


def clear_display(): display.delete(0, tk.END)


def calculate():
    try:
        result = eval(display.get())
        clear_display()
        display.insert(tk.END, result)
    except:
        clear_display()
        display.insert(tk.END, "Error")


def sci_function(func):
    try:
        val = float(display.get())
        clear_display()
        if func == "√":
            display.insert(tk.END, math.sqrt(val))
        elif func == "sin":
            display.insert(tk.END, math.sin(math.radians(val)))
        elif func == "cos":
            display.insert(tk.END, math.cos(math.radians(val)))
        elif func == "tan":
            display.insert(tk.END, math.tan(math.radians(val)))
    except:
        display.insert(tk.END, "Error")


buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3, "blue"),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3, "blue"),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3, "blue"),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 3, "blue"), ("=", 4, 2, "red"),
    ("C", 6, 0, "red"), ("√", 5, 1, "purple"), ("sin", 5, 2, "purple"),
    ("cos", 5, 3, "purple"), ("tan", 5, 0, "purple"),
]

for (text, row, col, *color) in buttons:
    cmd = (lambda x=text: add_to_display(x)) if text not in ("=", "C", "√", "sin", "cos", "tan") else (
        calculate if text == "=" else clear_display if text == "C" else lambda f=text: sci_function(f))
    bg_color = color[0] if color else "green"
    tk.Button(root, text=text, font=("Arial", 12), bg=bg_color, fg="white", width=4, height=2, command=cmd).grid(
        row=row, column=col, padx=5, pady=5)

root.mainloop()
