import pygame
import neat
import time
import os
import random
from math import *
import pickle
import visualize

#------------------------------------------------------Globals and Init-------------------------------------------------
pygame.font.init()
WIN_WIDTH = 500  #Window Width
WIN_HEIGHT = 800 #Window Height
GEN = 0
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
STAT_FONT = pygame.font.SysFont('arial',50)
TITLE_FONT = pygame.font.SysFont('arial', 30)

#----------------------------------------------------Import Images and scale--------------------------------------------------------
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("img","bird1.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("img","bird2.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("img","bird3.png")))]

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("img","pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("img","base.png")))
BG_IMG   = pygame.transform.scale2x(pygame.image.load(os.path.join("img","bg.png")))
TITLE_IMG = pygame.image.load(os.path.join('img','title.png'))
SPACE_IMGS = [pygame.image.load(os.path.join('img','human_button1.png')),
                pygame.image.load(os.path.join('img','human_button2.png')),]

ESC_IMGS = [pygame.image.load(os.path.join('img','esc_button1.png')),
                pygame.image.load(os.path.join('img','esc_button2.png')),]

TAB_IMGS = [pygame.image.load(os.path.join('img','ai_button1.png')),
                pygame.image.load(os.path.join('img','ai_button2.png')),]





#------------------------------------------------Bird Object-------------------------------------------------
class Bird:
    IMGS = BIRD_IMGS   #frames for animation
    MAX_ROT = 25       #max rotation
    ROT_VEL = 20       #velocity of rotation
    ANIMATION_TIME = 5 #Frames per img
    animation_step = 1 #direction of animation
    moving = 1         #ability to move
    max_fallspeed = 16 #max dy

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img_num = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0  #time since last jump
        self.height = self.y #Height of last jump start
    
    def move(self):
        self.tick_count += 1
        dy = (self.vel*self.tick_count*self.moving + 1.5*self.tick_count**2)  #Exponential fall rate based on time since flap
        if dy>=self.max_fallspeed:
            dy = self.max_fallspeed
        elif dy<0:
            dy -= 2
        self.y += dy

        if self.y >= 710: #Dont fall past floor
            self.y = 710
        if dy < 0 or self.y < self.height-10: #Dont tilt too far
            if self.tilt < self.MAX_ROT:
                self.tilt = self.MAX_ROT
        else:
            if self.tilt > -70:
                self.tilt -= self.ROT_VEL 

    def draw(self, win):
        if self.img_count >= len(self.IMGS)*self.ANIMATION_TIME-1:
            self.animation_step = -1
            self.img_count-=self.ANIMATION_TIME
        elif self.img_count == 0 and self.animation_step ==-1:
            self.animation_step = 1
            self.img_count +=self.ANIMATION_TIME
        self.img_count+= self.animation_step
        self.img_num = floor(self.img_count/self.ANIMATION_TIME)
        if self.moving:
            self.img = self.IMGS[self.img_num]

        if self.tilt <= -80:
            self.img = self.IMGS[1] #Gliding img when nosediving
            self.img_count = self.ANIMATION_TIME*2 #img_count expected for this img

        rotated_img = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_img.get_rect(center = self.img.get_rect(topleft = (int(self.x), int(self.y))).center)

        win.blit(rotated_img, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)



#----------------------------------------------------------------Pipe Object------------------------------------------------
class Pipe:
    VEL = 5

    def __init__(self,x):
        self.x = x
        self.height = 0 #height of center of gap
        self.gap = 100 #Dist between pipes/2

        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG

        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(150,550)
        self.top = self.height - self.PIPE_TOP.get_height() - self.gap
        self.bottom = self.height + self.gap

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x-bird.x, self.top - round(bird.y))
        bottom_offset = (self.x -bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset) #Returns None or True if collide or not

        if t_point or b_point: #If they collide
            return True
        return False


#-----------------------------------------------------------Ground Object---------------------------------------------------------
class Base:
    VEL = 5
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self,y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))


#-------------------------------------------------------AI Methods-----------------------------------------------------------
def draw_window(win, birds, pipes, base, score, gen): #Draws window
    win.blit(BG_IMG, (0,0))
    for bird in birds:
        bird.draw(win)
    for pipe in pipes:
        pipe.draw(win)
    base.draw(win)

    text = STAT_FONT.render('Score: '+str(score),1,(255,255,255))
    win.blit(text,(WIN_WIDTH-10-text.get_width(),10))

    text = STAT_FONT.render('Gen: '+str(gen),1,(255,255,255))
    win.blit(text,(10,10))

    pygame.display.update()  

def eval_genomes(genomes, config): #Main Game Loop, and fitness function for NEAT
    global GEN, WIN
    win = WIN
    GEN+=1
    nets = []
    ge = [] 
    birds = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230,350))
        g.fitness = 0
        ge.append(g)

    base = Base(WIN_HEIGHT-70)
    pipes = [Pipe(700)]
    clock = pygame.time.Clock()
    score = 0

    running = True
    while running:
        clock.tick(30)
        base.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False #pygame.quit()
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                pass

        pipe_ind = 0
        if len(birds) >0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x+50+pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
        else: #No birds left
            running = False
            break

        for x, bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.1

            #Pass all input neurons, recieve a value for all output neurons
            output = nets[x].activate((bird.y, 
                                        abs(bird.y-pipes[pipe_ind].height-pipes[pipe_ind].gap), 
                                        abs(bird.y-pipes[pipe_ind].height+pipes[pipe_ind].gap)))       

            if output[0] > 0.5:
                bird.jump()

        rem = []
        add_pipe = False
        for pipe in pipes:
            for x, bird in enumerate(birds):
                if pipe.collide(bird):
                    ge[x].fitness -=1
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe =True
            
            if pipe.x + pipe.PIPE_TOP.get_width()<0:
                #Pipe is offscreen
                rem.append(pipe)

            pipe.move()

        for pipe in rem:
            pipes.remove(pipe)

        if add_pipe:
            for g in ge:
                g.fitness +=5
            pipes.append(Pipe(700))
            score +=1

        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_height() > WIN_HEIGHT-70 or bird.y < 0:
                ge[x].fitness -=5
                birds.pop(x)
                ge.pop(x)
                nets.pop(x)
        if score > 10:
            #pickle.dump(nets[0],open("best.pickle", "wb"))
            break;        
        
        draw_window(win, birds, pipes, base, score, GEN)


#----------------------------------------------Universal Methods----------------------------------------------------------
def draw_esc_menu(win, current_screen):
    global WIN_HEIGHT, WIN_WIDTH
    s = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    s.set_alpha(200)
    s.fill((0,0,0))
    win.blit(s, (0,0))
    win.blit(STAT_FONT.render('PAUSED',1,(255,255,255)),(150,50))
    if current_screen == 'main_menu':
        win.blit(TITLE_FONT.render('Press ESC again to quit',1,(255,255,255)),(100,300))
        win.blit(TITLE_FONT.render('Press any to resume',1,(255,255,255)),(100,400))
    elif current_screen == 'human_game':
        pass
    elif current_screen == 'ai_gen':
        pass
    elif current_screen == 'single_ai':
        pass
    pygame.display.update()




#------------------------------------------NEAT--Config-------------------------------------------------
def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, 
                                neat.DefaultReproduction, 
                                neat.DefaultSpeciesSet, 
                                neat.DefaultStagnation, 
                                config_path)
    
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(eval_genomes,50)
    #node_names = { 
    #                '-1':'Bird y-position',
    #                '-2':'Difference in bird y and top pipe',
    #                '-3':'Difference in bird y and bottom pipe'
    #            }
    
    visualize.draw_net(config, winner, view= False) #, node_names=node_names)
    visualize.plot_stats(stats, ylog=False, view=False)
    #visualize.plot_species(stats, view=True)
    pickle.dump(winner,open("best.pickle", "wb"))
    main_menu()
    




#--------------------------------Single Player---------------------------------------------------------------------------
def human_game(menuBird):
    global WIN
    win = WIN
    bird = Bird(menuBird.x,menuBird.y)
    playing = True
    clock = pygame.time.Clock()
    pipes = [Pipe(700)]
    base = Base(730)
    score = 0
    bird.jump()

    while playing:
        clock.tick(30)
        base.move()
        draw_window_human(win, bird, pipes, base, score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False #pygame.quit()
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
                if event.key == pygame.K_ESCAPE:
                    playing = False
                    main_menu()

        bird.move()
        rem = []
        add_pipe = False
        for pipe in pipes:
            if pipe.collide(bird):
                gameOver(bird, pipes, base)

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe =True
            
            if pipe.x + pipe.PIPE_TOP.get_width()<0:
                #Pipe is offscreen
                rem.append(pipe)

            pipe.move()

        for pipe in rem:
            pipes.remove(pipe)

        if add_pipe:
            pipes.append(Pipe(700))
            score +=1

        if bird.y < 0:
            bird.y = 0
        elif bird.y >= 700:
            gameOver(bird, pipes, base)
            
def gameOver(bird, pipes, base):
    bird.moving = 0
    bird.max_fallspeed = 25
    base.VEL = 0
    for pipe in pipes:
        pipe.VEL = 0

def draw_window_human(win, bird, pipes, base, score): #Draws window
    win.blit(BG_IMG, (0,0))
    for pipe in pipes:
        pipe.draw(win)
    bird.draw(win)
    base.draw(win)

    text = STAT_FONT.render('Score: '+str(score),1,(255,255,255))
    win.blit(text,(WIN_WIDTH-10-text.get_width(),10))

    pygame.display.update()

#-------------------------------Race the AI----------------------------------------------------------------------------





#--------------------------------Main Menu------------------------------------------------------------------------------
def draw_main_menu(win, menuBird, pause, buttons):
    win.blit(BG_IMG,(0,0))
    win.blit(TITLE_IMG, (30,30))
    win.blit(BASE_IMG,(0,730))
    for button in buttons:
        button.draw(win)
    for s, pos in [('Single Player',(170,500)), 
                ('Gen AI', (60,300)), 
                ('Pause Menu',(300,300))]:
        text = TITLE_FONT.render(s,1,(255,255,255))
        win.blit(text, pos)
    menuBird.draw(win)

    if not pause:
        pygame.display.update()

class Button():
    animation_time = 20
    img_count = 0

    def __init__(self, imgs, x, y):
        self.imgs = imgs
        self.img = imgs[0]
        self.x = x
        self.y = y

    def draw(self, win):
        self.img_count+=1
        if self.img_count >= self.animation_time * len(self.imgs):
            self.img_count = 0

        self.img = self.imgs[floor(self.img_count/self.animation_time)]

        win.blit(self.img, (self.x, self.y))


class MenuBird():
    imgs = BIRD_IMGS
    animation_time = 5
    time = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img_count = 0
        self.img_num = 0
        self.animation_step = 1
    
    def move(self, time):
        dy = sin(time/10)
        self.time+=1
        self.y+=dy

    def draw(self, win):
        if self.img_count >= len(self.imgs)*self.animation_time-1:
            self.animation_step = -1
            self.img_count-=self.animation_time
        elif self.img_count == 0 and self.animation_step ==-1:
            self.animation_step = 1
            self.img_count +=self.animation_time
        self.img_count+= self.animation_step
        self.img_num = floor(self.img_count/self.animation_time)
        win.blit(self.imgs[self.img_num],(int(self.x), int(self.y)))



def main_menu():
    global WIN
    win = WIN
    menuBird = MenuBird(230,350)
    humanButton = Button(SPACE_IMGS, 30, 500)
    aiButton = Button(TAB_IMGS, 0, 300)
    pauseButton = Button(ESC_IMGS, 300, 300)

    buttons = [humanButton, aiButton, pauseButton]

    on_main = True
    clock = pygame.time.Clock()
    pause = False
    keyUp = True

    while on_main:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_main = False #pygame.quit()
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if pause:
                    pause = not pause
                    if event.key == pygame.K_ESCAPE and keyUp:
                        pygame.quit()
                        quit()
                elif event.key == pygame.K_TAB: ##Change to AI runnning
                    on_main = False
                    local_dir = os.path.dirname(__file__)
                    config_path = os.path.join(local_dir, 'config-feedforward.txt')
                    run(config_path)
                elif event.key == pygame.K_SPACE:
                    on_main = False
                    human_game(menuBird)
                elif event.key == pygame.K_ESCAPE and keyUp:
                    pause = not pause
                    keyUp = False
                elif event.key == pygame.K_RETURN:
                        local_dir = os.path.dirname(__file__)
                        config_path = os.path.join(local_dir, 'config-feedforward.txt')
                        run2(config_path)
                
            if event.type == pygame.KEYUP:
                keyUp = True
            #if event.type == pygame.MOUSEMOTION:
                #Can be used for mouseovers
                #pos = pygame.mouse.get_pos()
                #pass
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #pos = pygame.mouse.get_pos()

        
        menuBird.move(menuBird.time)
        draw_main_menu(win, menuBird, pause, buttons)
        if pause:
            draw_esc_menu(win, 'main_menu')





def run_single_AI(gen, config): #Main Game Loop, and fitness function for NEAT
    global WIN
    try:
        file = open('best.pickle', 'rb')
        best = pickle.load(file)
        file.close()
    except Exception as e:
        print('Cannot load net\nError: '+str(e))
        return None

    win = WIN
    net = neat.nn.FeedForwardNetwork.create(best, config)
    ge = best
    bird = Bird(230,350)

    base = Base(WIN_HEIGHT-70)
    pipes = [Pipe(700)]
    clock = pygame.time.Clock()
    score = 0

    running = True
    while running:
        clock.tick(30)
        #print(clock.get_fps())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False #pygame.quit()
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    main_menu()
                    break

        pipe_ind = 0
   
        if len(pipes) > 1 and bird.x > pipes[0].x+50+pipes[0].PIPE_TOP.get_width():
            pipe_ind = 1

        bird.move()
        output = net.activate((bird.y, 
                                    abs(bird.y-pipes[pipe_ind].height-pipes[pipe_ind].gap), 
                                    abs(bird.y-pipes[pipe_ind].height+pipes[pipe_ind].gap)))       

        if output[0] > 0.5:
            bird.jump()

        base.move()

        rem = []
        add_pipe = False
        for x,pipe in enumerate(pipes):
            if pipe.collide(bird):
                base.VEL = 0
                pipe.VEL = 0
                pipes[x].vel = 0
                bird.moving = -1

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe =True
            
            if pipe.x + pipe.PIPE_TOP.get_width()<0:
                #Pipe is offscreen
                rem.append(pipe)

            pipe.move()

        for pipe in rem:
            pipes.remove(pipe)

        if add_pipe:
            pipes.append(Pipe(700))
            score +=1       
        
        draw_window(win, [bird], pipes, base, score, 0)


def run2(config_path):
    config = neat.config.Config(neat.DefaultGenome, 
                                neat.DefaultReproduction, 
                                neat.DefaultSpeciesSet, 
                                neat.DefaultStagnation, 
                                config_path)
    
    p = neat.Population(config)
    p.run(run_single_AI,1)
    main_menu()

#-----------------Start of program--------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main_menu()










