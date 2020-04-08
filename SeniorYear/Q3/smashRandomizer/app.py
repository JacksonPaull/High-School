import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
from PIL import ImageTk,Image
import math
from functools import partial
import pandas as pd
import numpy
import json


dt = pd.read_csv('./scrapeData.csv',index_col=0)
with open('settings.json') as f:
    settings = json.load(f)

#-----------------------------------------------Functions---------------
def openImage(filepath):
    image = Image.open(filepath)
    image = image.resize((100,100))
    image = ImageTk.PhotoImage(image)
    return image

def changeFighter(label,numlabel,fighterName,index,filename):
    img = openImage('./fighterImages/main/%s'%(filename))
    label.config(text = fighterName, fg = 'black')
    numlabel.config(text =index, fg = 'black')
    return img


def close_window(root):
    root.destroy()


def randomFighter(dt,column,label,numlabel):
    df = dt.copy()
    df.drop_duplicates(subset = column,inplace = True)
    selection = df.sample(n=1)
    name = selection['Fighters'].values[0]
    index = selection[column].values[0]
    filename = selection['filename'].values[0]
    return changeFighter(label,numlabel,name.lower(),index,filename)

def genFighter(options,label,numlabel,canvas,controller):
    if settings['user1']['echos'] == 'notIncluded':
        col = 'numNoEcho'
    else:
        col = 'FighterNumber'

    img = randomFighter(options,col,label,numlabel)
    controller.image = img
    canvas.delete('all')
    fighterImage = canvas.create_image((0,0),anchor =NW, image=img)
    return img






def saveSettings(user,data,info,label,options):
    settings[user][data] = info
    label.config(text = options[info])
    with open('settings.json', 'w') as f:
        json.dump(settings,f)
    refreshSettings()

def refreshSettings():
    with open('settings.json') as f:
        settings = json.load(f)    
#-----------------------------------------------------------------------





"""NOTES FOR EXPANSION
-need to code in filename system
    probably best to do this at the scrape which should go in the order
        names
        images
        icons
        stats (with stats having a button in the app to regather)
    This could be done by gathering the name of the fighter when scraping thumb_h and attaching that filename to the row of that fighter in pandas    
    Then, when you need to retrieve the filename for that character you simply index the dataframe

    Make up a way to input enjoyment through the app interface
    


    MODES
        -True Random
            is what it sounds like
        -Weighted random based on likeness
            needs
            -interface to input enjoyment
            -weighted index
            Could be done with a randint from 0 to the cumulative sum of all enjoyment levels, and selecting the last fighter with a cumulative enjoyment less that
        -Manual selection
            interface could have heros as clickable buttons that when clicked fade out by drawing a rectangle the size of the image over it at 50% opacity
            needs
                -selective indexing
                -to be able to know which fighters are selected, pref in a series, then a slice of the dt is taken with fighters = to the series and then acts normal
        -Extra options
            -index by tier
            -index by winrate
            -index by weight
            -index by speed
            -index by franchise
            -index by archetype


        -Stats
            -would require whole new interface and data tracking... this comes last

        -profiles
            -save files containing user likeness data as a piece of their name and simply let them choose profile from a dropdown menu

        -duos
            this can come later but all of the stuff outlined above just with teams (some of the other options like tier)
            might be interesting to be able to have a manual list of teams enjoyed by user that can be randomly selected from to guarentee synergy

"""