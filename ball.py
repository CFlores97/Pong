import pygame
import random

# CONSTANTS
BALL_WIDTH, BALL_HEIGHT = 20, 20
BALL_COLOR = (69, 139, 116)
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 700
START_X = WINDOW_WIDTH / 2 - 10
START_Y = WINDOW_HEIGHT / 2 - 10


class Ball:
    ball_x_pos = START_X
    ball_y_pos = START_Y
    ball_dim = pygame.Rect(ball_x_pos, ball_y_pos, BALL_WIDTH, BALL_HEIGHT)

    def __init__(self):
        self.speed_x = 6 * random.choice((1, -1))
        self.speed_y = 6 * random.choice((1, -1))
        self.move_speed = 5

    def reset_ball(self):
        self.ball_dim.x = START_X
        self.ball_dim.y = START_Y
        self.speed_x *= random.choice((1, -1))
        self.speed_y *= random.choice((1, -1))

    def move_ball(self):
        self.ball_dim.x += self.speed_x
        self.ball_dim.y += self.speed_y

        # detects collisions with edges
        if self.ball_dim.top <= 0 or self.ball_dim.bottom >= WINDOW_HEIGHT:
            self.speed_y *= -1
