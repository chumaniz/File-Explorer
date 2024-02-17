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

# Function for renaming a file 
def rename_a_file():
    selectedFile = open_a_window()
    path_source = os.path.dirname(selectedFile)
    extender = os.path.splitext(selectedFile) [1]
    print("Enter new File name")
    newFileName = input()
    path = os.path.join(path_source, newFileName+extender)
    print(path)
    os.rename(selectedFile,path)
    mb.showinfo('Notice', "File Renamed!")

# Function for moving a file
def move_a_folder():
    source = open_a_window()
    location = filedialog.askdirectory()
    if (source==location):
        mb.showinfo('Notice', "Source and location are concurrent")
    else:
        shutil.move(source, location)  
        mb.showinfo('Notice', "File Moved Successfully!")

# Function for Making a Folder
def make_a_folder():
    brandNewFolderPath = filedialog.askdirectory()
    print("Enter New Folder Name")  
    brandNewFolder = input()
    path = os.path.join(brandNewFolderPath, brandNewFolder)

    os.mkdir(path)
    mb.showinfo('Notice', "Folder Made Successfully!")

# Function for Deleting a Folder
def delete_a_folder():
    delete_a_folder = filedialog.askdirectory()
    os.rmdir(delete_a_folder)
    os.remove(delete_a_folder)
    mb.showinfo('Notice', "File Deleted")