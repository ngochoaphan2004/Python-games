import pygame
import pygame.freetype

pygame.init()
# Mode game
difficult = 0.3
# Size of all frame
size = 30
information_space = 50
padding_space = 20
play_space_size = 600
block_size = play_space_size / size
block_size_padding = 0.06 * block_size
snake_body_size = block_size - 2 * block_size_padding
window_width = play_space_size + 2 * padding_space 
window_height = play_space_size + information_space + padding_space
# Font, size, text and rect
working_path = "D:\\Code\\Python\\code_games\\snake\\dist\\"
failed_font = pygame.font.Font(working_path + "Typographica-Blp5.ttf",50)
restart_font = pygame.font.Font(working_path + "Typographica-Blp5.ttf",20)
information_font = pygame.font.Font(working_path + "Typographica-Blp5.ttf",20)
failed_text = failed_font.render("Game over", True, (0,0,0))
restart_text = restart_font.render("press space to restart", True, (0,0,0))  
information_font.render
# Apple load
apple_icon = pygame.image.load(working_path + "apple_image.png")
apple_icon = pygame.transform.scale(apple_icon,(snake_body_size - block_size_padding, snake_body_size - block_size_padding))
# Initialize screen and clock        
play_screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
