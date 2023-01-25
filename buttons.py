import tkinter as tk


class Button:
    def __init__(self,
                 text: str,
                 background: str,
                 font_type: str,
                 font_size: int,
                 command,
                 x: int,
                 y: int,
                 width: int,
                 height: int):

        self.button = tk.Button(text=text,
                                background=background,
                                font=(f"'{font_type}', {font_size}"),
                                command=command).place(x=x,
                                                       y=y,
                                                       width=width,
                                                       height=height)
