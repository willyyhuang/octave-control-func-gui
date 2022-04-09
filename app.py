from tkinter import *
from oct2py import octave

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        
root = Tk()
app = Window(root)

def submitCallback(_J, _b, _Ke, _Kt):
    if _J is None:
        _J = 1
    if _b is None:
        _b = 1.5
    if _Ke is None:
        _Ke = 1.5
    if _Kt is None:
        _Kt = 1.5

    print('Plotting')
    out = octave.tfPlot(float(_J), float(_b), float(_Ke), float(_Kt))
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