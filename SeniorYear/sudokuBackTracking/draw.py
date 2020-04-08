import pygame

WIN_HEIGHT = 0
WIN_WIDTH = 0
BOARD_HEIGHT = 0
BOARD_WIDTH = 0


#init colors
col_black = (0,0,0)
col_gray = (100,100,100)
col_white = (255,255,255)
col_green = (0,200,0)
col_red = (200,0,0)
col_blue = (0,0,200)

def draw_init(win_height, win_width, board_height, board_width):
    global WIN_HEIGHT, WIN_WIDTH, BOARD_HEIGHT, BOARD_WIDTH    
    WIN_HEIGHT = win_height
    WIN_WIDTH = win_width
    BOARD_WIDTH = board_width
    BOARD_HEIGHT = board_height
    return pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT), pygame.RESIZABLE)

def set_window_size(width, height, board_width, board_height):
    global WIN_HEIGHT, WIN_WIDTH, BOARD_HEIGHT, BOARD_WIDTH   
    WIN_HEIGHT = height
    WIN_WIDTH = width
    BOARD_WIDTH = board_width
    BOARD_HEIGHT = board_height
    #return pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT), pygame.RESIZABLE)


def drawBoard(win, spaces = None, step_count = '', currTime ='', sidebar=False):
    board = pygame.Surface((BOARD_WIDTH,BOARD_HEIGHT))
    win.fill(col_white)
    board.fill(col_white) #draw bg

    mult = int(BOARD_WIDTH/9) #draw lines
    fntSize = int(mult*.9)
    if spaces is not None:
        for space in spaces: #draw numbers
            space.draw(board,mult,fntSize)
    
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
    
    pos = int((WIN_WIDTH-BOARD_WIDTH)/2)
    if not currTime == '':
        draw_text(win,'Time to Finish: %s'%(currTime),(pos,BOARD_HEIGHT+60))
    if not step_count == '':
        draw_text(win,'Steps Taken: %s'%(step_count),(pos,BOARD_HEIGHT+25))
    win.blit(board,(pos,0))
    
    if sidebar:
        surf = pygame.Surface((mult+10,mult*9+4))
        surf.fill((255,255,255))
        for x in range(10):
            thickness = 1
            if x % 9 == 0:
                thickness = 4
            if x<2:
                pygame.draw.lines(surf, (0,0,0), False, [(x*mult,0),(x*mult,9*mult)], 4)
            pygame.draw.lines(surf, (0,0,0), False, [(0,x*mult),(mult,x*mult)], thickness)
        
        for x in range(10):
            draw_text(surf, str(x), (12, 12+mult*x), fontsize=max(mult-20,10))
        win.blit(surf,(1500,0))

    pygame.display.update()

def draw_text(win, text, pos, fontname='arial', fontsize=25, col=(0,0,0), alpha=255):
    surf = pygame.Surface((int(fontsize*.6*len(text)),int(fontsize)*1.1))
    surf.fill((255,255,255))
    try:
        fnt = pygame.font.SysFont(fontname,fontsize)
    except:
        pygame.font.init()
        fnt = pygame.font.SysFont(fontname,fontsize)
    txt = fnt.render(text, 1, col)
    surf.blit(txt,(0,0))
    surf.set_alpha(alpha)
    win.blit(surf,pos)


def highlightCurrent(win,x,y,mult, alpha, col):
    surf = pygame.Surface((mult,mult))
    surf.fill(col)
    surf.set_alpha(alpha) 
    win.blit(surf,(x*mult,y*mult))

def highlightInList(win,space,mult):
    for spacex in space.quadSpaces:
        highlightCurrent(win, spacex.x,spacex.y,mult,50,col_red)
    for spacex in space.horSpaces:
        highlightCurrent(win, spacex.x,spacex.y,mult,50,col_red)
    for spacex in space.vertSpaces:
        highlightCurrent(win, spacex.x,spacex.y,mult,50,col_red)