# Written by Oliver Mardle 2017
from tkinter import *
from tkinter import ttk
import time

Characters = ['a']

def UpdateGUI4(L9, win4, Var1, Var2, Var3, Var4, Var5, Var6, Var7):
        Vars = [Var1, Var2, Var3, Var4, Var5, Var6, Var7]
        BinString = '0b'
        for i in range(0, len(Vars)):
            BinString = BinString + str(Vars[i].get())
        Letter = int(BinString, 2)
        L9.configure(text = chr(Letter))
        win4.update()

def DrawGUI4():
        win4 = Tk()
        win4.title('Character Encoding')

        Var1 = IntVar(win4, value = 0)
        Var2 = IntVar(win4, value = 0)
        Var3 = IntVar(win4, value = 0)
        Var4 = IntVar(win4, value = 0)
        Var5 = IntVar(win4, value = 0)
        Var6 = IntVar(win4, value = 0)
        Var7 = IntVar(win4, value = 0)

        F1 = ttk.Frame(win4)
        F1.pack()
        L1 = ttk.Label(F1, text = 'Convert this Character to ASCII: ' + Characters[len(Characters) - 1])
        L2 = ttk.Label(F1, text = '64')
        L3 = ttk.Label(F1, text = '32')
        L4 = ttk.Label(F1, text = '16')
        L5 = ttk.Label(F1, text = '8')
        L6 = ttk.Label(F1, text = '4')
        L7 = ttk.Label(F1, text = '2')
        L8 = ttk.Label(F1, text = '1')
        L9 = ttk.Label(F1, text = '...')
        R1 = ttk.Checkbutton(F1, variable = Var1, command = lambda: UpdateGUI4(L9, win4, Var1, Var2, Var3, Var4, Var5, Var6, Var7))
        R2 = ttk.Checkbutton(F1, variable = Var2, command = lambda: UpdateGUI4(L9, win4, Var1, Var2, Var3, Var4, Var5, Var6, Var7))
        R3 = ttk.Checkbutton(F1, variable = Var3, command = lambda: UpdateGUI4(L9, win4, Var1, Var2, Var3, Var4, Var5, Var6, Var7))
        R4 = ttk.Checkbutton(F1, variable = Var4, command = lambda: UpdateGUI4(L9, win4, Var1, Var2, Var3, Var4, Var5, Var6, Var7))
        R5 = ttk.Checkbutton(F1, variable = Var5, command = lambda: UpdateGUI4(L9, win4, Var1, Var2, Var3, Var4, Var5, Var6, Var7))
        R6 = ttk.Checkbutton(F1, variable = Var6, command = lambda: UpdateGUI4(L9, win4, Var1, Var2, Var3, Var4, Var5, Var6, Var7))
        R7 = ttk.Checkbutton(F1, variable = Var7, command = lambda: UpdateGUI4(L9, win4, Var1, Var2, Var3, Var4, Var5, Var6, Var7))
        B1 = ttk.Button(F1, text = 'Submit')

        L1.grid(row = 1, column = 1, columnspan = 8, padx = 10)
        L2.grid(row = 2, column = 1)
        L3.grid(row = 2, column = 2)
        L4.grid(row = 2, column = 3)
        L5.grid(row = 2, column = 4)
        L6.grid(row = 2, column = 5)
        L7.grid(row = 2, column = 6)
        L8.grid(row = 2, column = 7)
        L9.grid(row = 3, column = 8)
        R1.grid(row = 3, column = 1)
        R2.grid(row = 3, column = 2)
        R3.grid(row = 3, column = 3)
        R4.grid(row = 3, column = 4)
        R5.grid(row = 3, column = 5)
        R6.grid(row = 3, column = 6)
        R7.grid(row = 3, column = 7)
        B1.grid(row = 4, column = 1, columnspan = 8)

        win4.mainloop()

DrawGUI4()
