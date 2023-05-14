import pygame

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 700
START_PLAYER_X = WINDOW_WIDTH - 20
START_PLAYER_Y = WINDOW_HEIGHT - 670
PLAYER_WIDTH = 15
PLAYER_HEIGHT = 60


class Player:
    def __init__(self):
        self.player_pos_x = START_PLAYER_X
        self.player_pos_y = START_PLAYER_Y
        self.player_dim = pygame.Rect(self.player_pos_x, self.player_pos_y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.player_speed = 7

    def check_edge(self):
        if self.player_dim.top <= 0:
            self.player_dim.y = 0

        if self.player_dim.bottom >= WINDOW_HEIGHT:
            self.player_dim.y = WINDOW_HEIGHT - 60

    def player_move(self):
        self.check_edge()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.player_dim.y -= self.player_speed

        if keys[pygame.K_s]:
            self.player_dim.y += self.player_speed
