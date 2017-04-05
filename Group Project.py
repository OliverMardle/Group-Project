# Developed buy Oliver M
# Edited by Dawid S
from tkinter import *
from tkinter import ttk

window = Tk()
window.resizable(width=False, height=False)
window.title('Logic Gates Of Woe')

F1 = Frame(window)
F1.pack(fill = BOTH)
NB = ttk.Notebook(F1)
T1 = ttk.Frame(NB)
T2 = ttk.Frame(NB)
T3 = ttk.Frame(NB)
T4 = ttk.Frame(NB)
T5 = ttk.Frame(NB)
T6 = ttk.Frame(NB)
T7 = ttk.Frame(NB)

# AND TAB

ANDVar1 = IntVar(value = 0)
ANDVar2 = IntVar(value = 0)
ANDVar3 = IntVar(value = 0)
ANDVar4 = IntVar(value = 0)

Photo = PhotoImage(file = 'AND.gif')

def AND(window):
    CheckVar5 = IntVar(value = 0)
    CheckVar6 = IntVar(value = 0)
    L1.destroy()
    L2.destroy()
    L3.destroy()
    L4.destroy()
    L5.destroy()
    L6.destroy()
    L7.destroy()
    L8.destroy()
    R1.destroy()
    R2.destroy()
    R3.destroy()
    R4.destroy()
    B1.destroy()
    Q1 = ttk.Checkbutton(T1, variable = CheckVar5)
    Q2 = ttk.Checkbutton(T1, variable = CheckVar6)
    S1 = ttk.Label(T1)
    Q1.grid(column = 1, row = 1, rowspan = 2)
    Q2.grid(column = 1, row = 3, rowspan = 2)
    S1.grid(column = 5, row = 1, rowspan = 4)
    window.update()
    while True:
        if CheckVar5.get() == 1 and CheckVar6.get() == 1:
            S1.configure(text = '1')
        else:
            S1.configure(text = '0')
        window.update()

L1 = ttk.Label(T1, text = '1')
L1.grid(row = 1, column = 1, padx = 10)
L2 = ttk.Label(T1, text = '1')
L2.grid(row = 1, column = 2, padx = 10)
R1 = ttk.Checkbutton(T1, variable = ANDVar1)
R1.grid(row = 1, column = 3)
L3 = ttk.Label(T1, text = '1')
L3.grid(row = 2, column = 1, padx = 10)
L4 = ttk.Label(T1, text = '0')
L4.grid(row = 2, column = 2, padx = 10)
R2 = ttk.Checkbutton(T1, variable = ANDVar2)
R2.grid(row = 2, column = 3)
L5 = ttk.Label(T1, text = '0')
L5.grid(row = 3, column = 1, padx = 10)
L6 = ttk.Label(T1, text = '1')
L6.grid(row = 3, column = 2, padx = 10)
R3 = ttk.Checkbutton(T1, variable = ANDVar3)
R3.grid(row = 3, column = 3)
L7 = ttk.Label(T1, text = '1')
L7.grid(row = 4, column = 1, padx = 10)
L8 = ttk.Label(T1, text = '1')
L8.grid(row = 4, column = 2, padx = 10)
R4 = ttk.Checkbutton(T1, variable = ANDVar4)
R4.grid(row = 4, column = 3)
B1 = ttk.Button(T1, text = 'Submit', command = lambda: AND(window))
B1.grid(row = 1, column = 5, rowspan = 4)
P1 = Label(T1, image = Photo)
P1.grid(row = 1, column = 4, rowspan = 4)
# AND TAB

NB.add(T1, text = 'AND')
NB.add(T2, text = 'NAND')
NB.add(T3, text = 'NOR')
NB.add(T4, text = 'NOT')
NB.add(T5, text = 'OR')
NB.add(T6, text = 'XNOR')
NB.add(T7, text = 'XOR')
NB.pack(fill = BOTH)

window.mainloop()
