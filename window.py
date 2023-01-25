import tkinter as tk


class Window:
    '''
    TODO...
    '''
    def __init__(self,
                 title: str,
                 width: str,
                 height: str,
                 is_resizable: bool,
                 icon_path: str,
                 background_color: str):

        self.window = tk.Tk()
        self.window.title(f'{title}')
        self.window.geometry(f'{width}x{height}')
        self.window.resizable(is_resizable, is_resizable)
        self.window.configure(bg=f'{background_color}')

        icon_photo = tk.PhotoImage(file=f'{icon_path}')
        self.window.iconphoto(False, icon_photo)

        # calculator = ...

    def run(self):
        '''
        TODO...
        '''
        self.window.mainloop()
