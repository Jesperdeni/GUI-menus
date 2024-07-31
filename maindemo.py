from tkinter import *
from menus.filemenu import *
from menus.editmenu import *

 
a= Tk()
a.title("Demo")
a.geometry("500x500+200+100")



def menulist(pass_a):
    menulist=Menu(pass_a)
    pass_a.config(menu=menulist)

    filemenulist(menulist)
    editmenulist(menulist)
    

menulist(a)

a.mainloop()