# Written by Oliver Mardle 2017
from tkinter import *
from tkinter import ttk
import random

Numbers = []
Score = 0

def Exit():
    win2.destroy()
    sys.exit()

def ShowScore():
    L1.configure(text = 'Your Score:')
    L2.configure(text = 'Score ' + str(Score))
    L3.configure(text = 'Percentage ' + str((100 / 10) * Score) + '%')
    L4.destroy()
    E1.destroy()
    E2.destroy()
    B1.configure(text = 'Close', command = Exit)
    print(Score)

def GetNumber():
    Number = random.randint(0, 255)
    Numbers.append(Number)

def UpdateGUI(win2, Numbers):
    L2.configure(text = 'The Number to convert is: ' + str(Numbers[len(Numbers) - 1]))
    print(Score)
    print('Length', len(Numbers))
    if len(Numbers) == 11:
        ShowScore()

def CheckAnswer(win2, Numbers):
    global Score
    print(Numbers[len(Numbers) - 1])
    print(E1.get())
    if len(Numbers) <= 10:
        if int(E1.get(), 2) == (Numbers[len(Numbers) - 1]) and (int(E2.get(), 16) == (Numbers[len(Numbers) - 1])):
            print('Correct')
            Score += 1
            GetNumber()
            UpdateGUI(win2, Numbers)
        else:
            Score += 0
            GetNumber()
            UpdateGUI(win2, Numbers)
    else:
        print('Done')

win2 = Tk()
win2.title('Data Representation')
win2.geometry('{}x{}'.format(404, 160))
win2.resizable = (False)

Var1 = IntVar(win2, value = 0)
Var2 = IntVar(win2, value = 0)
Var3 = IntVar(win2, value = 0)
Var4 = IntVar(win2, value = 0)
Var5 = IntVar(win2, value = 0)
Var6 = IntVar(win2, value = 0)
Var7 = IntVar(win2, value = 0)
Var8 = IntVar(win2, value = 0)

GetNumber()
Number = Numbers[len(Numbers) - 1]

F1 = ttk.Frame(win2)
F1.place(anchor = 'c', relx = 0.5, rely = 0.5)

L1 = ttk.Label(F1, text = 'Convert the following number from Decimal to Hex and Binary.')
L2 = ttk.Label(F1, text = 'The Number to convert is: ' + str(Number))
L3 = ttk.Label(F1, text = 'Binary')
L4 = ttk.Label(F1, text = 'Hexidecimal')
L5 = ttk.Label(F1, text = '128')
L6 = ttk.Label(F1, text = '64')
L7 = ttk.Label(F1, text = '32')
L8 = ttk.Label(F1, text = '16')
L9 = ttk.Label(F1, text = '8')
L10 = ttk.Label(F1, text = '4')
L11 = ttk.Label(F1, text = '2')
L12 = ttk.Label(F1, text = '1')
R1 = ttk.Checkbutton(F1, variable = Var1)
R2 = ttk.Checkbutton(F1, variable = Var2)
R3 = ttk.Checkbutton(F1, variable = Var3)
R4 = ttk.Checkbutton(F1, variable = Var4)
R5 = ttk.Checkbutton(F1, variable = Var5)
R6 = ttk.Checkbutton(F1, variable = Var6)
R7 = ttk.Checkbutton(F1, variable = Var7)
R8 = ttk.Checkbutton(F1, variable = Var8)
E1 = ttk.Entry(F1)
E2 = ttk.Entry(F1)
B1 = ttk.Button(F1, text = 'Submit', command = lambda: CheckAnswer(win2, Numbers))

L1.grid(row = 1, column = 1, columnspan = 8)
L2.grid(row = 2, column = 1, columnspan = 8)
L3.grid(row = 3, column = 1, columnspan = 4)
L4.grid(row = 4, column = 1, columnspan = 4)
L5.grid(row = 5, column = 1)
L6.grid(row = 5, column = 2)
L7.grid(row = 5, column = 3)
L8.grid(row = 5, column = 4)
L9.grid(row = 5, column = 5)
L10.grid(row = 5, column = 6)
L11.grid(row = 5, column = 7)
L12.grid(row = 5, column = 8)
R1.grid(row = 6, column = 1)
R2.grid(row = 6, column = 2)
R3.grid(row = 6, column = 3)
R4.grid(row = 6, column = 4)
R5.grid(row = 6, column = 5)
R6.grid(row = 6, column = 6)
R7.grid(row = 6, column = 7)
R8.grid(row = 6, column = 8)
E1.grid(row = 3, column = 5, columnspan = 4)
E2.grid(row = 4, column = 5, columnspan = 4)
B1.grid(row = 7, column = 1, columnspan = 8)

win2.mainloop()
