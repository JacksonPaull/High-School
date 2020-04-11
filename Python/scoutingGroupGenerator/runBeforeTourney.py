"""
THIS FILE IS INTENDED TO SPIT OUT A LIST OF PEOPLE WHO AREN'T TRAINED BUT ARE PLANNING ON GOING TO TOURNEY
SO THAT THEY CAN BE TRAINED
"""

import pandas as pd
import random
import math

dt = pd.read_csv("./data.csv")
def main(tourney):
    print(dt[dt["trained"]==False and dt["atT%s" %(tourney)]==True])

if(len(dt[dt["trained"]==False])!=0):
    print("What tourney are you checking?")
    num = input()
    if(num>0 and num<5 and num%1 == 0):
        main(num)
else:
    print("Everyone is trained")