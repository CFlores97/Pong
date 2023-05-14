import pygame
from ball import Ball

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 700
START_AI_X = WINDOW_WIDTH - 790
START_AI_Y = WINDOW_HEIGHT - 670
AI_WIDTH = 15
AI_HEIGHT = 60

ball = Ball()


class Ai:
    def __init__(self):
        self.ai_pos_x = START_AI_X
        self.ai_pos_y = START_AI_Y
        self.ai_dim = pygame.Rect(self.ai_pos_x, self.ai_pos_y, AI_WIDTH, AI_HEIGHT)
        self.ai_speed = 4

    def check_edge(self):
        if self.ai_dim.top <= 0:
            self.ai_dim.y = 0
            return True

        if self.ai_dim.bottom >= WINDOW_HEIGHT:
            self.ai_dim.y = WINDOW_HEIGHT - 60
            return True

    def ai_move(self):

        if self.ai_dim.centery < ball.ball_dim.centery:
            self.ai_dim.centery += self.ai_speed

        if self.ai_dim.centery > ball.ball_dim.centery:
            self.ai_dim.centery -= self.ai_speed

        self.check_edge()

