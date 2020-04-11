import pandas as pd
import random
from tkinter import *
#import seaborn as sns

#--------------------------------------ROADMAP--------------------------------------------------
    #1.0:
        #Initialization manually for every character
        #Weighted randomization based on enjoyment of characters on a scale of 0-10
        #Manually Remove Characters from the pool of available characters graphically
    #1.1:
        #Quick initialization (Done by fighter type)
        #Graphical update
        #New data:
            #Weight Class
            #Fighter Type
            #Universe
    #2.0
        #Multiple profile/player support
        #Inlcude offline stage selection support (new csv)
        #Restrict character pool through graphical UI elements (restrict by any of the data as well as search bars)
    #X.X:
        #Statistics section??


#--------------------------------------DEBUG FUNCTIONS---------------------------
def assignRandom(row):
    return random.randint(0,10)


#-----------------------Functions--------------
def assignEach(row):
    while(True):
        message = "For %s, rate your enjoyment (0-10): " % (row["Fighters"])
        enjoyment = input(message)
        if(enjoyment == ''):
            print("That is an invalid input. Enter an integer from 0-10")
            print()
            continue
        elif((enjoyment in "12345678910")):
            return int(enjoyment)          
        else:
            print("That is an invalid input. Enter an integer from 0-10")
            print()
            continue
            


def init():
    #If the csv doesn't exist then create it through web scraper and run player input
    
    #GENERATE CSV THROUGH SCRAPE

    #if("UserEnjoyment" not in dt.columns):
        #dt["UserEnjoyment"] = dt.apply(assignEach, axis = 1)
    dt["UserEnjoyment"] = dt.apply(assignRandom, axis = 1)
    if("Odds" not in dt.columns):    
        total = dt["UserEnjoyment"].sum()
        dt["Odds"] = dt["UserEnjoyment"]/total
        dt["Odds"] = dt["Odds"].cumsum()
    for i in range(5):
        randomize(dt)
    dt.sort_index(inplace = True)
    dt.to_csv(path_or_buf = "./scrapeData.csv", index = False)

def randomize(options):
    number = random.random()
    selection = options[options["Odds"] < number][-1:]
    print("Fighter: %s\nEnjoyment: %s" % (selection["Fighters"], selection["UserEnjoyment"]))
    #return selection["Fighters"] 


#---------------------------------------Main----------------------------------------
try:
    dt = pd.read_csv("./scrapeData.csv", index_col = 0)
    if(not "UserEnjoyment" in dt.columns):
        init()
except:
    #Run init
    dt = None

init()