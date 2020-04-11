import sudoku
import singleplayer
import pygame
import draw

pygame.init()
win = draw.draw_init(1000,1000,900,900)
pygame.display.set_caption('Main Menu')


singleplayer.init(win, 'Singleplayer')
singleplayer.singleplayer()

#sudoku.init(win, 'Gamer')
#sudoku.main_algorithm(False, './board1.txt')



sudoku.init(win, 'Sudoku Algorithm')
sudoku.main_algorithm(False,'./board1.txt')
for x in range(17):
    for letter in ['a','b','c']:
        x = str(x)
        if len(x)!=2:
            x= '0'+x
        filepath = './sudokus/s%s%s.txt'%(x,letter)
        if x == 16:
            filepath = './s16.txt'
        try:
            file = open(filepath, 'r')
            file.close()
            print('----------------------------------------------------')
            print('Attempting to open file: '+filepath)
            sudoku.main_algorithm(False,filepath)
        except:
            print('Opening Failed: file does not exist')
            break
