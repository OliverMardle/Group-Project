import sys
from cx_Freeze import setup, Executable

import os

os.environ['TCL_LIBRARY'] = "C:\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Python36-32\\tcl\\tk8.6"

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

opts = {'include_files':["tcl86t.dll", "tk86t.dll", "AND.gif", "NAND.gif", "NOR.gif", "NOT.gif", "OR.gif", "XNOR.gif", "XOR.gif", "0.txt", "1.txt", "2.txt", "3.txt", "4.txt", "5.txt", "6.txt"], 'includes': ['re', 'tkinter']}

setup( name = 'Y11 GCSE Computing ToolKit',
       version = '3.1',
       description = 'Year 11 GCSE Computing Revision Tool-Kit for Logic Gates, Data Representation and Data Types',
       author = 'Oliver Mardle',
       options = {'build_exe': opts},
       executables = [Executable('Y11 GCSE Computing ToolKit.py', base = base)])
