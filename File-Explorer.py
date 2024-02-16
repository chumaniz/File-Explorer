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
        mb.showinfo('Notice', "File Not Found!")

# Function for copying a file
def copy_a_file():
    source_original = open_a_window
    location_original = filedialog.askdirectory()
    shutil.copy(source_original,location_original)
    mb.showinfo('Notice', "File Copied!")

# Function for deleting a file
def delete_a_file():
    delete_a_file = open_a_window
    if os.path.exists(delete_a_file):
        os.remove(delete_a_file)
    else:
        mb.showinfo('Notice', "File Not Found!")