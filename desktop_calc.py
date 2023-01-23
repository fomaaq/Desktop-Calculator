from tkinter import *


window = Tk()
window.title('Desktop calculator')
window.geometry('300x400')
window.mainloop()

btn = Button(window, text="+")
btn.grid(column=0, row=0)

btn = Button(window, text="-")
btn.grid(column=1, row=0)
