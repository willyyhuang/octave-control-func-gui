from tkinter import *
from oct2py import octave

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        
root = Tk()
app = Window(root)

def submitCallback(_a, _b, _c):
    if _a is None:
        _a = 0
    if _b is None:
        _b = 0
    if _c is None:
        _c = 0

    print('Plotting y = ' + str(_a) + 'x^2 + ' + str(_b) + 'x + ' + str(_c))
    out = octave.polynomialPlot(float(_a), float(_b), float(_c))
    print(out)

# set window title
root.wm_title('SOEN 385 Project')

Label(root, text='Plot y = ax^2 + bx + c').grid(row=0, columnspan=2)

Label(root, text='a').grid(row=1)
Label(root, text='b').grid(row=2)
Label(root, text='c').grid(row=3)

a = Entry(root)
a.grid(row=1, column=1)
b = Entry(root)
b.grid(row=2, column=1)
c = Entry(root)
c.grid(row=3, column=1)


Button(root, text='Plot', command=lambda: submitCallback(a.get(), b.get(), c.get())).grid(row=4, columnspan=2)

# show window
root.mainloop()