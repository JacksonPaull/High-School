"""
    In this file I will create the board class, which will be responsible for housing information on board size, where obstacles are, origin, and goal

    Some notable functions to include from the start:
        -Save and load feature
        -Scaling of size
        -Graphical "Create the board"
            -Move tool
                -Usable on all objects 
                    -Origin
                    -Goal
                    -Wall
            -Erase tool
                -Only usable on walls
            -Place tool
                -only usable on walls

        Useful debug/tools
            -Highlight grid segment the mouse is in (for graphical editing and snapping features)
"""
import pygame
from math import *

class Board():
    bg_col = (124, 196, 230)
    line_col = (0,0,0)
    start_col = (0,150,0)
    end_col = (150,0,0)

    def __init__(self, size, node_size):
        self.m = size[0] #Size is a tuple of the form (m,n)
        self.n = size[1] #This indicated rows by columns
        self.node_size = node_size
        self.start_pos = None
        self.end_pos = None
        self.wall_list = []

    def add_wall(self,pos):
        #might want to expand this and possibly add a wall class if I want them to behave differently or something
        if self.wall_list.count(pos) == 0:
            self.wall_list.append(pos)

    def debug_print_board_info(self):
        print('-----------------------[DEBUG] BOARD INFORMATION-----------------------')
        print('board.m: '+str(self.m))
        print('board.n: '+str(self.n))
        print('board.node_size: '+str(self.node_size))
        print('board.start_pos: '+str(self.start_pos))
        print('board.wall_list: '+str(self.wall_list))
        print('\n')

    def draw_board(self, win, pos):
        surf = pygame.Surface((self.node_size*(self.m)+1,self.node_size*(self.n)+1))
        surf.fill(self.bg_col)
        #w, h = surf.get_size()
        maxw = (self.n)*self.node_size
        maxh = (self.m)*self.node_size
        buffer = 100

        for i in range(self.m+1):
            pygame.draw.line(surf, (255,255,255), (0,i*self.node_size), (maxw, i*self.node_size))
        for j in range(self.n+1):
            pygame.draw.line(surf, (255,255,255), (j*self.node_size, 0), (j*self.node_size, maxh))

        if self.start_pos is not None:
            posx = (self.start_pos[0]*self.node_size+1, self.start_pos[1]*self.node_size+1)
            rect = pygame.Rect(posx, (self.node_size-2,self.node_size-2))
            pygame.draw.rect(surf, self.start_col, rect)

        if self.end_pos is not None:
            posx = (self.end_pos[0]*self.node_size+1, self.end_pos[1]*self.node_size+1)
            rect = pygame.Rect(posx, (self.node_size-2,self.node_size-2))
            pygame.draw.rect(surf, self.end_col, rect)
        
        if len(self.wall_list) > 0:
            for wall_pos in self.wall_list:
                posx = (wall_pos[0]*self.node_size+1, wall_pos[1]*self.node_size+1)
                rect = pygame.Rect(posx, (self.node_size-2,self.node_size-2))
                pygame.draw.rect(surf, (0,0,0), rect)

        win.blit(surf,pos)

    def draw_path(self, win, node_list, pos):
        surf = pygame.Surface((self.node_size*(self.m)+1,self.node_size*(self.n)+1))
        surf.fill((255,255,255))
        surf.set_colorkey((255,255,255))
        for x in range(len(node_list)):
            #Convert array pos to center of node on screen pos
            if x < len(node_list)-1:
                node = node_list[x]
                xpos = node[0]*self.node_size+self.node_size/2
                ypos = node[1]*self.node_size+self.node_size/2

                xpos2 = node_list[x+1][0]*self.node_size+self.node_size/2
                ypos2 = node_list[x+1][1]*self.node_size +self.node_size/2

                pygame.draw.line(surf, (0,0,0), (xpos,ypos), (xpos2,ypos2), 1)
        win.blit(surf,pos)
    
