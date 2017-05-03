# Written by Oliver Mardle
from tkinter import *
from tkinter import ttk

Count = 7
Score1 = 0
Tabs = ['AND','NAND','NOR','NOT','OR','XNOR','XOR']
Images = ['AND.gif','NAND.gif','NOR.gif','NOT.gif','OR.gif','XNOR.gif','XOR.gif']
Labels = []
Names = []

def Close1(win1):
        win1.destroy()
        sys.exit()

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

def CreateGUI1(Count):
        Score1 = 0
        win1 = Tk()
        win1.resizable(width=False, height=False)
        win1.title('Logic Of Woe')
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

                Photo = PhotoImage(file = Images[i])
                
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
CreateGUI1(Count)
