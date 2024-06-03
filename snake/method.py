import pygame, sys
from variable import *

# Home screen init
def home_screen_init():
    play_screen.fill((255,255,255))
    game_title = failed_font.render("SnakePy", True,(0,0,0))
    game_title_rect = game_title.get_rect(center=(window_width/2, window_height/2))
    play_screen.blit(game_title, game_title_rect)
    game_info = restart_font.render("Press any key to continue", True, (0,0,0))
    game_info_rect = game_info.get_rect(center=(window_width/2, window_height/2 + 50))
    play_screen.blit(game_info, game_info_rect)
# Home screen loop
def home_screen_loop():
    home_screen = True
    home_screen_init()
    back_ground_music.play(-1)
    pygame.display.update()
    while home_screen:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                home_screen = False
                back_ground_music.set_volume(0.3)
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
