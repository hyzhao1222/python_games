import pygame.draw
from settings import Settings
class MiddleLine:
    def __init__(self,screen):
        self.settings=Settings()
        self.screen=screen
    def draw(self):
        pygame.draw.line(self.screen,(255,255,255),(self.settings.screen_size[0]/2+2,0),(self.settings.screen_size[0]/2+2,self.settings.screen_size[1]),2)
if __name__=='__main__':
    print('Debug=True')