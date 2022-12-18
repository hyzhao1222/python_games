class Settings:
    def __init__(self):
        self.paddle_size=(10,80)
        self.screen_size=(700,700)
        self.paddle1_init_pos=(80,int(self.screen_size[1]/2))
        self.paddle_color=(255,255,255)
        self.background_color=(0,0,0)
        self.paddle2_init_pos=(self.screen_size[1]-80,int(self.screen_size[1]/2))
        self.paddle_speed=8
        self.ball_size=(20,20)
        self.ball_init_pos=(int(self.screen_size[0]/2),self.paddle2_init_pos[1]-100)
        self.ball_speed=3
        self.ball_color=(255,255,255)