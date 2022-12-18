import pygame,sys,random
from pygame.locals import *
from settings import Settings
from score import Score
from middleline import MiddleLine
pygame.init()
pygame.display.set_caption('ballgame')
screen=pygame.display.set_mode(Settings().screen_size)
class Paddle1:
    def __init__(self,screen):
        global pos1,size1
        self.settings=Settings()
        self.pos=self.settings.paddle1_init_pos
        self.size=self.settings.paddle_size
        pos1=self.pos
        size1=self.size
        self.screen_size=self.settings.screen_size
        self.rect=pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        self.screen=screen
        self.color=self.settings.paddle_color
        self.speed=self.settings.paddle_speed
    def move(self):
        keypress=pygame.key.get_pressed()
        if keypress[K_w]:
            if not self.rect.y<=0:
                self.rect.y-=self.speed
        if keypress[K_s]:
            if not self.rect.y>=self.screen_size[1]-self.size[1]:
                self.rect.y+=self.speed
    def update_posy(self):
        global pos1y
        pos1y=self.rect.y
class Paddle2:
    def __init__(self,screen):
        global pos2,size2
        self.settings=Settings()
        self.pos=self.settings.paddle2_init_pos
        self.size=self.settings.paddle_size
        pos2=self.pos
        size2=self.size
        self.screen_size=self.settings.screen_size
        self.rect=pygame.Rect(self.pos[0]+self.size[0],self.pos[1],self.size[0],self.size[1])
        self.screen=screen
        self.color=self.settings.paddle_color
        self.speed=self.settings.paddle_speed
    def move(self):
        keypress=pygame.key.get_pressed()
        if keypress[K_UP]:
            if not self.rect.y<=0:
                self.rect.y-=self.speed
        if keypress[K_DOWN]:
            if not self.rect.y>=self.screen_size[1]-self.size[1]:
                self.rect.y+=self.speed
    def update_posy(self):
        global pos2y
        pos2y=self.rect.y
class Ball:
    def __init__(self,screen):
        self.settings=Settings()
        self.score1,self.score2=0,0
        self.gameover=False
        self.pos=self.settings.ball_init_pos
        self.size=self.settings.ball_size
        self.screen_size=self.settings.screen_size
        self.rect=pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        self.screen=screen
        self.color=self.settings.ball_color
        self.speed=self.settings.ball_speed
        self.way=random.choice(['left','left'])
        self.yway=random.choice(['up','down'])
    def move(self):
        self.move_left_right()
        self.move_up_down()
        self.check_hit_edge()
        self.check_hit_paddle()
    def check_game_over(self):
        if self.rect.left<=0:
            self.gameover=True
        elif self.rect.right>=self.settings.screen_size[0]:
            self.gameover=True
        return self.gameover
    def check_hit_paddle(self):
        if self.rect.left==pos1[0]:
            if self.rect.bottom>=pos1y and self.rect.top<=pos1y+size1[1]:
                self.way='right'
                self.score1+=1
        elif self.rect.left==pos2[0]:
            if self.rect.bottom>=pos2y and self.rect.top<=pos2y+size2[1]:
                self.way='left'
                self.score2+=1
    def check_hit_edge(self):
        if self.rect.top<=0:
            self.yway='down'
        elif self.rect.bottom>=self.settings.screen_size[1]:
            self.yway='up'
    def move_left_right(self):
        if self.way=='left':
            self.rect.x-=self.speed
        elif self.way=='right':
            self.rect.x+=self.speed
    def move_up_down(self):
        if self.yway=='up':
            self.rect.y-=self.speed
        elif self.yway=='down':
            self.rect.y+=self.speed
paddle1=Paddle1(screen)
paddle2=Paddle2(screen)
scoreboard=Score(screen)
ball=Ball(screen)
clock=pygame.time.Clock()
middleline=MiddleLine(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(Settings().background_color)
    if not ball.check_game_over():
        pygame.draw.rect(paddle1.screen,paddle1.color,paddle1.rect)
        pygame.draw.rect(paddle2.screen,paddle2.color,paddle2.rect)
        pygame.draw.ellipse(screen,ball.color,ball.rect)
        middleline.draw()
        scoreboard.show1(ball.score1)
        scoreboard.show2(ball.score2)
        paddle1.move()
        paddle1.update_posy()
        paddle2.move()
        paddle2.update_posy()
        ball.move()
        pygame.display.update()
        clock.tick(80)