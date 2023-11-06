import tkinter as tk

# Функция добавления цифры в поле
def button_num_click(num:int):
    current = entry.get()
    entry.delete(0, 9999)
    entry.insert(0, str(current) + str(num))

# Функция отчистки поля
def button_clear_click():
    entry.delete(0, 9999)

# Функция добавления плюсика в поле
def button_ammd_click(val:str):
    current = entry.get()
    entry.delete(0, 9999)
    entry.insert(0, str(current) + str(val))

# Функция решения примера в поле
def button_equal_click():
    current = entry.get()
    entry.delete(0, 9999)
    entry.insert(0, eval(current))

# Создание окна
root = tk.Tk()
root.title('Simple Calculator')
root.resizable(False, False)

# Создание поля теста
entry = tk.Entry(root, width=5, borderwidth=5)

# Размещение поля в приложении
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Создание кнопок
button_1 = tk.Button(root, text='1', padx=40, pady=20, command=lambda: button_num_click(1))
button_2 = tk.Button(root, text='2', padx=40, pady=20, command=lambda: button_num_click(2))
button_3 = tk.Button(root, text='3', padx=40, pady=20, command=lambda: button_num_click(3))

button_4 = tk.Button(root, text='4', padx=40, pady=20, command=lambda: button_num_click(4))
button_5 = tk.Button(root, text='5', padx=40, pady=20, command=lambda: button_num_click(5))
button_6 = tk.Button(root, text='6', padx=40, pady=20, command=lambda: button_num_click(6))

button_7 = tk.Button(root, text='7', padx=40, pady=20, command=lambda: button_num_click(7))
button_8 = tk.Button(root, text='8', padx=40, pady=20, command=lambda: button_num_click(8))
button_9 = tk.Button(root, text='9', padx=40, pady=20, command=lambda: button_num_click(9))

button_0 = tk.Button(root, text='0', padx=88, pady=20, command=lambda: button_num_click(0))
button_clear = tk.Button(root, text='Clear', padx=29, pady=20, command=lambda: button_clear_click())

button_plus = tk.Button(root, text='+', padx=40, pady=20, command=lambda: button_ammd_click('+'))
button_minus = tk.Button(root, text='-', padx=40, pady=20, command=lambda: button_ammd_click('-'))
button_equal = tk.Button(root, text='=', padx=39, pady=52, command=lambda: button_equal_click())

button_multiplication = tk.Button(root, text='*', padx=41, pady=20, command=lambda: button_ammd_click('*'))
button_division = tk.Button(root, text='/', padx=40, pady=20, command=lambda: button_ammd_click('/'))

# Размещение кнопок в приложении
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0, columnspan=2)
button_clear.grid(row=4, column=2)

button_plus.grid(row=5, column=0)
button_minus.grid(row=5, column=1)
button_equal.grid(row=5, column=2, rowspan=2)

button_multiplication.grid(row=6, column=0)
button_division.grid(row=6, column=1)

# Запуск приложения
root.mainloop()