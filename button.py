import tkinter as tk


class Button:
    def __init__(self,
                 text: str,
                 background: str,
                 command,
                 x: int,
                 y: int):

        self.button = tk.Button(text=text,
                                background=background,
                                font=("'Segoe', 19"),
                                command=command)

        self.place(x=x, y=y)

    def place(self, x: int, y: int):
        self.button.place(x=x, y=y, width=115, height=79)
