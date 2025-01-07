# calculator_gui.py
import tkinter as tk
from Calculator import sum, subtract, multiply, divide, square, square_root, power # type: ignore

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x400")

def on_click(operation):
    num1 = float(entry1.get())
    num2 = float(entry2.get()) if entry2.get() else None
    
    if operation == 'add':
        result.set(sum(num1, num2))
    elif operation == 'subtract':
        result.set(subtract(num1, num2))
    elif operation == 'multiply':
        result.set(multiply(num1, num2))
    elif operation == 'divide':
        try:
            result.set(divide(num1, num2))
        except ZeroDivisionError as e:
            result.set(e)
    elif operation == 'square':
        result.set(square(num1))
    elif operation == 'square_root':
        try:
            result.set(square_root(num1))
        except ValueError as e:
            result.set(e)
    elif operation == 'power':
        result.set(power(num1, num2))
    else:
        result.set("Invalid operation")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

tk.Button(root, text="Add", command=lambda: on_click('add')).pack()
tk.Button(root, text="Subtract", command=lambda: on_click('subtract')).pack()
tk.Button(root, text="Multiply", command=lambda: on_click('multiply')).pack()
tk.Button(root, text="Divide", command=lambda: on_click('divide')).pack()
tk.Button(root, text="Square", command=lambda: on_click('square')).pack()
tk.Button(root, text="Square Root", command=lambda: on_click('square_root')).pack()
tk.Button(root, text="Power", command=lambda: on_click('power')).pack()

root.mainloop()




