"""
THIS FILE IS INTENDED TO PARSE THE RESPONSES FROM THE GOOGLE FORM TO WORK WITH THE SCRIPT.
IMPORT THIS FILE AND RUN THE SINGLE FUNCTION LMAO
"""

import pandas as pd
dt = pd.read_csv('./rawData.csv')

dt.rename(columns = {'Name (first last)':'name',
                    'Which team are you on?':'team', 
                    'What grade are you in?':'grade',
                    'Any special role at competition (can be changed later)':'specialRole',
                    'Have you been trained to scout yet? (for 2020 season)':'trainedScout',
                    'Would you like to be trained to control? (This does not guarantee you a role as a controller)':'controllerInterest',
                    'Which tournaments do you plan on going to? (This can be changed later don\'t worry)':'tourneysAt',
                    'What is your email?':'email',
                    'Have you already been trained to control? (2020 season)':'trainedControl'})


#trained
dt['trained'] = False
dt.loc['specialRole'=='none' and 'trainedScout'=='Yes','trained'] = True
dt.loc['specialRole'=='controller' and 'trainedController'=='Yes','trained'] = True


#atT__
dt.loc['Greenville' in 'tourneysAt', 'atT1'] == True
dt.loc['Vandegrift' in 'tourneysAt', 'atT2'] == True
dt.loc['District' in 'tourneysAt', 'atT3'] == True
dt.loc['World' in 'tourneysAt', 'atT4'] == True


dt = dt['name','specialRole','trained','atT1','atT2','atT3','atT4'].copy()

pd.to_csv('./data',index = False)