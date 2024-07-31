from tkinter import *


def editmenulist(pass_menulist):
    editmenu=Menu(pass_menulist)
    pass_menulist.add_cascade(label="Edit",command=editmenu)
    editmenu.add_command(label="Undo")
    editmenu.add_command(label="Redo")
    
    
    
    
   