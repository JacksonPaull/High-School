"""import tkinter as tk
from tkinter import *
import random
from PIL import ImageTk,Image
import math
import pandas as pd"""
from app import *

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title('Smash Randomizer')
        self.geometry('400x400')
        self.frames = {}
        for F in (StartPage, randomPage, settingsPage, fighterSelectPage, setFighterEnjoymentPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        tk.Label(self,text = 'Start Page', fg ='black').pack()
        tk.Button(self,text = 'Go to randomizer page', command = lambda: controller.show_frame(randomPage)).pack()
        tk.Button(self,text = 'Go to settings page', command = lambda: controller.show_frame(settingsPage)).pack()
        tk.Button(self,text = 'Go to enjoyment setting page', command = lambda: controller.show_frame(setFighterEnjoymentPage)).pack()
        #tk.Button(self,text = 'Go to settings page', command = lambda: controller.show_frame(settingsPage)).pack()
        randomPageBtn = tk.Button(self,text = 'Go to Fighter Select page', command = lambda: controller.show_frame(fighterSelectPage))
        randomPageBtn.pack()

        
        #Quit button
        button = tk.Button(self,text = "Quit",  command = lambda:controller.destroy())
        button.pack()


class randomPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self,text = '<fighterName>', fg ='grey')
        label.pack()
        numlabel = tk.Label(self,text = '<fighterNumber>', fg ='grey')
        numlabel.pack()

        button = tk.Button(self,text = 'Random Fighter', width = 25, 
                        command = lambda:genFighter(dt,label,numlabel,canvas,app))
        button.pack()

        image = openImage('./fighterImages/main/mario.png')
        controller.image = image
        canvas = Canvas(self, width = 100, height =100)      
        canvas.pack()
        fighterImage = canvas.create_image((0,0),anchor =NW, image=image)
        



        #Quit button
        tk.Button(self,text = "Quit", width = 25, command =lambda:controller.destroy()).pack()
        tk.Button(self,text = 'Back', command = lambda: controller.show_frame(StartPage)).pack()
        
    
class settingsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        options = {'included':'Included','notIncluded':'Not Included'}

        tk.Label(self,text ='Current Inclusion Status:', fg = 'black').pack()
        settingsList = tk.Label(self,text =options[settings['user1']['echos']], fg = 'black')
        settingsList.pack()

        
        combo = ttk.Combobox(self,values=list(options.values()))
        combo.pack()
        combo.current(1)
        #save button
        button = tk.Button(self,text = 'Save Settings', command =lambda:
                    saveSettings('user1','echos',list(options.keys())[combo.current()],settingsList,options))
        button.pack()

        button = tk.Button(self,text = "Back", command =lambda:controller.show_frame(StartPage))
        button.pack()

        button = tk.Button(self,text = "Quit", command =lambda:controller.destroy())
        button.pack()
    
class fighterSelectPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        """for row in dt.iterrows():
            canvas = Canvas(self,height = 100, width = 100)
            canvas.pack()
            
            image = openImage('./fighterImages/main/mario.png')
            controller.image = image
            fighterImage = canvas.create_image((0,0),anchor =NW, image=image)"""

        """
        draw a canvas of specified image size for each fighter and assign it's thumb_h
        dt.iterrows????
        putting a onclick for canvas?
        drawing the image with a rectangle of half opacity above it to indicate deselected?

        add an extra column of "available" in dt?
        dont need to write it out and have it on start up equal true for everyone?

        scrolling page in tkinter
        """


        tk.Button(self,text = "Back", command =lambda:controller.show_frame(StartPage)).pack()
        tk.Button(self,text = "Quit", command =lambda:controller.destroy()).pack()

class setFighterEnjoymentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        """
        create an update function
        pass label, dt, current fighter number, and entry field
        read in entry field as an int
        store it in the dt for the appropriate fighter as enjoyment
        then rewrite label for the next fighter, provided it doesnt overflow
        repeat, and at the end of the function write this to userXenj.csv
        modify reading the dt to join the scrape data and userenj on fighter name 
        
        """


        l = tk.Label(self, text = 'Enter your level of enjoyment for %s below.'%('bigDick'), fg = 'black')
        l.pack()
        enj = tk.Entry(self)
        enj.pack()
        
        tk.Button(self, text = 'test', command = lambda: l.config(text = enj.get())).pack()
        
        #Quit button
        tk.Button(self, text = "Quit",  command = lambda:controller.destroy()).pack()
    

app = App()
app.mainloop()