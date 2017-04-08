# Developed By Oliver M
# Edited By Dawid S
from tkinter import *
from tkinter import ttk
import random

window = Tk()
window.resizable(width=False, height=False)
window.title('Logic Gates Of Woe')

Count = 7
Tabs = ['AND','NAND','NOR','NOT','OR','XNOR','XOR']
Images = ['AND.gif','NAND.gif','NOR.gif','NOT.gif','OR.gif','XNOR.gif','XOR.gif']
Names = []

F1 = Frame(window)
F1.pack(fill = BOTH)
NB = ttk.Notebook(F1)

ANDVar1 = IntVar(value = 0)
ANDVar2 = IntVar(value = 0)
ANDVar3 = IntVar(value = 0)
ANDVar4 = IntVar(value = 0)
ANDVar5 = IntVar(value = 0)
ANDVar6 = IntVar(value = 0)

def CreateGUI(Count):
        for i in range(0, Count):
                Names.append('T' + str(i + 1))
        for i in range(0, Count):
                Names[i] = ttk.Frame(window)
                NB.add(Names[i], text = Tabs[i])

                Photo = PhotoImage(file = Images[i])
                
                L1 = ttk.Label(Names[i], text = '1')
                L1.grid(row = 1, column = 1, padx = 10)
                L2 = ttk.Label(Names[i], text = '1')
                L2.grid(row = 1, column = 2, padx = 10)
                R1 = ttk.Checkbutton(Names[i], variable = ANDVar1)
                R1.grid(row = 1, column = 3)
                L3 = ttk.Label(Names[i], text = '1')
                L3.grid(row = 2, column = 1, padx = 10)
                L4 = ttk.Label(Names[i], text = '0')
                L4.grid(row = 2, column = 2, padx = 10)
                R2 = ttk.Checkbutton(Names[i], variable = ANDVar2)
                R2.grid(row = 2, column = 3)
                L5 = ttk.Label(Names[i], text = '0')
                L5.grid(row = 3, column = 1, padx = 10)
                L6 = ttk.Label(Names[i], text = '1')
                L6.grid(row = 3, column = 2, padx = 10)
                R3 = ttk.Checkbutton(Names[i], variable = ANDVar3)
                R3.grid(row = 3, column = 3)
                L7 = ttk.Label(Names[i], text = '1')
                L7.grid(row = 4, column = 1, padx = 10)
                L8 = ttk.Label(Names[i], text = '1')
                L8.grid(row = 4, column = 2, padx = 10)
                R4 = ttk.Checkbutton(Names[i], variable = ANDVar4)
                R4.grid(row = 4, column = 3)
                B1 = ttk.Button(Names[i], text = 'Submit')
                B1.grid(row = 1, column = 5, rowspan = 4)
                P1 = Label(Names[i], image = Photo)
                P1.image = Photo
                P1.grid(row = 5, column = 2, rowspan = 4, columnspan = 4)
                R5 = ttk.Checkbutton(Names[i], variable = ANDVar5)
                R5.grid(row = 5, column = 1, rowspan = 2)
                R6 = ttk.Checkbutton(Names[i], variable = ANDVar6)
                R6.grid(row = 7, column = 1, rowspan = 2)
                L9 = ttk.Label(Names[i], text = '0')
                L9.grid(row = 5, column = 7, rowspan = 4)
                
        NB.pack(fill = BOTH)

CreateGUI(Count)

window.mainloop()
