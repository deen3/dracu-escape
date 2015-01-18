"""
This module is for displaying highcores.
"""
import pygame
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
        #self.show_highscore()
 
    def init_window(self):
        pygame.init()
        # initialize sounds/music
        self.hoveredSound = pygame.mixer.Sound('includes/sound/button.wav')
        pygame.mixer.music.load('includes/music/menu-music.wav')
        pygame.mixer.music.play(10)
        
        # changing the title of our master widget      
        self.master.title("DRACU-ESCAPE")

        # load images to use
        icon = ImageTk.PhotoImage(Image.open("includes/img/icon.png"))
        bg = ImageTk.PhotoImage(Image.open("includes/img/bg.png"))
        self.btn_play = ImageTk.PhotoImage(Image.open("includes/img/btn-play.png"))
        self.btn_playH = ImageTk.PhotoImage(Image.open("includes/img/btn-playH.png"))
        self.btn_score = ImageTk.PhotoImage(Image.open("includes/img/btn-score.png"))
        self.btn_scoreH = ImageTk.PhotoImage(Image.open("includes/img/btn-scoreH.png"))
        self.btn_option= ImageTk.PhotoImage(Image.open("includes/img/btn-option.png"))
        self.btn_optionH= ImageTk.PhotoImage(Image.open("includes/img/btn-optionH.png"))
        
        # setting the icon
        self.tk.call('wm', 'iconphoto', root._w, icon)

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # display background
        img = Label(self, image=bg)
        img.image = bg
        img.place(x=-2, y=-2)

        # display buttons
        self.btn1 = Button(self, bd=0, bg="black", image = self.btn_play)
        self.btn1.configure(image = self.btn_play)
        self.btn1.place(x=555, y=150)
        self.btn1.bind('<Enter>', self.btn1Enter)
        self.btn1.bind('<Leave>', self.btn1Leave)

        self.btn2 = Button(self, bd=0, bg="black", image = self.btn_score)
        self.btn2.configure(image = self.btn_score)
        self.btn2.place(x=555, y=235)
        self.btn2.bind('<Enter>', self.btn2Enter)
        self.btn2.bind('<Leave>', self.btn2Leave)

        self.btn3 = Button(self, bd=0, bg="black", image = self.btn_option)
        self.btn3.configure(image = self.btn_option)
        self.btn3.place(x=555, y=315)
        self.btn3.bind('<Enter>', self.btn3Enter)
        self.btn3.bind('<Leave>', self.btn3Leave)

    def btn1Enter(self, event):
        self.btn1.configure(image = self.btn_playH)
        self.hoveredSound.play()
    def btn2Enter(self, event):
        self.btn2.configure(image = self.btn_scoreH)
        self.hoveredSound.play()
    def btn3Enter(self, event):
        self.btn3.configure(image = self.btn_optionH)
        self.hoveredSound.play()

    def btn1Leave(self, no):
        self.btn1.configure(image = self.btn_play)
    def btn2Leave(self, no):
        self.btn2.configure(image = self.btn_score)
    def btn3Leave(self, no):
        self.btn3.configure(image = self.btn_option)

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
