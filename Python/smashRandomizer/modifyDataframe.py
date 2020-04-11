import pandas as pd

dt = pd.read_csv('./scrapeData.csv', index_col=0)

"""def setEchos(row):                                                   #Used to document where the echos are
    global dt
    if("ᵋ" in row["FighterNumber"]):
        index = dt[dt["FighterNumber"]==row["FighterNumber"]].index.values[0]
        return "Echo Fighter of %s" %(dt.iloc[index-1]["Fighters"])
    return 'notEcho'

dt['Echo'] = dt.apply(setEchos, axis = 1)"""


"""dt.sort_values(by = "FighterNumber", inplace = True)
dt.reset_index(drop = True, inplace = True)
dt['numWithEcho'] = dt.index+1
dt.sort_index(inplace = True)"""

dt.loc[dt["Fighters"] == "POKEMON TRAINER", "FighterNumber"] = "34"
dt.loc[dt["Fighters"] == "Mii FIGHTER", "FighterNumber"] = "52"
dt.sort_values(by='FighterNumber',inplace = True)

def numNoEcho(row):                                        #Used to reset fighter number without the echo
    number = row["FighterNumber"][:2]                                #This is because I can use the regular index as the echo fighter inclusion index
    return number 

dt['numNoEcho'] = dt.apply(numNoEcho,axis = 1)

dt.to_csv(path_or_buf='./scrapeData.csv', index = False)