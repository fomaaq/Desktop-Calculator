import tkinter as tk

# TODO...
window = tk.Tk()
window.title('Calculator')
window.geometry('500x557')
window.resizable(False, False)
icon_photo = tk.PhotoImage(file='imgs/icon_calc.png')
window.iconphoto(False, icon_photo)
window.configure(bg='#666666')


# TODO...
def calculate(operation):
    global formula

    if operation == 'C':
        formula = ''

    elif operation == 'del':
        formula = formula[0:-1]

    elif operation == 'X^2':
        formula = str((eval(formula)) ** 2)

    elif operation == '=':
        formula = str(eval(formula))

    elif operation == '+/-':
        formula = str((eval(formula)) * -1)

    else:
        if formula == '0':
            formula = ''
        formula += operation
    label_text.configure(text=formula)


# TODO...
formula = '0'
label_text = tk.Label(anchor='e',
                      text=formula,
                      font=('Segoe', 27, 'bold'),
                      bg='#666666',
                      fg='white',
                      width=20,
                      height=3)
label_text.pack()


# TODO...
buttons = ['C', 'del', 'X^2', '=',
           '1', '2', '3', '/', 
           '4', '5', '6', '*', 
           '7', '8', '9', '-', 
           '+/-', '0', '.', '+']
x = 18
y = 140
for button in buttons:
    get_label = lambda x=button: calculate(x)
    tk.Button(text=button, bg='#99CCCC', font=('Segoe', 19), command=get_label).place(x=x, y=y, width=115, height=79)
    x += 117
    if x > 400:
        x = 18
        y += 81


# TODO...
window.mainloop()
