# Written by Oliver Mardle 2017
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Year 11 Computing Revision Tools')

RootFrame = ttk.Frame(root)
RootFrame.pack()
    
L1 = ttk.Label(RootFrame, text = 'Welcome to the Year 11 GCSE Computing Revision Tool Kit.\nTo proceed, Click on one of the subjects below:\nOr to exit press \'Exit\'')
L1.grid(row = 1, column = 1, columnspan = 2, pady = 10)
B1 = ttk.Button(RootFrame, text = 'Logic Gates', width = 16).grid(row = 2, column = 1)
B2 = ttk.Button(RootFrame, text = 'Data Representation', width = 16).grid(row = 2, column = 2)
B3 = ttk.Button(RootFrame, text = 'System Architecture', width = 16).grid(row = 3, column = 1)
B4 = ttk.Button(RootFrame, text = 'Networks', width = 16).grid(row = 3, column = 2)
B5 = ttk.Button(RootFrame, text = 'Character Encoding', width = 16).grid(row = 4, column = 1)
B6 = ttk.Button(RootFrame, text = 'Software Dev Lifecycle', width = 16).grid(row = 4, column = 2)
B7 = ttk.Button(RootFrame, text = 'Data Types', width = 16).grid(row = 5, column = 1)
B8 = ttk.Button(RootFrame, text = 'Data Structures', width = 16).grid(row = 5, column = 2)
B9 = ttk.Button(RootFrame, text = 'Exit', width = 16).grid(row = 6, column = 1, columnspan = 2, pady = 10)

root.mainloop()
