from pygame import Color
import pygame.font
from settings import Settings
class Score:
    def __init__(self,screen):
        self.screen=screen
        self.font=pygame.font.Font('freesansbold.ttf', 20)
    def show1(self,score):
        self.score1=score
        self.screen.blit(self.font.render(str(self.score1),1,Color(255,255,255)),(Settings().screen_size[0]/2-20,10))
    def show2(self,score):
        self.score2=score
        self.screen.blit(self.font.render(str(self.score2),1,Color(255,255,255)),(Settings().screen_size[0]/2+20,10))
if __name__=='__main__':
    print('Debug=True')