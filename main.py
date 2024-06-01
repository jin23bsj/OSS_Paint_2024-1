import tkinter as tk

window = tk.Tk()
window.title('계산기')

operator = 'none'
calculation = 0

def button_click(key=0):
    global num1, num2
    if operator == 'none':
        if print_value.get() == '0':
            print_value.set(str(key))
            num1 = key
        else:
            num1 *= 10
            num1 += key
            print_value.set(str(num1))
    else:
        if print_value.get() == '0' or num2 == 0:
            print_value.set(str(key))
            num2 = key
        else:
            num2 *= 10
            num2 += key
            print_value.set(str(num2))

def operator_click(op):
    global operator
    operator = op

def calculate():
    global num1, num2, operator
    if operator == '+':
        calculation = num1 + num2
    elif operator == '-':
        calculation = num1 - num2
    else:
        calculation = 0

    print_value.set(str(calculation))
    num1 = 0
    num2 = 0
    operator = 'none'

def initialize():
    global num1, num2, operator
    num1 = 0
    num2 = 0
    operator = 'none'
    print_value.set('0')

# 출입력 창
num1, num2 = 0, 0
print_value = tk.StringVar()
print_value.set(0)
display = tk.Entry(window, width=25, textvariable=print_value, justify='right', font=('Arial', 24))
display.grid(columnspan=4, row=0, ipadx=8, ipady=20, sticky='nsew')

# 버튼 크기 조절 및 배치
buttons = [
    ('1', 1, 1), ('2', 1, 2), ('3', 1, 3), ('C', 1, 4),
    ('4', 2, 1), ('5', 2, 2), ('6', 2, 3), ('+', 2, 4),
    ('7', 3, 1), ('8', 3, 2), ('9', 3, 3), ('-', 3, 4),
    ('0', 4, 1), ('=', 4, 4)
]

for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(window, text=text, command=initialize)
    elif text in '+-':
        button = tk.Button(window, text=text, command=lambda op=text: operator_click(op))
    elif text == '=':
        button = tk.Button(window, text=text, command=calculate)
    else:
        button = tk.Button(window, text=text, command=lambda key=int(text): button_click(key))
    button.grid(row=row, column=col, sticky='nsew', padx=1, pady=1)

# grid 행 및 열 크기 조절
for i in range(1, 5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

window.mainloop()
