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




#------------------------------------------------------------------------Info-----------------------------------------------


#--------------------------------------------------------------Imports-----------------------------------------
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

