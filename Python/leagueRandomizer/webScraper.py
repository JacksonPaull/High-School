#-----------------------------------------------------------------------------Links------------------------------------------------------
    #Link 1: https://na.leagueoflegends.com/en/game-info/champions/
        #Can be used to scrape:
            #Full list of champions
            #Champion Icons
            #Then through https://na.leagueoflegends.com/en/game-info/champions/Aatrox/
            #(Replacing the last bit with the newly gathered names)
            #Skins and high rez complete icon
    #Link 2:
        #https://www.mobachampion.com/champion/aatrox-build/
            #Can be used to scrape:
                #Winrate
                #Popularity
                #Ban rate
                #Average KDA
                #Winrate and popularity by lane
                #Synergies
                #Counters
                #Countered By
                #Item Builds
                #Runes against 4 different comps
                #Damage Composition
                #Tips
                #(https://www.mobachampion.com/tier-list/)
                #Champion Tier (Top, above average, average, below average is every unmentioned laner)
                #Portrait style images
                #Grab the primary lane from the image in the champion list (it has alt text I can substring out as well as just take the image)
                #Grab secondary and tertiary lanes from lane popularity for each champion (each has a seperate tier associated, but maintain general counters)


        #Could try pulling from multiple websites and aggregating the data? idk
        #https://app.mobalytics.gg/champions/aatrox/build
        #https://app.mobalytics.gg/lol-tier-list
        #https://u.gg/lol/champions/darius/build




#------------------------------------------------------------------------Info-----------------------------------------------

"""
Todo and planning:


The GUI can be made with pygame, to provide an easier way to place objects and code the visuals as opposed to tkinter, but this can always be reworked

The webdriver should gather the stats enumerated above

goal to randomize champion and skin
based on mastery, lane, enjoyment, hard filter, tier, and playstyle

Once randomized, the menu should show the campion, skin, chroma (if applicable), runes, counters, countered by, starting items, damage comp, tips
Ideally there is a decent UI for changing any of the really modular info, IE champions owned, skins owned, enjoyment, mastery level, etc

Saved data can be split into profile specific and universal data. 
Profile specific data includes
    skins
    champs owned
    mastery
    enjoyment

Universal data includes
    champs in the game
    champ specific data
    skins the champ owns
    etc


"""

#--------------------------------------------------------------Imports-----------------------------------------
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import time

browser = -1 #set global browser variable to be used on everything


def scrape_champions(HTML):
    #Scrapes the name of all champions, then returns that list of champions
    champion_names = []
    champions_names_raw = HTML.findAll('span', class_ = 'style__Text-sc-12h96bu-3 gPUACV')
    for raw in champions_names_raw:
        champion_names.append(raw.text)
    
    return pd.Series(champion_names)


def scrape_mini_splash(HTML): 
    dir = os.path.join('./','championMiniSplashes')
    if not os.path.exists(dir):
        os.mkdir(dir)
    
    #Scrape all img sources
    champion_divider = HTML.find('div', id = '___gatsby').find('section', class_ = 'style__Wrapper-ntddd-0 style__ResponsiveWrapper-ntddd-4 fSyoAt')
    champ_list = champion_divider.findAll('a')
    
    imgs = []
    for champ_div in champ_list:
        source_raw = champ_div.find('img')
        champion = champ_div.find('span', class_='style__Text-sc-12h96bu-3 gPUACV').text
        source = source_raw.get('src')
        img = requests.get(source).content
        filepath = './championMiniSplashes/%s.jpg'%(champion)
        save_image(filepath, img)
        imgs.append(img)
    return pd.Series(imgs)



def save_image(filepath, image):
    f = open(filepath,'wb')
    f.write(image)
    f.close()

def scrape_champion_skins(champion):
    """
    Given the name of a champion,
    scrape
        List of their skins
        Hi rez versions of all splash arts
    """
    global browser
    link = 'https://na.leagueoflegends.com/en/game-info/champions/%s'%(champion)
    browser.get(link)                                                   #Opens link in browser
    content = browser.execute_script("return document.body.innerHTML")   #Returns the inner HTML as a string
    HTML = BeautifulSoup(content, "html.parser")

    skins_div = HTML.findAll('div', class_='style__SlideshowItemImage-sc-1tlyqoa-4 gNgqjZ')
    skin_names_div = HTML.find('div', class_='style__Side-sc-1tlyqoa-6 kcGhQe')
    skin_names = skin_names_div.findAll('li')

    names = []
    images = []

    for x, name in enumerate(skin_names):
        img_src = skins_div[x].find('img').get('src')
        skin_name = name.find('label').text
        img = requests.get(img_src).content
        images.append(img)
        names.append(skin_name)

    number = len(names)

    return names, images, number
    

    #In the dataframe, a column could be named 'Skins" with entries as series
   
def scroll_to_bottom(driver):
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def scrape_champion_stats(champion):
    """
    Scrape all game info about the champion via link two
    """
    global browser
    
    link = "https://u.gg/lol/champions/%s/build"%(champion)
    browser.get(link)                                                   #Opens link in browser
    content = browser.execute_script("return document.body.innerHTML")   #Returns the inner HTML as a string
    HTML = BeautifulSoup(content, "html.parser")

    #TODO need to scrape champion icon, ability icons, item images, and rune images without doubling up

    #Scrape runes

    #Scrape top 6 worst matchups and winrates

    #Scrape winrate pickrate banrate

    #Scrape pref lane

    #Scrape skill priority


    
    link = "https://app.mobalytics.gg/champions/%s/build"%(champion)
    browser.get(link)                                                   #Opens link in browser
    content = browser.execute_script("return document.body.innerHTML")   #Returns the inner HTML as a string
    HTML = BeautifulSoup(content, "html.parser")

    #Scrape damage composition

    #Scrape powerspikes

    #Scrape best lane matchups
    
    #Scrape starting items

    #Scrape core items

    #Scrape vs heavy AD items

    #Scrape vs heavy AP team items

    #Scrape vs general team items


def scrape_tier_list():
    global browser
    
    link = "https://u.gg/lol/tier-list/"
    browser.get(link)
    scroll_to_bottom(browser)                                                   #Opens link in browser
    content = browser.execute_script("return document.body.innerHTML")   #Returns the inner HTML as a string
    HTML = BeautifulSoup(content, "html.parser")

    list_div = HTML.find('div', class_='rt-tbody')

    champ_list = list_div.findAll('div')

    for row in champ_list:
        #Finds all of the information regardless of how the table is sorted.
        #By default it is sorted by winrate
        role = row.find('div', class_ =lambda c: 'rt-td role' in c).find('img').get('alt')
        champion = row.find('div', class_=lambda c: 'rt-td champion' in c).find('Strong').text
        tier = row.find('div', class_=lambda c: 'rt-td tier' in c).find('b').text
        winrate = row.find('div', class_=lambda c: 'rt-td winrate' in c).find('b').text
        banrate = row.find('div', class_=lambda c: 'rt-td banrate' in c).find('b').text
        counter_div_list = row.find('div', class_='against-container').findAll('div', class_='against')
        counters = []
        for counter in counter_div_list:
            champ_link = str(counter.find('a').get('href'))
            start = champ_link.index('/', start=10)+1
            end = champ_link.index('/build')
            champion = champ_link[start,end]
            counters.append(champion)
        




#--------------------------------------Browser-Functions--------------------------------------
def browser_init():
    global browser
    if browser == -1: 
        browser = webdriver.Chrome()


def browser_close():
    global browser 
    browser.quit()
    browser = -1

def string_to_array(string):
    array = []
    word = ''
    for char in string:
        if char == '[' or char == ']' or char =='\'':
            continue
        elif char == ',':
            array.append(word)
            word = ''
        else:
            word = word+char
    
    return array







"""
Notes:

ex of how to parse skins array from df and extract data from it
skins = string_to_array(str(dt.loc[dt['name']==name, 'skins']))
print('The second skin just added was: '+ skins[1])




"""