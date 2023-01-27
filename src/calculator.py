'''
The module contains parameters, classes and methods for setting up, running and operating the calculator
'''

from src.widgets.window import Window
from src.widgets.label import Label
from src.widgets.button import Button

# List of calculator buttons
_BUTTONS = ['C', 'del', 'X^2', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '+/-', '0', '.', '=']


class Calculator:
    '''
    The class is responsible for setting up and operating the calculator
    '''
    def __init__(self):
        self._create_formula()
        self._create_window()
        self._create_label()
        self._configure_buttons()

    def run(self):
        '''
        Starts the calculator
        '''
        self.window.run()

    def _create_formula(self):
        '''
        Creates a variable for performing calculations
        '''
        self.formula = '0'

    def _create_window(self):
        '''
        Creates a window
        '''
        self.window = Window(title='Calculator',
                             width=500,
                             height=557,
                             is_resizable=False,
                             icon_path='src/widgets/icon_calc.png',
                             background_color='#666666')

    def _create_label(self):
        '''
        Creates a text label
        '''
        self.label = Label(initial_text='0')

    def _configure_buttons(self):
        '''
        Setting up buttons
        '''
        # Position of the first button
        place_button_x = 18
        place_button_y = 140

        # A loop for setting up and placing buttons
        for button in _BUTTONS:
            # Lambda function for performing calculations by pressing buttons
            button_command = lambda x=button: self._calculate(operation=x)

            # Setting colors for different buttons
            if button == 'C':
                Button(text=button,
                       background='#cd9898',
                       command=button_command,
                       x=place_button_x,
                       y=place_button_y)

            elif button == '=':
                Button(text=button,
                       background='#98cda5',
                       command=button_command,
                       x=place_button_x,
                       y=place_button_y)

            elif button in list('0123456789'):
                Button(text=button,
                       background='#9ABFCD',
                       command=button_command,
                       x=place_button_x,
                       y=place_button_y)

            else:
                Button(text=button,
                       background='#98b5cd',
                       command=button_command,
                       x=place_button_x,
                       y=place_button_y)

            # Setting the position of the buttons
            place_button_x += 117
            if place_button_x > 400:
                place_button_x = 18
                place_button_y += 81

    def _calculate(self, operation):
        '''
        Performs calculations

        :param str operation: calculation operation
        '''
        # Setting up calculations for various operations
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

        # Updating the text label after the calculations performed
        self.label.update_text(new_text=self.formula)
