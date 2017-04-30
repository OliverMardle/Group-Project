# Written by Oliver Mardle 2017
from tkinter import *
from tkinter import ttk
import random

Numbers = []
Score = 0

def Exit():
    win.destroy()
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
    print(bin(Number))
    print(hex(Number))

def UpdateGUI(win, Numbers):
    L2.configure(text = 'The Number to convert is: ' + str(Numbers[len(Numbers) - 1]))
    print(Score)
    print('Length', len(Numbers))
    if len(Numbers) == 11:
        ShowScore()

def CheckAnswer(win, Numbers):
    global Score
    print(Numbers[len(Numbers) - 1])
    print(E1.get())
    if len(Numbers) <= 10:
        if int(E1.get(), 2) == (Numbers[len(Numbers) - 1]) and (int(E2.get(), 16) == (Numbers[len(Numbers) - 1])):
            print('Correct')
            Score += 1
            GetNumber()
            UpdateGUI(win, Numbers)
        else:
            Score += 0
            GetNumber()
            UpdateGUI(win, Numbers)
    else:
        print('Done')

win = Tk()
win.title('Data Representation')
win.geometry('{}x{}'.format(404, 116))
win.resizable = (False)

GetNumber()
Number = Numbers[len(Numbers) - 1]

F1 = ttk.Frame(win)
F1.place(anchor = 'c', relx = 0.5, rely = 0.5)

L1 = ttk.Label(F1, text = 'Convert the following number from Decimal to Hex and Binary.')
L2 = ttk.Label(F1, text = 'The Number to convert is: ' + str(Number))
L3 = ttk.Label(F1, text = 'Binary')
L4 = ttk.Label(F1, text = 'Hexidecimal')
E1 = ttk.Entry(F1)
E2 = ttk.Entry(F1)
B1 = ttk.Button(F1, text = 'Submit', command = lambda: CheckAnswer(win, Numbers))

L1.grid(row = 1, column = 1, columnspan = 2)
L2.grid(row = 2, column = 1, columnspan = 2)
L3.grid(row = 3, column = 1)
L4.grid(row = 4, column = 1)
E1.grid(row = 3, column = 2)
E2.grid(row = 4, column = 2)
B1.grid(row = 5, column = 1, columnspan = 2)

win.mainloop()
