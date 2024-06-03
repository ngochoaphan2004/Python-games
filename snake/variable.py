import pygame
import pygame.freetype

pygame.init()
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
failed_font = pygame.font.Font("dist\\Typographica-Blp5.ttf",50)
restart_font = pygame.font.Font("dist\\Typographica-Blp5.ttf",20)
information_font = pygame.font.Font("dist\\Typographica-Blp5.ttf",20)
failed_text = failed_font.render("Game over", True, (0,0,0))
restart_text = restart_font.render("press space to restart", True, (0,0,0))  
# Sound load
eat_apple_sound = pygame.mixer.Sound("dist\\coin_earning.wav")
eat_apple_sound.set_volume(0.5)
snake_hit_wall = pygame.mixer.Sound("dist\\snake_hit_wall.wav")
back_ground_music = pygame.mixer.Sound("dist\\game_background_sound.wav")
back_ground_music.set_volume(0.8)
# Apple load
apple_icon = pygame.image.load("dist\\apple_image.png")
apple_icon = pygame.transform.scale(apple_icon,(snake_body_size - block_size_padding, snake_body_size - block_size_padding))
# Initialize screen and clock        
play_screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("PySnake")
clock = pygame.time.Clock()
