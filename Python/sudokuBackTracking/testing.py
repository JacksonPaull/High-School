import pygame
from math import *


class movableObject():
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
        self.fontsize = 75
        self.held = False

    def draw(self, win, fontname='arial', fontsize=75):
        if fontsize != self.fontsize:
            self.fontsize = fontsize
        try:
            fnt = pygame.font.SysFont(fontname,fontsize)
        except:
            pygame.font.init()
            fnt = pygame.font.SysFont(fontname,fontsize)
        txt = fnt.render(str(self.num), 1, (0,0,0))
        
        self.update()
        win.blit(txt, (self.x,self.y))

    def update(self):
        if self.held:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            self.x = int(mouse_x-num.fontsize*9/32)
            self.y = int(mouse_y-num.fontsize/2)
    
    def snapToGrid(self, grid, mult):
        x = int(self.x + self.fontsize*9/32)
        y = int(self.y + self.fontsize/2)
        self.x = floor((x - grid.x)/mult)*mult + grid.x +  int(self.fontsize*9/32)
        self.y = floor((y - grid.y)/mult)*mult + grid.y + int(self.fontsize/4)

class grid():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self, win):
        col_black = (0,0,0)

        board = pygame.Surface((900,900))
        board.fill((255,255,255))
        mult = int(100) #draw lines
        fntSize = int(mult*.9)
        
        #draw border
        for x in range(10):
            thickness = 1
            length = 0
            if x % 3 == 0:
                thickness = 4
                if x == 9:
                    length = thickness-2
            pygame.draw.lines(board, col_black, False, [(x*mult,0),(x*mult,int(mult*9))],thickness)
            pygame.draw.lines(board, col_black, False, [(0,x*mult),((mult*9+length),x*mult)],thickness)
        win.blit(board,(self.x,self.y))




def draw(win):
    win.fill((255,255,255))
    


pygame.init()
win = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Main Menu')


testing = True
num = movableObject(75,50,9)
grid = grid(50,50)
while testing:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            testing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            if mouse_x in range(num.x,ceil(num.x+num.fontsize*9/16)):
                if mouse_y in range(num.y,num.y+num.fontsize):
                    num.held = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            if mouse_x in range(num.x,ceil(num.x+num.fontsize*9/16)):
                if mouse_y in range(num.y,num.y+num.fontsize):
                    num.held = False
                    num.snapToGrid(grid, 100)
            
    draw(win)  
    grid.draw(win)
    num.draw(win)
    pygame.display.update()
        
