# Written by Oliver Mardle 2017
from tkinter import *
from tkinter import ttk
import random

# Score Variables
Score1 = 0
Score2 = 0
Score3 = 0
# Variables for Logic Gates
Count = 7
Tabs = ['AND','NAND','NOR','NOT','OR','XNOR','XOR']
Images = ['AND.gif','NAND.gif','NOR.gif','NOT.gif','OR.gif','XNOR.gif','XOR.gif']
Labels = []
Names = []
# Variables for Data Representation
Numbers = []
# Variables for Data Types
Set1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
Set2 = ['\'MotherBoard\'', '\'CPU\'', '\'RAM\'', '\'Graphics Card\'', '\'Power Supply\'', '\'Network Interface Card\'', '\'Dial Up Modem\'', '\'CPU Cooler\'', '\'Hard Disk Drive\'', '\'Solid State Drive\'']
Set3 = ['True', 'False']
Set4 = ['1.23','34.321','12.32','357.23213','213.98','99.99','636.234','76.345','25.23','345.234']
Set1I = []
Set2I = []
Set3I = []
Set4I = []
Lists = [Set1I, Set2I, Set3I, Set4I]
DATA = []
Set = []

# Code for Logic Gates
def Close1(win1):
        win1.destroy()
        root.deiconify()

def Check1(Variables, Variables2, S1, NB, win1, F8, Var1, Var2, Var3, Var4, Var5, Var6):
        global Score1
        Tab = NB.index(NB.select())
        File = open(str(Tab) + '.txt', 'r')
        Text = File.readlines()
        Answers = []
        for line in Text:
                line = line.strip('\n')
                Answers.append(line)
        for i in range(0, len(Answers)):
                if int(Answers[i]) == Variables2[i].get():
                        Score1 += 1
                elif int(Answers[i]) != Variables2[i].get():
                        Score1 += 0
                S1.configure(text = 'Score: ' + str(Score1))
        for i in range(0, 6):
                Variables[i].set(0)
        if Tab != Count - 1:
                NB.tab(NB.index(NB.select()) + 1, state = 'normal')
                NB.tab(NB.index(NB.select()), state = 'disabled')
                NB.select(Names[NB.index(NB.select())])
        else:
                NB.tab(7, state = 'normal')
                NB.tab(NB.index(NB.select()), state = 'disabled')
                S2 = ttk.Label(F8, text = 'Total Score: ' + str(Score1))
                S3 = ttk.Label(F8, text = 'Percentage: '+ str((100 / 26) * Score1) + '%')
                B1 = ttk.Button(F8, text = 'Close', command = lambda: Close1(win1))
                S2.pack(padx = 10, pady = 10)
                S3.pack(padx = 10, pady = 10)
                B1.pack(padx = 10, pady = 10)
                NB.select(NB.index(NB.select()))
        win1.update()

def Tab1(win1, x, Var1, Var2, Var3, Var4, Var5, Var6):
        if Var1.get() == 1 and Var2.get() == 1:
                Labels[x].configure(text = '1')
        else:
                Labels[x].configure(text = '0')
        win1.update()
        
def Tab2(win1, x, Var1, Var2, Var3, Var4, Var5, Var6):
        if Var1.get() == 1 and Var2.get() == 1:
                Labels[x].configure(text = '0')
        else:
                Labels[x].configure(text = '1')
        win1.update()
        
def Tab3(win1, x, Var1, Var2, Var3, Var4, Var5, Var6):
        if Var1.get() == 0 and Var2.get() == 0:
                Labels[x].configure(text = '1')
        else:
                Labels[x].configure(text = '0')
        win1.update()
                        
def Tab4(win1, x, Var1, Var2, Var3, Var4, Var5, Var6):
        if Var1.get() == 1:
                Labels[x].configure(text = '0')
        else:
                Labels[x].configure(text = '1')
        win1.update()
                        
def Tab5(win1, x, Var1, Var2, Var3, Var4, Var5, Var6):
        if Var1.get() == 0 and Var2.get() == 0:
                Labels[x].configure(text = '0')
        else:
                Labels[x].configure(text = '1')
        win1.update()
                        
def Tab6(win1, x, Var1, Var2, Var3, Var4, Var5, Var6):
        if (Var1.get() == 1 and Var2.get() == 1) or (Var1.get() == 0 and Var2.get() == 0):
                Labels[x].configure(text = '1')
        else:
                Labels[x].configure(text = '0')
        win1.update()
                        
def Tab7(win1, x, Var1, Var2, Var3, Var4, Var5, Var6):
        if (Var1.get() == 1 and Var2.get() == 1) or (Var1.get() == 0 and Var2.get() == 0):
                Labels[x].configure(text = '0')
        else:
                Labels[x].configure(text = '1')
        win1.update()

def Tab8(win1, x, Var1, Var2, Var3, Var4, Var5, Var6):
        win1.update()

TabFunctions = [Tab1, Tab2, Tab3, Tab4, Tab5, Tab6, Tab7, Tab8]

def DrawGUI1(Count):
        root.withdraw()
        global Score1
        Score1 = 0
        win1 = Tk()
        win1.resizable(width=False, height=False)
        win1.title('Logic Gates')
        F1 = Frame(win1)
        F1.pack(fill = BOTH)
        NB = ttk.Notebook(F1)
        S1 = ttk.Label(F1, text = 'Score: ' + str(Score1))

        Var1 = IntVar(win1, value = 0)
        Var2 = IntVar(win1, value = 0)
        Var3 = IntVar(win1, value = 0)
        Var4 = IntVar(win1, value = 0)
        Var5 = IntVar(win1, value = 0)
        Var6 = IntVar(win1, value = 0)

        Variables = [Var1, Var2, Var3, Var4, Var5, Var6]
        Variables2 = [Var3, Var4, Var5, Var6]
        
        for i in range(0, Count):
                Names.append('T' + str(i + 1))
                Labels.append('O' + str(i + 1))
        for i in range(0, Count):
                Names[i] = ttk.Frame(win1)
                NB.add(Names[i], text = Tabs[i])

                Photo = PhotoImage(master = win1, file = Images[i])
                
                R1 = ttk.Checkbutton(Names[i], variable = Var1)
                R2 = ttk.Checkbutton(Names[i], variable = Var2)
                P1 = ttk.Label(Names[i], image = Photo)
                P1.image = Photo
                Labels[i] = ttk.Label(Names[i], text = '0')
                F2 = ttk.Frame(Names[i])
                L2 = ttk.Label(F2, text = '1  |  1  |')
                L3 = ttk.Label(F2, text = '1  |  0  |')
                L4 = ttk.Label(F2, text = '0  |  1  |')
                L5 = ttk.Label(F2, text = '0  |  0  |')
                R3 = ttk.Checkbutton(F2, variable = Var3)
                R4 = ttk.Checkbutton(F2, variable = Var4)
                R5 = ttk.Checkbutton(F2, variable = Var5)
                R6 = ttk.Checkbutton(F2, variable = Var6)
                B1 = ttk.Button(Names[i], text = 'Submit', command = lambda: Check1(Variables, Variables2, S1, NB, win1, F8, Var1, Var2, Var3, Var4, Var5, Var6))

                R1.grid(row = 1, column = 1, rowspan = 2)
                R2.grid(row = 3, column = 1, rowspan = 2)
                P1.grid(row = 1, column = 2, rowspan = 4, columnspan = 3)
                Labels[i].grid(row = 1, column = 5, rowspan = 4)
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
                if i == 3:
                        L2.configure(text = '1  |')
                        L3.configure(text = '0  |')
                        L4.destroy()
                        L5.destroy()
                        R2.destroy()
                        R5.destroy()
                        R6.destroy()
                        R1.grid(rowspan = 4)
                if i > 0:
                        NB.tab(i, state = 'disabled')
                        
        F8 = ttk.Frame(win1)
        NB.add(F8, text = 'Score')
        NB.tab(7, state = 'hidden')
        NB.pack(fill = BOTH)
        S1.pack()
        while True:
                x = NB.index(NB.select())
                TabFunctions[x](win1, x, Var1, Var2, Var3, Var4, Var5, Var6)
                win1.update()
        win1.mainloop()

# Code for Data Representation
def Exit2(win2):
        Score2 = 0
        win2.destroy()
        root.deiconify()

def ShowScore2(win2, L1, L2, L3, L4, L13, E1, E2, B1, L5, L6, L7, L8, L9, L10, L11, L12, R1, R2, R3, R4, R5, R6, R7, R8):
        L1.configure(text = 'Your Score:')
        L2.configure(text = 'Score ' + str(Score2))
        L3.configure(text = 'Percentage ' + str((100 / 10) * Score2) + '%')
        L4.destroy()
        L5.destroy()
        L6.destroy()
        L7.destroy()
        L8.destroy()
        L9.destroy()
        L10.destroy()
        L11.destroy()
        L12.destroy()
        L13.destroy()
        E1.destroy()
        E2.destroy()
        R1.destroy()
        R2.destroy()
        R3.destroy()
        R4.destroy()
        R5.destroy()
        R6.destroy()
        R7.destroy()
        R8.destroy()
        B1.configure(text = 'Close', command = lambda: Exit2(win2))

def GetNumber2():
        Number = random.randint(0, 255)
        Numbers.append(Number)

def UpdateGUI2(win2, Numbers, L1, L2, L3, L4, L13, E1, E2, B1, L5, L6, L7, L8, L9, L10, L11, L12, R1, R2, R3, R4, R5, R6, R7, R8):
        L2.configure(text = 'The Number to convert is: ' + str(Numbers[len(Numbers) - 1]))
        if len(Numbers) == 11:
                ShowScore2(win2, L1, L2, L3, L4, L13, E1, E2, B1, L5, L6, L7, L8, L9, L10, L11, L12, R1, R2, R3, R4, R5, R6, R7, R8)

def CheckAnswer2(win2, Numbers, L1, L2, L3, L4, L13, E1, E2, B1, L5, L6, L7, L8, L9, L10, L11, L12, R1, R2, R3, R4, R5, R6, R7, R8):
        global Score2
        if len(Numbers) <= 10:
                if int(E1.get(), 2) == (Numbers[len(Numbers) - 1]) and (int(E2.get(), 16) == (Numbers[len(Numbers) - 1])):
                        Score2 += 1
                        GetNumber2()
                        UpdateGUI2(win2, Numbers, L1, L2, L3, L4, L13, E1, E2, B1, L5, L6, L7, L8, L9, L10, L11, L12, R1, R2, R3, R4, R5, R6, R7, R8)
                        L13.configure(text = 'Score: ' + str(Score2))
                else:
                        Score2 += 0
                        GetNumber2()
                        UpdateGUI2(win2, Numbers, L1, L2, L3, L4, L13, E1, E2, B1, L5, L6, L7, L8, L9, L10, L11, L12, R1, R2, R3, R4, R5, R6, R7, R8)
                        L13.configure(text = 'Score: ' + str(Score2))
        
def DrawGUI2(Numbers):
        global Score2
        Score2 = 0
        root.withdraw()
        win2 = Tk()
        win2.title('Data Representation')
        win2.geometry('{}x{}'.format(404, 170))
        win2.resizable(width=False, height=False)
        Var1 = IntVar(win2, value = 0)
        Var2 = IntVar(win2, value = 0)
        Var3 = IntVar(win2, value = 0)
        Var4 = IntVar(win2, value = 0)
        Var5 = IntVar(win2, value = 0)
        Var6 = IntVar(win2, value = 0)
        Var7 = IntVar(win2, value = 0)
        Var8 = IntVar(win2, value = 0)
        
        GetNumber2()
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
        L13 = ttk.Label(F1, text = 'Score: ' + str(Score2))
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
        B1 = ttk.Button(F1, text = 'Submit', command = lambda: CheckAnswer2(win2, Numbers, L1, L2, L3, L4, L13, E1, E2, B1, L5, L6, L7, L8, L9, L10, L11, L12, R1, R2, R3, R4, R5, R6, R7, R8))

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
        L13.grid(row = 8, column = 1, columnspan = 8)
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

# Code for Data Types
def Close3(win3):
        Score3 = 0
        win3.destroy()
        root.deiconify()

def ShowScore3(win3, F1, L1, L2, R1, R2, R3, R4, B1):
        R1.destroy()
        R2.destroy()
        R3.destroy()
        R4.destroy()
        L1.configure(text = 'Score: ' + str(Score3))
        L2.configure(text = 'Percentage: ' + str(100 / 10 * Score3) + '%')
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
        DATA.append(Data)

def CheckAns3(win3, F1, L1, L2, R1, R2, R3, R4, B1, State):
        global Score3
        if Set[len(Set) - 1] == 1 and State.get() == '1':
                Score3 += 1
        elif Set[len(Set) - 1] == 2 and State.get() == '2':
                Score3 += 1
        elif Set[len(Set) - 1] == 3 and State.get() == '3':
                Score3 += 1
        elif Set[len(Set) - 1] == 4 and State.get() == '4':
                Score3 += 1
        else:
                Score3 += 0
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

def DrawGUI3():
        global Score3
        Score3 = 0
        root.withdraw()
        win3 = Tk()
        win3.title('Data Types')
        win3.geometry('{}x{}'.format(300, 200))
        win3.resizable(width=False, height=False)
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

# Code for the Main Menu
root = Tk()
root.title('Year 11 Computing Revision Tools')

RootFrame = ttk.Frame(root)
RootFrame.pack()
    
L1 = ttk.Label(RootFrame, text = 'Welcome to the Year 11 GCSE Computing Revision Tool Kit.\nTo proceed, Click on one of the subjects below:\nOr to exit press \'Exit\'')
L1.grid(row = 1, column = 1, columnspan = 2, pady = 10)
B1 = ttk.Button(RootFrame, text = 'Logic Gates', command = lambda: DrawGUI1(Count), width = 20).grid(row = 2, column = 1)
B2 = ttk.Button(RootFrame, text = 'Data Representation', command = lambda: DrawGUI2(Numbers), width = 20).grid(row = 2, column = 2)
B3 = ttk.Button(RootFrame, text = 'Data Types', command = lambda: DrawGUI3(), width = 20).grid(row = 3, column = 1)
#B4 = ttk.Button(RootFrame, text = 'Character Encoding', width = 20).grid(row = 3, column = 2)
#B5 = ttk.Button(RootFrame, text = 'Networks', width = 20).grid(row = 4, column = 1)
#B6 = ttk.Button(RootFrame, text = 'Software Dev Lifecycle', width = 20).grid(row = 4, column = 2)
#B7 = ttk.Button(RootFrame, text = 'System Architecture', width = 20).grid(row = 5, column = 1)
#B8 = ttk.Button(RootFrame, text = 'Data Structures', width = 20).grid(row = 5, column = 2)
B9 = ttk.Button(RootFrame, text = 'Exit', command = lambda: root.destroy(), width = 20).grid(row = 3, column = 2, pady = 10)

root.mainloop()
