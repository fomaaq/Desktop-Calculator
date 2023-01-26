'''
The module contains classes and methods for working with the window
'''

import tkinter as tk


class Window:
    '''
    The class is used to configure and create a window
    '''
    def __init__(self,
                 title: str,
                 width: str,
                 height: str,
                 is_resizable: bool,
                 icon_path: str,
                 background_color: str):

        # Configuration of window parameters
        self.window = tk.Tk()
        self.window.title(f'{title}')
        self.window.geometry(f'{width}x{height}')
        self.window.resizable(is_resizable, is_resizable)
        self.window.configure(bg=f'{background_color}')

        # Configuring the window icon
        icon_photo = tk.PhotoImage(file=f'{icon_path}')
        self.window.iconphoto(False, icon_photo)

    def run(self):
        '''
        Launches the window and application
        '''
        self.window.mainloop()
