# import pygame
#
# # Constants
# SCORE_COLOR = (255, 255, 255)
# FONT_SIZE = 100
#
# pygame.font.init()
#
#
# class Score:
#     player_score = 0
#     ai_score = 0
#
#     def __init__(self):
#
#         self.font = pygame.font.Font(None, FONT_SIZE)
#
#     def increase_player_score(self):
#         self.player_score += 1
#
#     def increase_ai_score(self):
#         self.ai_score += 1
#
#     def draw_score_player(self):
#         score_text_player = self.font.render(str(self.player_score), True, SCORE_COLOR)
#         return score_text_player
#
#     def draw_score_ai(self):
#         score_text_ai = self.font.render(str(self.ai_score), True, SCORE_COLOR)
#         return score_text_ai
#
#
#
