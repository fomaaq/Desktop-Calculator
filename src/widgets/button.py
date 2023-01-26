'''
The module contains classes and methods for working with buttons
'''

import tkinter as tk


class Button:
    '''
    The class is used to create and place a button
    '''
    def __init__(self,
                 text: str,
                 background: str,
                 command,
                 x: int,
                 y: int):

        # Creating a button
        self.button = tk.Button(text=text,
                                background=background,
                                font=("'Segoe', 19"),
                                command=command)
        # Button placement
        self.place(x=x, y=y)

    def place(self, x: int, y: int):
        '''
        The method places the button
        '''
        self.button.place(x=x, y=y, width=115, height=79)
