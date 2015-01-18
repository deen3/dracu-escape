"""
This module is for displaying highcores.
"""
import pygame
import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from itertools import chain

import masterDracu

class Menu(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)   
 
        #reference to the master widget, which is the tk window                 
        self.master = master
 
        self.init_window()
        self.show_buttons()

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
        self.bg = ImageTk.PhotoImage(Image.open("includes/img/bg.png"))
        self.bg_sub = ImageTk.PhotoImage(Image.open("includes/img/bg-sub.png"))
        self.btn_menu = ImageTk.PhotoImage(Image.open("includes/img/btn-menu.png"))
        self.btn_menuH = ImageTk.PhotoImage(Image.open("includes/img/btn-menuH.png"))
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
        self.bg_img = Label(self, image=self.bg)
        self.bg_img.image = self.bg
        self.bg_img.place(x=-2, y=-2)

    def show_buttons(self):
        # display buttons
        self.btn1 = Button(self, bd=0, bg="black", image = self.btn_play, command=self.show_play)
        self.btn1.configure(image = self.btn_play)
        self.btn1.place(x=555, y=150)
        self.btn1.bind('<Enter>', self.btn1Enter)
        self.btn1.bind('<Leave>', self.btn1Leave)

        self.btn2 = Button(self, bd=0, bg="black", image = self.btn_score, command=self.show_highscore)
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
    def btn4Enter(self, event):
        self.btn4.configure(image = self.btn_menuH)
        self.hoveredSound.play()

    def btn1Leave(self, no):
        self.btn1.configure(image = self.btn_play)
    def btn2Leave(self, no):
        self.btn2.configure(image = self.btn_score)
    def btn3Leave(self, no):
        self.btn3.configure(image = self.btn_option)
    def btn4Leave(self, no):
        self.btn4.configure(image = self.btn_menu)

    def show_menu(self):
        self.init_window()
        self.show_buttons()

    def show_play(self):
        masterDracu.main()
        quit()
        
    def show_highscore(self):
        self.init_window()
        self.bg_img.configure(image = self.bg_sub)

        score = ImageTk.PhotoImage(Image.open("includes/img/lbl-score.png"))
        lbl = Label(self, bd=0, image=score)
        lbl.image = score
        lbl.place(x=300, y=155)

        self.btn4 = Button(self, bd=0, bg="gray", image = self.btn_menu, command=self.show_menu)
        self.btn4.configure(image = self.btn_menu)
        self.btn4.place(x=300, y=400)
        self.btn4.bind('<Enter>', self.btn4Enter)
        self.btn4.bind('<Leave>', self.btn4Leave)
        
##        fr = Frame (self, width=50, height=45).place(x=60, y=200)
##        # make a listbox
##        self.lb = Listbox(self, bd=0, activestyle="dotbox", bg="gray", height=15, width=20, font=("Agency FB", 16))
##        #self.lb.bind('<Double-Button-1>',self.lbSelected)
##        self.lb.place(x=45, y=180)
##
##        # put values in lb from db
##        conn = sqlite3.connect("dracuDb.s3db")
##        cur = conn.execute("SELECT dracuDb_score FROM dracuTbl ORDER BY dracuDb_score")
##        try:
##            first_row = next(cur)
##            for row in chain((first_row,),cur):
##                self.lb.insert(END, str(row[0])+" --- "+str(row[0]))
##        except StopIteration as e:
##            self.lb.insert(END,"Empty Record")

        conn = sqlite3.connect("dracuDb.s3db")
        cur = conn.execute("SELECT dracuDb_score FROM dracuTbl ORDER BY dracuDb_score")
        lbl = Label(self, bd=0, bg="lightgray", font=("Chiller", 20), text="1. \n2. \n3. \n4. \n5. ").place(x=270, y=230)
        lbl = Label(self, bd=0, bg="lightgray", font=("Chiller", 20), text="Dina\nDevy\nDevinson\nKienah\nFhianne").place(x=300, y=230)
        lbl = Label(self, bd=0, bg="lightgray", font=("Chiller", 20), text="1. \n2. \n3. \n4. \n5. ").place(x=270, y=230)
        
root = Tk()
root.geometry("800x600")

#creation of an instance
app = Menu(root)

#mainloop 
root.mainloop()
