# Developed my Oliver M
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('Tab Bar')
NB = ttk.Notebook(window)
T1 = ttk.Frame(NB)
T2 = ttk.Frame(NB)
T3 = ttk.Frame(NB)
B1 = ttk.Button(T1, text = 'Button Of Woe')
B1.pack(padx = 40, pady = 20)
NB.add(T1, text = 'Logic Gates')
NB.add(T2, text = 'FDE Cycle')
NB.add(T3, text = 'Memory')
NB.pack()
window.mainloop()
