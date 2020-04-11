#some example solvable puzzles can be found @ https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html
#generator can be found @ https://qqwing.com/generate.html

#-------------------------------------Imports----------------------------------------
import pygame          #Used for game functions
from math import *     #Used for general math

import time            #Used for animation
import threading       #Used for animation
#import logging        #Used for debugging threads

import datetime        #Used for timer
import timedelta       #Used for timer
from draw import *
from debug import *


#---------------------------------init--------------------------------

win = None
def init(WIN, caption):
    global win
    win = WIN
    pygame.display.set_caption(caption)


#---------------------------------------Space class----------------------------------------
class Space():
    
    given = False
    alpha = 255

    def __init__(self, x, y, num):
        self.previous = []
        self.possible = []
        self.x = x
        self.y = y
        self.num =  num
        self.quad = floor(self.y/3)*3+floor(self.x/3)
        if num != ' ':
            self.given = True
            self.col = col_black
        else:
            self.col = (0,100,0)
        
        
    def initLists(self, spaces):
        self.quadSpaces = []
        self.vertSpaces = []
        self.horSpaces = []
        for space in spaces:
            if space == self:
                pass
            else:
                if space.quad == self.quad:
                    self.quadSpaces.append(space)
                if space.x == self.x:
                    self.vertSpaces.append(space)
                if space.y == self.y:
                    self.horSpaces.append(space)

    def findPossibleNums(self, spaces):
        possible = [i for i in range(1,10)]

        for space in self.quadSpaces:
            if space.num in possible:
                possible.remove(space.num)

        for space in self.vertSpaces:
            if space.num in possible:
                possible.remove(space.num)

        for space in self.horSpaces:
            if space.num in possible:
                possible.remove(space.num)

        for num in self.previous:
            if num in possible:
                possible.remove(num)

        self.possible = possible


    def attemptSolve(self, spaces, backtracking):
        self.findPossibleNums(spaces)
        success = False
        multiplePossible = False
        noPossible = False
        if not backtracking:
            if len(self.possible) == 1:
                self.col = col_green
                self.num = self.possible[0]
                self.alpha = 255
                success = True     
            else:
                self.col = col_gray
                self.alpha = 75
                self.num = '?'
                
                if len(self.possible) >1:
                    multiplePossible = True
                elif len(self.possible) == 0:
                    noPossible = True
        else:
            if len(self.possible)>1:
                self.col = col_blue
                self.num = self.possible[0]
                self.alpha = 255
                success = True
                self.previous.append(self.num)
            elif len(self.possible)==1:
                self.col = col_green
                self.num = self.possible[0]
                self.alpha = 255
                success = True
                self.previous.append(self.num)
            elif len(self.possible)==0:
                noPossible = True     

        return (success, multiplePossible, noPossible)     


    def draw(self, win, mult, fntSize):
        #draws self text
        draw_text(win,str(self.num),(int(self.x*mult+mult*0.25),int(self.y*mult+mult*0.05)),fontsize=fntSize, col = self.col, alpha = self.alpha)




#--------------------------------------Threading-------------------------------------------------------
waiting = True
def wait(seconds):
    #logging.info('Starting Wait')
    time.sleep(seconds)
    global waiting
    waiting = False
    #logging.info('ending wait')




#------------------------General functions-------------------------------------------------------
def loadBoard(filepath):
    x = y = 0
    spaces = []
    unsolved = []
    possiblySolved = []

    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()
    for line in lines:
        for char in line:
            if char == '\n':
                y += 1
                x = 0
                break
            elif char == ' ':
                pass
            else:
                if char == '0':
                    space = Space(x,y,' ')
                else:
                    space = Space(x,y, int(char))
                spaces.append(space)
                if not space.given:
                    unsolved.append(space)
                x+=1
          
    for space in spaces: #needs to be done after all spaces are complete
        space.initLists(spaces)

    return (spaces, unsolved, possiblySolved)
        


def writeSolution(spaces, filepath):
    yprev = 0
    output = ''
    for space in spaces:
        if space.y != yprev:
            output+='\n'
        output += str(space.num)+' '
        yprev = space.y
    
    file = open(filepath, 'w')
    file.write(output)
    file.close()



def solve(spaces, unsolved, possiblySolved, cnt, backtracking, step_count, mult_count):
    if cnt<len(unsolved) and cnt>=0:
        space = unsolved[cnt]

        success, multiplePossible, noPossible = space.attemptSolve(spaces, backtracking)
        
        if success:
            possiblySolved.append(unsolved.pop(cnt))
            cnt-=1
            mult_count = 0
        elif noPossible:
            #not starting on the one I want it to start on
            space.num = '?'
            space.col = col_gray
            space.alpha = 75
            space.previous = []
            incorrect = possiblySolved.pop()
            incorrect.num = '?'
            incorrect.col = col_gray
            incorrect.alpha = 75
            unsolved.insert(cnt,incorrect)
            cnt-=2
            backtracking = True
        elif multiplePossible:
            mult_count += 1
        cnt += 1

        if mult_count == len(unsolved):
            backtracking = True
            mult_count = 0
        if cnt == len(unsolved):
            cnt=0
            mult_count = 0
        step_count+=1
    else:
        cnt = 0
    return spaces, unsolved, possiblySolved, cnt, backtracking, step_count, mult_count







#-----------------------------------------main Algorithm and game loop-----------------------------------------
def main_algorithm(animating, board_path, step_time=0.1 ):
    #UI variables
    waiting = True
    step_count = 0
    cnt = 0 # used for animation
    currTime = '0'
    timer = False
    running = True

    #Algorithm Variables
    backtracking = False
    mult_count = 0
    spaces, unsolved, possiblySolved = loadBoard(board_path)

    while running:  #game loop
        global win, WIN_HEIGHT, WIN_WIDTH, BOARD_WIDTH, BOARD_HEIGHT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                    if not timer:
                        start = datetime.datetime.now()
                    timer = True     
                elif event.key == pygame.K_RETURN:
                    writeSolution(spaces,'./solution.txt')
                elif event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.VIDEORESIZE:
                old = win
                win = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                win.blit(old,(0,0))
                WIN_HEIGHT = event.h
                WIN_WIDTH = event.w
                BOARD_HEIGHT = BOARD_WIDTH = min(event.h-100,event.w-50)
                del old

        if animating:
            if not waiting:
                if step_time == -1:
                    waiting = True         
                if step_time>0:
                    waitThread = threading.Thread(target=wait, args=(step_time,))
                    waitThread.start()
                
                spaces, unsolved, possiblySolved, cnt, backtracking, step_count, mult_count = solve(spaces, unsolved, possiblySolved, cnt, backtracking, step_count, mult_count)
                if len(unsolved) == 0:
                    #game is done
                    animating = False
            if timer:
                end = datetime.datetime.now()
                delta = (end-start)
                currTime = str(delta)#[:-3]       
            drawBoard(win, spaces, step_count, currTime)

        else:
            #not animating          
            if waiting:
                drawBoard(win, spaces, step_count, currTime)
            else:           
                spaces, unsolved, possiblySolved, cnt, backtracking, step_count, mult_count = solve(spaces, unsolved, possiblySolved, cnt, backtracking, step_count, mult_count)
                if len(unsolved) == 0:
                    #game is done
                    end = datetime.datetime.now()
                    delta = (end-start)
                    currTime = str(delta)#[:-3]
                    waiting = True
                    
            
            
            
            


