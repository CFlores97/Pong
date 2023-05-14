import pygame
from ball import Ball, BALL_COLOR
from player import Player
from ai import Ai

# constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 700
BG_COLOR = (0, 0, 0)
MAIN_COLOR = (255, 255, 255)
FONT_SIZE = 100
PLAYER_SCORE_POS = (WINDOW_WIDTH // 2 + 30, WINDOW_HEIGHT - 680)
AI_SCORE_POS = (WINDOW_WIDTH // 2 - 75, WINDOW_HEIGHT - 680)

pygame.init()
pygame.font.init()

# window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong game")
clock = pygame.time.Clock()

# objects
ball = Ball()
player = Player()
ai = Ai()

# score
player_score = 0
ai_score = 0

font = pygame.font.Font(None, FONT_SIZE)

# time
time = 60


def collision():
    global time
    collide_player = pygame.Rect.colliderect(ball.ball_dim, player.player_dim)
    collide_ai = pygame.Rect.colliderect(ball.ball_dim, ai.ai_dim)

    if collide_player or collide_ai:
        ball.speed_x *= -1
        time += ball.move_speed


running = True
has_scored = False

while running:

    new_player_score = 0
    new_ai_score = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw on screen
    window.fill(BG_COLOR)
    ball.move_ball()
    ai.ai_move()
    player.player_move()
    collision()

    pygame.draw.aaline(window, MAIN_COLOR, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT))
    pygame.draw.ellipse(window, BALL_COLOR, ball.ball_dim)
    pygame.draw.rect(window, MAIN_COLOR, player.player_dim)
    pygame.draw.rect(window, MAIN_COLOR, ai.ai_dim)

    if ball.ball_dim.left <= 0:
        player_score += 1
        ai.ai_speed += 0.5
        time = 60
        ball.reset_ball()

    elif ball.ball_dim.right >= WINDOW_WIDTH:
        ai_score += 1
        time = 60
        ball.reset_ball()

    score_text_player = font.render(str(player_score), True, MAIN_COLOR)
    score_text_ai = font.render(str(ai_score), True, MAIN_COLOR)

    window.blit(score_text_player, PLAYER_SCORE_POS)
    window.blit(score_text_ai, AI_SCORE_POS)
    print(time)

    pygame.display.update()
    clock.tick(time)
