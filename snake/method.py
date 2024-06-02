import pygame
from variable import *
# Display information of score
def display_score(sco):
    play_screen.fill((255,255,255),(0,0, window_width, information_space))
    information_text = information_font.render("Scores :" + str(sco), True, (0,0,0))
    information_rect = information_text.get_rect(center=(window_width / 2, information_space / 2))
    play_screen.blit(information_text, information_rect)
# Initialize all of window
def screen_init():
    play_screen.fill((255,255,255))
    display_score(0)
    pygame.draw.line(play_screen, (0,0,0), (padding_space, information_space), (padding_space + play_space_size, information_space),1)
    pygame.draw.line(play_screen, (0,0,0), (padding_space, information_space), (padding_space, information_space + play_space_size),1)
    pygame.draw.line(play_screen, (0,0,0), (padding_space + play_space_size, information_space), (padding_space + play_space_size, information_space + play_space_size),1)
    pygame.draw.line(play_screen, (0,0,0), (padding_space , information_space + play_space_size), (padding_space + play_space_size, information_space + play_space_size),1)
# Just initialize the movement space of snake
def play_space_init(): # reset play spaces
    play_screen.fill((255,255,255), (padding_space + 1, information_space + 1, play_space_size - 1, play_space_size - 1))
# Check spawn apple on snake
def apple_not_in_snake(self, cur_x, cur_y):
    if not self:
        return True
    if self.x == cur_x and self.y == cur_y:
        return False
    return apple_not_in_snake(self.next_snake, cur_x , cur_y)
