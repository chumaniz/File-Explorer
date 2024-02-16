from tkinter import *
import shutil
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb

# To open a file box window
# To be able to select a file
def open_a_window():
    read = easygui.fileopenbox()
    return read

# Open file function
def open_a_file():
    string = open_a_window
    try:
        os.startfile(string)
    except:
        mb.showinfo('File-Found', "File")