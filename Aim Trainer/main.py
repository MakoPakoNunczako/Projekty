from tkinter import *
import tkinter as tk
import random
import pygame

licznik = 0
licznik2 = 0
licznik3 = 0
licznik_ogl=0

# 
def startuj():
    root.destroy()
    aim = tk.Tk()
    aim.title("Ćwicz")
    aim.geometry('500x500')
    global wynik

    class RoundedButton(tk.Canvas):
        def __init__(self, parent, width, height, cornerradius, padding, color, bg, command=None):
            tk.Canvas.__init__(self, parent, borderwidth=0, 
                relief="flat", highlightthickness=0, bg=bg)
            self.command = command

            if cornerradius > 0.5*width:
                print("Error: cornerradius is greater than width.")
                return None

            if cornerradius > 0.5*height:
                print("Error: cornerradius is greater than height.")
                return None

            rad = 2*cornerradius
            def shape():
                self.create_polygon((padding,height-cornerradius-padding,padding,cornerradius+padding,padding+cornerradius,padding,width-padding-cornerradius,padding,width-padding,cornerradius+padding,width-padding,height-cornerradius-padding,width-padding-cornerradius,height-padding,padding+cornerradius,height-padding), fill=color, outline=color)
                self.create_arc((padding,padding+rad,padding+rad,padding), start=90, extent=90, fill=color, outline=color)
                self.create_arc((width-padding-rad,padding,width-padding,padding+rad), start=0, extent=90, fill=color, outline=color)
                self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), start=270, extent=90, fill=color, outline=color)
                self.create_arc((padding,height-padding-rad,padding+rad,height-padding), start=180, extent=90, fill=color, outline=color)


            id = shape()
            (x0,y0,x1,y1)  = self.bbox("all")
            width = (x1-x0)
            height = (y1-y0)
            self.configure(width=width, height=height)
            self.bind("<ButtonPress-1>", self._on_press)
            self.bind("<ButtonRelease-1>", self._on_release)

        def _on_press(self, event):
            self.configure(relief="sunken")

        def _on_release(self, event):
            self.configure(relief="raised")
            if self.command is not None:
                self.command()

    def koniec():
        wynik = tk.Tk()
        wynik.title("Wynik")
        wynik.geometry("300x200")
        wynik.config(bg="black")

        label_frame = tk.Frame(wynik, bg="black")
        label_frame.pack(pady=20)

        label = tk.Label(
            label_frame,
            text="Twój wynik: {}".format(licznik_ogl),
            font=("Helvetica", 20),
            fg="white",
            bg="black"
        )
        label.pack()

        button_frame = tk.Frame(wynik, bg="black")
        button_frame.pack(pady=20)

        button = tk.Button(
            button_frame,
            text="Zamknij",
            font=("Helvetica", 12),
            fg="white",
            bg="red",
            relief="solid",
            command=wynik.destroy
        )
        button.pack()

        wynik.mainloop()


    


    def test():
        global licznik
        global a2
        global b2
        licznik+=1
        global licznik_ogl
        licznik_ogl+=1
        a=float(random.randint(1,8)/10)
        b=float(random.randint(1,8)/10)
        button.place(relx=a, rely=b)
        pygame.init()
        point = pygame.mixer.Sound("clicked.mp3")
        pygame.mixer.music.load('clicked.mp3')
        pygame.mixer.music.play(1)
        # print("kulka1:",licznik, " roznica: ", licznik-licznik2)
        if licznik == 3:
            a2=float(random.randint(1,8)/10)
            b2=float(random.randint(1,8)/10)
            button2.place(relx=a2, rely=b2)
        if licznik-licznik2>8 or licznik2-licznik<-8 or licznik2-licznik3>8:
            aim.destroy()
            koniec()
            return test
    
    def test2():
        global licznik2
        licznik2+=1
        global licznik_ogl
        licznik_ogl+=1
        a2=float(random.randint(1,8)/10)
        b2=float(random.randint(1,8)/10)
        button2.place(relx=a2, rely=b2)
        point = pygame.mixer.Sound("clicked.mp3")
        pygame.mixer.music.load('clicked.mp3')
        pygame.mixer.music.play(1)
        # print("kulka2:",licznik2, " roznica: ", licznik2-licznik)
        if licznik2 == 3:
            a3=float(random.randint(1,8)/10)
            b3=float(random.randint(1,8)/10)
            button3.place(relx=a3, rely=b3)

        if a==a2:
            a2=float(random.randint(1,8)/10)
        if b==b2:
            b2=float(random.randint(1,8)/10)
        if licznik-licznik2>8 or licznik2-licznik<-8 or licznik2-licznik3>8:
            aim.destroy()
            koniec()

    def test3():
        global licznik3
        licznik3+=1
        global licznik_ogl
        licznik_ogl+=1
        a3=float(random.randint(1,8)/10)
        b3=float(random.randint(1,8)/10)
        button3.place(relx=a3, rely=b3)
        point = pygame.mixer.Sound("clicked.mp3")
        pygame.mixer.music.load('clicked.mp3')
        pygame.mixer.music.play(1)
        # print("kulka3:",licznik3, " roznica: ", licznik2-licznik3)
        if a and a2==a3:
            a3=float(random.randint(1,8)/10)
        if b and b2==b3:
            b3=float(random.randint(1,8)/10)
        if licznik-licznik2>8 or licznik2-licznik<-8 or licznik2-licznik3>8:
            aim.destroy()
            koniec()
        

    canvas = Canvas(aim, height=500, width=500)
    canvas.config(background="black")
    canvas.pack()
    button = RoundedButton(aim, 50, 50, 25, 0, 'red','black', command=test)
    button2 = RoundedButton(aim, 30, 30, 15, 0, 'orange','black', command=test2)
    button3 = RoundedButton(aim, 40, 40, 20, 0, 'blue','black', command=test3)
    a=float(random.randint(1,8)/10)
    b=float(random.randint(1,8)/10)
    button.place(relx=a, rely=b)
    # var = StringVar()
    # var.set(licznik_ogl)
    aim.update()
    aim.update_idletasks()
    aim.mainloop()
    

# a = 1 do 8 | b = 1 do 8

root = tk.Tk()
root.geometry('500x350')
root.resizable(False, False)
root.title("Aim Trainer")

# Set a background image
root.config(bg="#333333")

# Add a title label
title_label = tk.Label(root, text="Trenuj swojego Aim'a", font=("Helvetica", 24), fg="white", bg="black")
title_label.pack(pady=20)

# Add a description label
description_label = tk.Label(root, text="Aby wygrać, utrzymaj równowagę między kulami", font=("Helvetica", 12), fg="red", bg="black")
description_label.pack()

# Add a start button
start_button = tk.Button(root, command=startuj ,text="START", width=10, height=2, font=("Helvetica", 12), fg="white", bg="#008080")
start_button.pack(pady=20)

root.mainloop()
