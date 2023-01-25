import tkinter as tk
from window import Window
from buttons import Button


# TODO...
window = Window(title='Calculator',
                width='500',
                height='557',
                is_resizable=False,
                icon_path='imgs/icon_calc.png',
                background_color='#666666')


def calculate(operation):
    '''
    TODO...
    '''
    global formula

    if operation == 'C':
        formula = '0'

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
buttons = ['C', 'del', 'X^2', '/',
           '7', '8', '9', '*',
           '4', '5', '6', '-',
           '1', '2', '3', '+',
           '+/-', '0', '.', '=']
place_button_x = 18
place_button_y = 140
button_width = 115
button_height = 79
button_font_type = 'Segoe'
button_font_size = 19

for button in buttons:
    get_label = lambda x=button: calculate(x)

    if button == 'C':
        Button(text=button,
               background='#ff6666',
               font_type=button_font_type,
               font_size=button_font_size,
               command=get_label,
               x=place_button_x,
               y=place_button_y,
               width=button_width,
               height=button_height)

    elif button == '=':
        Button(text=button,
               background='#9ACDB1',
               font_type=button_font_type,
               font_size=button_font_size,
               command=get_label,
               x=place_button_x,
               y=place_button_y,
               width=button_width,
               height=button_height)

    elif button in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        Button(text=button,
               background='#9ABFCD',
               font_type=button_font_type,
               font_size=button_font_size,
               command=get_label,
               x=place_button_x,
               y=place_button_y,
               width=button_width,
               height=button_height)

    else:
        Button(text=button,
               background='#99CCCC',
               font_type=button_font_type,
               font_size=button_font_size,
               command=get_label,
               x=place_button_x,
               y=place_button_y,
               width=button_width,
               height=button_height)

    place_button_x += 117
    if place_button_x > 400:
        place_button_x = 18
        place_button_y += 81


# TODO...
window.run()
