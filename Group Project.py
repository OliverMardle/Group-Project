# Developed By Oliver M
# Edited By Dawid S
from tkinter import *
from tkinter import ttk
import random

window = Tk()
window.resizable(width=False, height=False)
window.title('Logic Of Woe')

Count = 7
Tabs = ['AND','NAND','NOR','NOT','OR','XNOR','XOR']
Images = ['AND.gif','NAND.gif','NOR.gif','NOT.gif','OR.gif','XNOR.gif','XOR.gif']
Names = []

F1 = Frame(window)
F1.pack(fill = BOTH)
NB = ttk.Notebook(F1)

Var1 = IntVar(value = 0)
Var2 = IntVar(value = 0)
Var3 = IntVar(value = 0)
Var4 = IntVar(value = 0)
Var5 = IntVar(value = 0)
Var6 = IntVar(value = 0)

Variables = [Var1, Var2, Var3, Var4, Var5, Var6]

def Check(window):
        print(NB.index(NB.select()))
        for i in range(0, 6):
                print(i, Variables[i].get())
                Variables[i].set(0)
        NB.tab(NB.index(NB.select()), state = 'disabled')
        NB.select(Names[NB.index(NB.select())])
        
def CreateGUI(Count):
        for i in range(0, Count):
                Names.append('T' + str(i + 1))
        for i in range(0, Count):
                Names[i] = ttk.Frame(window)
                NB.add(Names[i], text = Tabs[i])

                Photo = PhotoImage(file = Images[i])
                
                R1 = ttk.Checkbutton(Names[i], variable = Var1)
                R2 = ttk.Checkbutton(Names[i], variable = Var2)
                P1 = ttk.Label(Names[i], image = Photo)
                P1.image = Photo
                L1 = ttk.Label(Names[i], text = '0')
                F2 = ttk.Frame(Names[i])
                L2 = ttk.Label(F2, text = '1  |  1  |')
                L3 = ttk.Label(F2, text = '1  |  0  |')
                L4 = ttk.Label(F2, text = '0  |  1  |')
                L5 = ttk.Label(F2, text = '0  |  0  |')
                R3 = ttk.Checkbutton(F2, variable = Var3)
                R4 = ttk.Checkbutton(F2, variable = Var4)
                R5 = ttk.Checkbutton(F2, variable = Var5)
                R6 = ttk.Checkbutton(F2, variable = Var6)
                B1 = ttk.Button(Names[i], text = 'Submit', command = lambda: Check(window))

                R1.grid(row = 1, column = 1, rowspan = 2)
                R2.grid(row = 3, column = 1, rowspan = 2)
                P1.grid(row = 1, column = 2, rowspan = 4, columnspan = 3)
                L1.grid(row = 1, column = 5, rowspan = 4)
                B1.grid(row = 5, column = 3, rowspan = 4, columnspan = 3)
                F2.grid(row = 5, column = 1, columnspan = 2)
                L2.grid(row = 1, column = 1)
                L3.grid(row = 2, column = 1)
                L4.grid(row = 3, column = 1)
                L5.grid(row = 4, column = 1)
                R3.grid(row = 1, column = 2)
                R4.grid(row = 2, column = 2)
                R5.grid(row = 3, column = 2)
                R6.grid(row = 4, column = 2)
                
        NB.pack(fill = BOTH)
        while True:
                x = NB.index(NB.select())
                if x == 0:
                        print(Var1.get(), Var2.get())
                        if Var1.get() == 1 and Var2.get() == 1:
                                L1.configure(text = '1')
                        else:
                                L1.configure(text = '0')
                        window.update()
                window.update()
CreateGUI(Count)

window.mainloop()
