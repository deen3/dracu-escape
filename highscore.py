"""
This module is for displaying highcores.
"""
import sqlite3
from tkinter import *
from PIL import Image, ImageTk

class Highscore(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)   
 
        #reference to the master widget, which is the tk window                 
        self.master = master
 
        self.init_window()
 
    def init_window(self):
        # changing the title of our master widget      
        self.master.title("DRACU-ESCAPE")

        # load images to use
        icon = ImageTk.PhotoImage(Image.open("includes/img/icon.png"))
        bg = ImageTk.PhotoImage(Image.open("includes/img/bg.png"))
        
        # setting the icon
        self.tk.call('wm', 'iconphoto', root._w, icon)

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # display background
        img = Label(self, image=bg)
        img.image = bg
        img.place(x=-2, y=-2)

root = Tk()
root.geometry("800x600")

#creation of an instance
app = Highscore(root)

#mainloop 
root.mainloop()
