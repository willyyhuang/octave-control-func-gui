from tkinter import *
from oct2py import Oct2Py
import os

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

oc = Oct2Py()
root = Tk()
app = Window(root)
def submitCallback(_J, _b, _Ke, _Kt):
    # if parameters are not inputted, set default parameters
    if _J == '':
        _J = 1.3
    if _b == '':
        _b = 1.75
    if _Ke == '':
        _Ke = 1.6
    if _Kt == '':
        _Kt = 1.9
    J = float(_J)
    b = float(_b)
    Ke = float(_Ke)
    Kt = float(_Kt)
    out = oc.tfPlot(J, b, Ke, Kt)
    print(out)

# set window title
root.wm_title('SOEN 385 Project')

Label(root, text='Change the parameters of the system').grid(row=0, columnspan=2)

Label(root, text='J = Moment of Inertia of rotor (between 1.00 to 1.50)').grid(row=1)
Label(root, text='b = Motor Viscous Friction Constant (between 1.50 and 2.00)').grid(row=2)
Label(root, text='Ke = Electromotive Force Constant (between 1.50 and 2.00)').grid(row=3)
Label(root, text='Kt = Motor Torque Constant (between 1.50 and 2.00)').grid(row=4)
Label(root, text='R = Armature Resistance (0,06727)').grid(row=5)
Label(root, text='L = Armature Inductance (0.001882)').grid(row=6)

J = Entry(root)
J.grid(row=1, column=1)
b = Entry(root)
b.grid(row=2, column=1)
Ke = Entry(root)
Ke.grid(row=3, column=1)
Kt = Entry(root)
Kt.grid(row=4, column=1)

Button(root, text='Plot', command=lambda: submitCallback(J.get(), b.get(), Ke.get(), Kt.get())).grid(row=7, columnspan=2)

# show window
root.mainloop()