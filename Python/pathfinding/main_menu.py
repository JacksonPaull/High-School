"""
    In this file I will create the main menu of the game as well as display all other aspects of the game.

    Over-arching features:
        -Pathfind from start to finish on variable boards
        -Ability to animate the algorithm
        -Ability to create and modify boards
        -Complete save and load feature
        -Complete menu system
"""

import pygame
import board as b
import aStar
from math import *
import datetime
import timedelta

#import threading
bg_col = (124, 196, 230)
buffer = 100
mouse_held = False

win = pygame.display.set_mode((500,500), pygame.RESIZABLE)
win.fill(bg_col)



board = b.Board((20,20),30)
board.start_pos = (5,5)
board.end_pos = (10,10)
path = None

def draw(win, brd, path = None):
    brd.draw_board(win,(buffer,buffer))
    if path is not None:
        brd.draw_path(win, path, (buffer,buffer))




playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            playing = False
        if event.type == pygame.VIDEORESIZE:
            old_win = win
            win = pygame.display.set_mode((event.w,event.h), pygame.RESIZABLE)
            win.fill(bg_col)
            win.blit(old_win,(0,0))
            board.node_size = min(floor((event.w-2*buffer)/board.n),floor((event.h-2*buffer)/board.m))
            del old_win
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_held = True
            x, y = pygame.mouse.get_pos()
            gridx = floor((x-buffer)/board.node_size)
            gridy = floor((y-buffer)/board.node_size)
            board.add_wall((gridx,gridy))
        if event.type == pygame.MOUSEMOTION and mouse_held:
            x, y = pygame.mouse.get_pos()
            gridx = floor((x-buffer)/board.node_size)
            gridy = floor((y-buffer)/board.node_size)
            board.add_wall((gridx,gridy))
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_held = False
        if event.type == pygame.KEYDOWN:
            start = datetime.datetime.now()
            if event.key == pygame.K_RIGHT:
                board.start_pos = (board.start_pos[0]+1,board.start_pos[1])
                path = aStar.pathfind(board)
            if event.key == pygame.K_LEFT:
                board.start_pos = (board.start_pos[0]-1,board.start_pos[1])
                path = aStar.pathfind(board)
            if event.key == pygame.K_UP:
                board.start_pos = (board.start_pos[0],board.start_pos[1]-1)
                path = aStar.pathfind(board)
            if event.key == pygame.K_DOWN:
                board.start_pos = (board.start_pos[0],board.start_pos[1]+1)
                path = aStar.pathfind(board)
            end = datetime.datetime.now()
            time = end-start
            print('Time to find path: '+str(time)[-9:-7]+'s, '+str(time)[-6:]+'ms')

    draw(win, board, path)
    
    pygame.display.update()








