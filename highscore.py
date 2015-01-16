"""
This module is for displaying highcores.
"""
import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from itertools import chain

class Highscore(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)   
 
        #reference to the master widget, which is the tk window                 
        self.master = master
 
        self.init_window()
        self.show_highscore()
 
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

    def show_highscore(self):
        fr = Frame (self, width=50, height=45).place(x=60, y=200)
        # make a listbox
        self.lb = Listbox(self, bd=0, activestyle="dotbox", bg="gray", height=15, width=20, font=("Agency FB", 16))
        #self.lb.bind('<Double-Button-1>',self.lbSelected)
        self.lb.place(x=45, y=180)

        # put values in lb from db
        conn = sqlite3.connect("dracuDb.s3db")
        cur = conn.execute("SELECT dracuDb_score FROM dracuTbl ORDER BY dracuDb_score")
        try:
            first_row = next(cur)
            for row in chain((first_row,),cur):
                self.lb.insert(END, str(row[0])+" --- "+str(row[0]))
        except StopIteration as e:
            self.lb.insert(END,"Empty Record")

root = Tk()
root.geometry("800x600")

#creation of an instance
app = Highscore(root)

#mainloop 
root.mainloop()
