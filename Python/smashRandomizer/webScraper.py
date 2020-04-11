#---------------------------------DATA LINKS------------------------------------------- 
    # Link 1:
    #   https://www.smashbros.com/en_US/fighter/index.html
    #   Use to grab:
    #       Fighter names
    #       Index number
    #       (Optional)
    #       Series Icon
    #       Image
    #       
    #Link 2:
    #   https://www.unitstatistics.com/ssbu/
    #   Use to grab:
    #       Tier
    #       Weight
    #       Air Speed
    #       Icon (minimalistic)
    #
    #Link 3:
    #   https://rankedboost.com/super-smash-bros/mario/
    #   Use to grab:
    #       Universe
    #       Counters
    #


#--------------------------------INFORMATION-------------------------------------------
    #This is a web scraper intended to gather information from 
    #the aforementioned links
    #It should be able to run every patch (on specific websites) 
    #So that I can piggyback on someone else's work
    #TODO Finish documentation with specifics on the data it gathers

#-----------------------------------IMPORTS----------------------------------------------------
import pandas as pd                                                  #Data science stuff
from selenium import webdriver                                       #Used to get rendered stuff
from bs4 import BeautifulSoup                                        #Used to work through the HTML
import urllib3
import requests
import os


try:
    dt = pd.read_csv('./scrapeData.csv')
except:
    dt = pd.DataFrame()


#-------------------------------------FUNCTIONS-------------------------------------------------------
def getText(array):                                                  #Used to change raw HTML to text
    i = 0
    while i < len(array):
        array[i] = array[i].text
        i+=1

def setEchos(row):                                                   #Used to document where the echos are
    global dt
    if("ᵋ" in row["FighterNumber"]):
        index = dt[dt["FighterNumber"]==row["FighterNumber"]].index.values[0]
        return "Echo Fighter of %s" %(dt.iloc[index-1]["Fighters"])
    return 'notEcho'

def fighterNumberNoEcho(row):                                        #Used to reset fighter number without the echo
    number = row["FighterNumber"][:2]                                #This is because I can use the regular index as the echo fighter inclusion index
    return number                                                    #While using the noEcho fighternumber as the echo exclusive index

def fixImageLinks(l):
    i = 0
    for link in l:
        text = link['style']
        urlend = text[text.index('image:url(')+10:-2]
        l[i] ='smashbros.com%s\n'%(urlend)
        i +=1

def fixImageLinksForFull(l):
    i = 0
    for link in l:
        text = link['style']
        urlstrt = text[text.index('image:url(')+10:text.index('/thumb_h'):]
        urlend = text[text.index('/thumb_h')+8:-6]
        x = 'smashbros.com%s%s/main.png'%(urlstrt, urlend)
        l[i] = x
        i +=1

#-------------------------------------FIRST LINK-----------------------------
link1 = "https://www.smashbros.com/en_US/fighter/index.html"
browser = webdriver.Chrome()                                         #Creates physical browser
browser.get(link1)                                                   #Opens link in browser
content = browser.execute_script("return document.body.innerHTML")   #Returns the inner HTML as a string
HTML = BeautifulSoup(content, "html.parser")



def gendt():
    global dt

    fighters = HTML.findAll('p', class_ = "fighter-list__name-main")
    index = HTML.findAll('p', class_ = "fighter-list__num")
    getText(fighters)
    getText(index)

    #-----------------------------------DataFrameGeneration---------
    dt = pd.DataFrame([index, fighters])
    dt = dt.transpose()

    #------------------------------------DATA CLEANING, Link 1--------
    dt.rename(columns = {
        0:"FighterNumber",
        1:"Fighters"
    }, inplace = True)

    dt = dt[dt.Fighters != '']
    
    dt.sort_values(by = "FighterNumber", inplace = True)
    dt.reset_index(drop = True, inplace = True)
    dt['numWithEcho'] == dt.index
    dt['numNoEcho'] = dt.apply(fighterNumberNoEcho, axis = 1)
    dt.sort_index(inplace = True)
    
    
#--------------------------------scrape images

def scrapeImages():
    global dt
    
    dir = os.path.join('./','','fighterImages')
    if not os.path.exists(dir):
        os.mkdir(dir)
    
    
    #-----------main--------------
    imageLinks = HTML.findAll('div', class_='fighter-list__img', style = True)
    fixImageLinksForFull(imageLinks)

    #Make the folder to save images if it doesn't Exist
    dir = os.path.join('./','fighterImages','main')
    if not os.path.exists(dir):
        os.mkdir(dir)

    for link in imageLinks:
        browser.get('https://www.%s'%(link))
        images = browser.find_elements_by_tag_name('img')
        i = 0
        for image in images:
            imgsrc = image.get_attribute('src')
            name = imgsrc[imgsrc.index('fighter/')+8:-9]
            
            f = open('./fighterImages/main/%s.png'%(name),'wb')
            f.write(requests.get(imgsrc).content)
            i+=1
        f.close()

    #-------------thumb_h----------
    imageLinks = HTML.findAll('div', class_='fighter-list__img', style = True)
    rawNumbers = HTML.findAll('em', class_ = 'fighter-list__num-txt')
    fighterNumbers = []
    for num in rawNumbers:
        if not num.text == '':
            fighterNumbers.append(num.text)


    fixImageLinks(imageLinks)
    
    dir = os.path.join('./','fighterImages','thumb_h')
    if not os.path.exists(dir):
        os.mkdir(dir)
    
    i = 0
    for link in imageLinks:
        browser.get('https://www.%s'%(link))
        images = browser.find_elements_by_tag_name('img')
        
        for image in images:
            imgsrc = image.get_attribute('src')
            fighterName = imgsrc[imgsrc.index('thumb_h/')+8:]
            #print('fighterNumber:',fighterNumbers[i],'is Fighter',fighterName)
            dt.loc[dt['FighterNumber']== fighterNumbers[i], 'filename'] = fighterName
            f = open('./fighterImages/thumb_h/%s'%(fighterName),'wb')
            f.write(requests.get(imgsrc).content)
            i+=1
        f.close()


def init():
    gendt()
    scrapeImages()
    dt.loc[dt["Fighters"] == "POKÉMON TRAINER", "Fighters"] = "POKEMON TRAINER"
    dt.loc[dt["Fighters"] == "POKEMON TRAINER", "FighterNumber"] = "34"
    dt.loc[dt["Fighters"] == "Mii FIGHTER", "FighterNumber"] = "52"
    dt.loc[dt["Fighters"] == "POKEMON TRAINER", "filename"] = "pokemon_trainer.png"
    dt.loc[dt["Fighters"] == "Mii FIGHTER", "filename"] = "mii_fighter.png"
    dt["Echo"] = dt.apply(setEchos, axis = 1)
    dt.to_csv(path_or_buf = "./scrapeData.csv", index = False)

#-----------------------------------Link 2-----------------------------------------------------
#link2 = "https://www.unitstatistics.com/ssbu/"
#browser.get(link2)
#content = browser.execute_script("return document.body.innerHTML")
#HTML = BeautifulSoup(content, "html.parser")
#fighters = HTML.findAll('td',class_="sorting_1")
#getText(fighters)

#dt["Link 2 Data"] = fighters

# Notes
#     I'll need to buffer pokemon trainer and Mii fighter data, or provide catches to not gather Mii Fighter data
#     Idk Ill just have to decide that lol
#     Otherwise the data should play nice but grabbing the tabular data cant be done through class selection so ill have to do it through some other way (Probably array selection)

#-----------------------------------------Link 3----------------------------------------------------
#link3 = https://rankedboost.com/super-smash-bros/mario/
#FOR THIS LINK CHANGE THE END FOR EVERY FIGHTER NAME



init()
#scrapeImages()
#dt.to_csv(path_or_buf='./scrapeData.csv',index = False)

browser.quit()
#----------------------------------------PROGRAM END---------------------------------------------