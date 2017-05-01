# Written by Oliver Mardle 2017
from tkinter import *
from tkinter import ttk
import random

Numbers = []
Score = 0

def Exit(win):
    win.destroy()
    root.deiconify()

def ShowScore(win, L1, L2, L3, L4, E1, E2, B1):
    L1.configure(text = 'Your Score:')
    L2.configure(text = 'Score ' + str(Score))
    L3.configure(text = 'Percentage ' + str((100 / 10) * Score) + '%')
    L4.destroy()
    E1.destroy()
    E2.destroy()
    B1.configure(text = 'Close', command = lambda: Exit(win))
    print(Score)

def GetNumber():
    Number = random.randint(0, 255)
    Numbers.append(Number)
    print(bin(Number))
    print(hex(Number))

def UpdateGUI(win, Numbers, L1, L2, L3, L4, E1, E2, B1):
    L2.configure(text = 'The Number to convert is: ' + str(Numbers[len(Numbers) - 1]))
    print(Score)
    print('Length', len(Numbers))
    if len(Numbers) == 11:
        ShowScore(win, L1, L2, L3, L4, E1, E2, B1)

def CheckAnswer(win, Numbers, L1, L2, L3, L4, E1, E2, B1):
    global Score
    print(Numbers[len(Numbers) - 1])
    print(E1.get())
    if len(Numbers) <= 10:
        if int(E1.get(), 2) == (Numbers[len(Numbers) - 1]) and (int(E2.get(), 16) == (Numbers[len(Numbers) - 1])):
            print('Correct')
            Score += 1
            GetNumber()
            UpdateGUI(win, Numbers, L1, L2, L3, L4, E1, E2, B1)
        else:
            Score += 0
            GetNumber()
            UpdateGUI(win, Numbers, L1, L2, L3, L4, E1, E2, B1)
    else:
        print('Done')
        
def DrawGUI(Numbers, Score):
    root.withdraw()
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
    B1 = ttk.Button(F1, text = 'Submit', command = lambda: CheckAnswer(win, Numbers, L1, L2, L3, L4, E1, E2, B1))

    L1.grid(row = 1, column = 1, columnspan = 2)
    L2.grid(row = 2, column = 1, columnspan = 2)
    L3.grid(row = 3, column = 1)
    L4.grid(row = 4, column = 1)
    E1.grid(row = 3, column = 2)
    E2.grid(row = 4, column = 2)
    B1.grid(row = 5, column = 1, columnspan = 2)

    win.mainloop()

root = Tk()
root.title('Year 11 Computing Revision Tools')

RootFrame = ttk.Frame(root)
RootFrame.pack()
    
L1 = ttk.Label(RootFrame, text = 'Welcome to the Year 11 GCSE Computing Revision Tool Kit.\nTo proceed, Click on one of the subjects below:\nOr to exit press \'Exit\'')
L1.grid(row = 1, column = 1, columnspan = 2, pady = 10)
B1 = ttk.Button(RootFrame, text = 'Logic Gates', width = 20).grid(row = 2, column = 1)
B2 = ttk.Button(RootFrame, text = 'Data Representation', command = lambda: DrawGUI(Numbers, Score), width = 20).grid(row = 2, column = 2)
B3 = ttk.Button(RootFrame, text = 'System Architecture', width = 20).grid(row = 3, column = 1)
B4 = ttk.Button(RootFrame, text = 'Networks', width = 20).grid(row = 3, column = 2)
B5 = ttk.Button(RootFrame, text = 'Character Encoding', width = 20).grid(row = 4, column = 1)
B6 = ttk.Button(RootFrame, text = 'Software Dev Lifecycle', width = 20).grid(row = 4, column = 2)
B7 = ttk.Button(RootFrame, text = 'Data Types', width = 20).grid(row = 5, column = 1)
B8 = ttk.Button(RootFrame, text = 'Data Structures', width = 20).grid(row = 5, column = 2)
B9 = ttk.Button(RootFrame, text = 'Exit', command = lambda: root.destroy(), width = 20).grid(row = 6, column = 1, columnspan = 2, pady = 10)

root.mainloop()
