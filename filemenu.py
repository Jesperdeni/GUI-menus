from tkinter import *



def filemenulist(pass_menulist):
    filemenu=Menu(pass_menulist,tearoff=0)
    pass_menulist.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="New File")
    filemenuextra(filemenu)

def filemenuextra(filemenu):
    filemenu.add_command(label="New Window")
    filemenu.add_separator()
    filemenu.add_command(label="Open")
    filemenu.add_separator()
    filemenu.add_command(label="Save")
    filemenu.add_command(label="Save As")
    filemenu.add_separator()
    filemenu.add_command(label="Close")

    



