import tkinter as tk


class Label:
    def __init__(self, initial_text: str):
        self.label_text = tk.Label(anchor='e',
                                   text=initial_text,
                                   font=('Segoe', 27, 'bold'),
                                   bg='#666666',
                                   fg='white',
                                   width=20,
                                   height=3)

        self.label_text.pack()

    def update_text(self, new_text: str):
        self.label_text.configure(text=new_text)
