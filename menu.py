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

        self.btn3 = Button(self, bd=0, bg="black", image = self.btn_option, command=self.show_option)
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
        self.show_sub_bg("score")

        ctr = 1
        addy = 235

        conn = sqlite3.connect("dracuDb.s3db")
        cur = conn.execute("SELECT * FROM dracuScore ORDER BY dracuDb_score DESC")
        try:
            first_row = next(cur)
            for row in chain((first_row,),cur):
                if ctr > 5:
                    break
                else:
                    lbl = Label(self, bd=0, bg="lightgray", font=("Chiller", 20), text=str(ctr)+". "+str(row[1])+"\t\t---\t"+str(row[2])).place(x=225, y=addy)

                    ctr = ctr + 1
                    addy = addy + 30
                
        except StopIteration as e:
            lbl = Label(self, bd=0, bg="lightgray", font=("Chiller", 20), text="No scores stored in the database.").place(x=225, y=235)

    def show_option(self):
        self.show_sub_bg("option")

        img = ImageTk.PhotoImage(Image.open("includes/img/bg-options.png"))
        lbl = Label(self, bd=0, image=img)
        lbl.image = img
        lbl.place(x=290, y=280)

        # load images to use
        rd1 = ImageTk.PhotoImage(Image.open("includes/img/rd-music.png"))
        rd2 = ImageTk.PhotoImage(Image.open("includes/img/rd-sound.png"))

        music = Button(self, bd=0, bg="gray", image = rd1, command=self.update_music)
        music.image = rd1
        music.place(x=445, y=290)

        sound = Button(self, bd=0, bg="gray", image = rd2, command=self.update_sound)
        sound.image = rd2
        sound.place(x=447, y=338)

        conn = sqlite3.connect("dracuDb.s3db")
        cur = conn.execute("SELECT * FROM dracuOption ORDER BY dracuDb_score DESC")
        try:
            first_row = next(cur)
            for row in chain((first_row,),cur):
                if row[0] == True: # if music is on
                    
                else:
                    
                if row[1] == True: # if sound is on

                else:
                
        except StopIteration as e:
            lbl = Label(self, bd=0, bg="lightgray", font=("Chiller", 20), text="An error occured.").place(x=225, y=235)


    def show_sub_bg(self, lbl):
        self.init_window()
        self.bg_img.configure(image = self.bg_sub)

        img = ImageTk.PhotoImage(Image.open("includes/img/lbl-"+lbl+".png"))
        lbl = Label(self, bd=0, image=img)
        lbl.image = img
        lbl.place(x=300, y=155)

        self.btn4 = Button(self, bd=0, bg="gray", image = self.btn_menu, command=self.show_menu)
        self.btn4.configure(image = self.btn_menu)
        self.btn4.place(x=300, y=400)
        self.btn4.bind('<Enter>', self.btn4Enter)
        self.btn4.bind('<Leave>', self.btn4Leave)

    def update_music(self):
        conn = sqlite3.connect("dracuDb.s3db")
        cur = conn.execute("SELECT music FROM dracuOption")
        try:
            first_row = next(cur)
            for row in chain((first_row,),cur):
                print(str(row[0]))
                if str(row[0]) == "True": # if music is on
                    conn.execute("UPDATE dracuOption set music='False'")
                    conn.commit()
                else:
                    conn.execute("UPDATE dracuOption set music='True'")
                    conn.commit()
        except StopIteration as e:
            lbl = Label(self, bd=0, bg="lightgray", font=("Chiller", 20), text="An error occured.").place(x=225, y=235)
        self.show_option()
        
    def update_sound(self):
        conn = sqlite3.connect("dracuDb.s3db")
        cur = conn.execute("SELECT sound FROM dracuOption")
        try:
            first_row = next(cur)
            for row in chain((first_row,),cur):
                print(str(row[0]))
                if str(row[0]) == "True": # if music is on
                    conn.execute("UPDATE dracuOption set sound='False'")
                    conn.commit()
                else:
                    conn.execute("UPDATE dracuOption set sound='True'")
                    conn.commit()
        except StopIteration as e:
            lbl = Label(self, bd=0, bg="lightgray", font=("Chiller", 20), text="An error occured.").place(x=225, y=235)
        self.show_option()
           
root = Tk()
root.geometry("800x600")

#creation of an instance
app = Menu(root)

#mainloop 
root.mainloop()
