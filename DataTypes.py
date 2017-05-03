# Written by Oliver Mardle 2017
from tkinter import *
from tkinter import ttk
import random

Score = 0
Set1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
Set2 = ['Series 1', 'Land Rover', 'Crank Shaft', 'Cam Shaft', 'Head Gasket', 'Brake Master Cylinder', 'Exhaust Manifold', 'Starter Motor', 'Radiator', 'Catalytic Converter']
Set3 = ['True', 'False']
Set4 = ['1.23','34.321','12.32','357.23213','213.98','99.99','636.234','76.345','25.23','345.234']
Set1I = []
Set2I = []
Set3I = []
Set4I = []
Lists = [Set1I, Set2I, Set3I, Set4I]
DATA = []
Set = []

def Close3(win3):
    win3.destroy()
    root.deiconify()

def ShowScore3(win3, F1, L1, L2, R1, R2, R3, R4, B1):
    R1.destroy()
    R2.destroy()
    R3.destroy()
    R4.destroy()
    L1.configure(text = 'Score: ' + str(Score))
    L2.configure(text = 'Percentage: ' + str(100 / 10 * Score) + '%')
    B1.configure(text = 'Quit', command = lambda: Close3(win3))
    
def CheckData3(x, y):
    for i in range(0, len(Lists[x - 1])):
        if y == Lists[x - 1][i]:
            return True

def GetDATA():
    Number1 = random.randint(1, 4)
    Number2 = random.randint(1, 9)
    Number3 = random.randint(0, 1)
    if Number1 == 1:
        Data = Set1[Number2]
        ErrorOccured = CheckData3(Number1, Number2)
        if ErrorOccured == True:
            return True
        else:
            Set1I.append(Number2)
            Set.append(1)
    if Number1 == 2:
        Data = Set2[Number2]
        ErrorOccured = CheckData3(Number1, Number2)
        if ErrorOccured == True:
            return True
        else:
            Set2I.append(Number2)
            Set.append(2)
    if Number1 == 3:
        Data = Set3[Number3]
        ErrorOccured = CheckData3(Number1, Number3)
        if ErrorOccured == True:
            return True
        else:
            Set3I.append(Number3)
            Set.append(3)
    if Number1 == 4:
        Data = Set4[Number2]
        ErrorOccured = CheckData3(Number1, Number2)
        if ErrorOccured == True:
            return True
        else:
            Set4I.append(Number2)
            Set.append(4)
    print(Data)
    print(Set1I, Set2I, Set3I, Set4I)
    DATA.append(Data)

def CheckAns3(win3, F1, L1, L2, R1, R2, R3, R4, B1, State):
    global Score
    print(State.get())
    if Set[len(Set) - 1] == 1 and State.get() == '1':
        print('Huzzah, Correct')
        Score += 1
    elif Set[len(Set) - 1] == 2 and State.get() == '2':
        print('Huzzah, Correct')
        Score += 1
    elif Set[len(Set) - 1] == 3 and State.get() == '3':
        print('Huzzah, Correct')
        Score += 1
    elif Set[len(Set) - 1] == 4 and State.get() == '4':
        print('Huzzah, Correct')
        Score += 1
    else:
        print('No.')
    if len(DATA) < 10:
        X = True
        while X == True:
            ReRun = GetDATA()
            if ReRun == True:
                ReRun = GetDATA()
                X = True
            if ReRun != True:
                X = False
        L2.configure(text = str(DATA[len(DATA) - 1]))
    else:
        ShowScore3(win3, F1, L1, L2, R1, R2, R3, R4, B1)
    print(Score)

def DrawGUI3():
    win3 = Tk()
    win3.title('Data Types')
    GetDATA()
    State = StringVar(win3)
    F1 = ttk.Frame(win3)
    F1.pack()
    L1 = ttk.Label(F1, text = 'Check the correct data type:')
    L2 = ttk.Label(F1, text = str(DATA[len(DATA) - 1]))
    R1 = ttk.Radiobutton(F1, text = 'Integer', variable = State, value = 1)
    R2 = ttk.Radiobutton(F1, text = 'String', variable = State, value = 2)
    R3 = ttk.Radiobutton(F1, text = 'Boolean', variable = State, value = 3)
    R4 = ttk.Radiobutton(F1, text = 'Float', variable = State, value = 4)
    B1 = ttk.Button(F1, text = 'Submit', command = lambda: CheckAns3(win3, F1, L1, L2, R1, R2, R3, R4, B1, State))
    L1.grid(row = 1, column = 1, columnspan = 2, padx = 10, pady = 10)
    L2.grid(row = 2, column = 1, columnspan = 2, padx = 10)
    R1.grid(row = 3, column = 1, sticky = 'w', padx = 10)
    R2.grid(row = 4, column = 1, sticky = 'w', padx = 10)
    R3.grid(row = 5, column = 1, sticky = 'w', padx = 10)
    R4.grid(row = 6, column = 1, sticky = 'w', padx = 10)
    B1.grid(row = 7, column = 1, columnspan = 2, padx = 10, pady = 10)
    win3.mainloop()

DrawGUI3()
