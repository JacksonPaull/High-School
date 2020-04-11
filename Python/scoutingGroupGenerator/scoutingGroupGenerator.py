import pandas as pd
import random
import math

"""
DOCUMENTATION:
    This program is given a CSV with information about students regarding scouting, then generates 
    a schedule based on games and number of people.

    Somebody is expected to scout if:
        They are not on pit team
        They are not on drive team
        They have no outreach duties that day
        They are at the tournament
        

    1. Gather and clean data
    2. Generate controller groups based on who can conrtol
    3. Generate scouting groups
"""

#!------------------------------------Data table loading and variable generation--------------------!#
dt = pd.read_csv('./data.csv')                                                                       #Define datatable for people from csv, whether they will be expected to scout and whether they can control
#dt = dt[dt["at_______________"]==True].copy()                                                       #selects people from the appropriate tournament
scoutinggtotal = math.floor(len(dt[dt['specialRole']=="none"].index)/6)                              #number of groups wanted (people who are doing nothing but scouting)
controllergtotal = math.floor(len(dt[dt['specialRole']=="Controller"].index)/2)                      #Number of controller groups wanted
numgames = 12                                                                                         #numgames = number of games
maxGamesperGroup = 5                                                                                #maxGames is the most games a group will do at a time
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'                                                              #for use in group naming
dt['group'] = 'none'                                                                                 #automatically set group to none
#!--------------------------------------------------------------------------------------------------!#


#!-----------Generate group of name group, of size group size, and of people from list selectFrom---!#
def randGroup(group, groupSize, selectFrom):
    for index in range(groupSize):                                                                   #puts groupsize amount of people in the group
        selection = random.randint(0,len(selectFrom['name'].index)-1)                                #Select a random non grouped individual
        person = selectFrom.iloc[selection]                                                          #gets data for the selected person
        dt.loc[dt['name'] == person['name'], 'group'] = group                                        #edits the master datatable
        selectFrom.drop(axis = 0, index = selection, inplace = True)                                 #removes selected person from available list
        selectFrom.reset_index(inplace=True, drop = True)                                            #resets list so it can be pulled from again without error
    return selectFrom
#!--------------------------------------------------------------------------------------------------!#

#!Generate schedule from datatable df, number of groups num groups, of size groupsize, and of naming index groupKey----!#
def genSchedule(df, numGroups, groupSize, groupKey):
    selectFrom = df.copy()
    selectFrom.reset_index(inplace=True,drop=True)
    notGrouped = selectFrom
    for index in range(numGroups):                                     #runs an amount of times equal to the amount of groups wanted
        selectFrom = df.copy()
        selectFrom.reset_index(inplace=True,drop=True)
        groupName = "%s Group %s" %(groupKey,alphabet[index:index+1])  #Creates the name wanted
        notGrouped = randGroup(groupName,groupSize,notGrouped)                       #Generates the group and puts it into the master dt
    return None
#!--------------------------------------------------------------------------------------------------------!#

#!--------------------------------------Cleans group name to match special role----------------------------#
def specialGroups(row):
    if(row['specialRole'] not in "none Controller"):
       dt.loc[dt['name'] == row['name'], 'group'] = row['specialRole']
    return None

def gameNum():
    rounds = math.ceil(numgames/maxGamesperGroup)
    for index in range(rounds):
        group = index
        lastRound = index*5+5
        firstRound = index*5+1
        if lastRound>numgames:
            lastRound = numgames
        
        while group>(scoutinggtotal-1):
            group-=scoutinggtotal

        group = alphabet[group]
        roundPerGroup = 'Games (round %s)' %(math.floor(index/scoutinggtotal)+1)
        message = 'Games %s - %s' %(firstRound,lastRound)
        dt.loc[dt['group']== 'Scouting Group %s' %(group), roundPerGroup] = message
        dt.loc[dt['group']== 'Controller Group %s' %(group), roundPerGroup] = message
        dt.loc[dt.index[0], message] = 'Group %s' %(group)
        print('%s: Group %s' %(message,group))
    return None
#-----------------------------------------------------------------------------------------------------------#

#-------------------------------------------Running Fuctions------------------------------------------------#
genSchedule(dt[dt['specialRole']=="none"],scoutinggtotal,6,"Scouting") #Generate Scouting Schedule
genSchedule(dt[dt['specialRole']=="Controller"],controllergtotal,2,"Controller")
dt.apply(specialGroups, axis = 1)
gameNum()
#-------------------------------------------------------------------------------------------------------------#

#-----------------------------------------END OF PROGRAM------------------------------------------------#
dt.to_csv(path_or_buf='data.csv',index=False) #write out new dt