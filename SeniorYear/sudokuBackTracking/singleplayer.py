import pygame
import draw

win = None
def init(WIN, caption):
    global win
    win = WIN
    pygame.display.set_caption(caption)

class number():
    def __init__(self, num):
        self.num = num
        self.x = 0
        self.y = num - 1




def singleplayer():
    
    global win
    running = True

    while running:  #game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    """if event.key == pygame.K_TAB:
                        BOARD_HEIGHT = BOARD_WIDTH = min(500-100,500-50)
                        draw.set_window_size(500,500, BOARD_HEIGHT, BOARD_WIDTH)
                        win = pygame.display.set_mode((500,500), pygame.RESIZABLE)"""
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        break
                if event.type == pygame.VIDEORESIZE:
                    old = win
                    win = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    win.blit(old,(0,0))
                    WIN_HEIGHT = event.h
                    WIN_WIDTH = event.w
                    BOARD_HEIGHT = BOARD_WIDTH = min(event.h-100,event.w-50)
                    draw.set_window_size(WIN_WIDTH,WIN_HEIGHT, BOARD_HEIGHT, BOARD_WIDTH)
                    del old

            draw.drawBoard(win, sidebar=True)

            