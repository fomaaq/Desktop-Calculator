from window import Window
from label import Label
from button import Button


class Calculator:
    def __init__(self):
        self._BUTTONS = ['C', 'del', 'X^2', '/',
                         '7', '8', '9', '*',
                         '4', '5', '6', '-',
                         '1', '2', '3', '+',
                         '+/-', '0', '.', '=']

        self.formula = '0'

        self.window = Window(title='Calculator',
                             width=500,
                             height=557,
                             is_resizable=False,
                             icon_path='imgs/icon_calc.png',
                             background_color='#666666')

        self.label = Label(initial_text='0')

        self._configure_buttons()

    def run(self):
        self.window.run()

    def _calculate(self, operation):
        if operation == 'C':
            self.formula = '0'

        elif operation == 'del':
            self.formula = self.formula[0:-1]

        elif operation == 'X^2':
            self.formula = str((eval(self.formula)) ** 2)

        elif operation == '=':
            self.formula = str(eval(self.formula))

        elif operation == '+/-':
            self.formula = str((eval(self.formula)) * -1)

        else:
            if self.formula == '0':
                self.formula = ''
            self.formula += operation

        self.label.update_text(new_text=self.formula)

    def _configure_buttons(self):
        place_button_x = 18
        place_button_y = 140

        for button in self._BUTTONS:
            button_command = lambda x=button: self._calculate(operation=x)

            if button == 'C':
                Button(text=button,
                       background='#ff6666',
                       command=button_command,
                       x=place_button_x,
                       y=place_button_y)

            elif button == '=':
                Button(text=button,
                       background='#9ACDB1',
                       command=button_command,
                       x=place_button_x,
                       y=place_button_y)

            elif button in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                Button(text=button,
                       background='#9ABFCD',
                       command=button_command,
                       x=place_button_x,
                       y=place_button_y)

            else:
                Button(text=button,
                       background='#99CCCC',
                       command=button_command,
                       x=place_button_x,
                       y=place_button_y)

            place_button_x += 117
            if place_button_x > 400:
                place_button_x = 18
                place_button_y += 81
