import logging
from math import *

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

#-------------------------------------------debug---------------------------------------------------
def debug_printTables(unsolved, possiblySolved):
    print('------------------------------------------------------------------------------------')
    print('The current solved and unsolved lists are')
    print('Unsolved:')
    for s in unsolved:
        print('(%s,%s) '%(s.x,s.y), end='')
    print('\n\nPossibly Solved:')
    for s in possiblySolved:
        print('(%s,%s)'%(s.x,s.y), end='')
    print()
    print('------------------------------------------------------------------------------------')

def debug_printBoard(spaces):
    yprev = 0
    xprev = 0
    for space in spaces:
        print(space.num, end='')
        if floor(xprev/3) != floor(space.x/3):
            print('|',end = ' ')
        if floor(yprev/3) != floor(space.y/3):
            print('\n------------------------')
        yprev = space.y
        xprev = space.x
        #print('Space object at (%s,%s) with num = %s'%(space.x,space.y,space.num))

def debug_spaceInfo(space, x):
    print('----------------------------------------------------------')
    print('Printing info for space number: %s'%(x))
    print('Number: %s'%(space.num))
    print('Position: (%s,%s)'%(space.x,space.y))
    print('Possible list: %s'%(space.possible))
    print('Previous list: %s'%(space.previous))
    print('----------------------------------------------------------')