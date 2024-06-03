import pygame, sys
import random
from method import *
home_screen_loop()
# Mode game
difficult = 0.3   
# Game variables
score = 0

pre_move = True
right_move = True
left_move = False
up_move = False
down_move = False

failed = False
reset = False
list_snake_body = None  
snake_run_counter = 0.0001
tail_snake = None
# Apple variable
apple_init = True
apple_x = 0
apple_y = 0
# Class of snake information
class snake_body:
    x = None
    y = None
    next_snake = None
    def __init__(self, x_in, y_in, next = None):
        self.x = x_in
        self.y = y_in
        self.next_snake = next
    # Add new tail
    def add(self):
        if self == None:
            return
        if self.next_snake == None:
            self.next_snake = snake_body(tail_snake.x, tail_snake.y)
        else: 
            self.next_snake.add()
    # Check exist value
    def exits(self, cur_x, cur_y):
        if self == None:
            return False
        if self.x == cur_x and self.y == cur_y:
            return True
        if self.next_snake == None:
            return False
        return self.next_snake.exits(cur_x, cur_y)
    # Find way the previous body of snake to move
    def pre_body_move_to(seft, move):
        if seft.next_snake == None:
            return move
        if seft.next_snake.x > seft.x:
            return 'l'
        elif seft.next_snake.x < seft.x:
            return 'r'
        elif seft.next_snake.y > seft.y:
            return 'u'
        elif seft.next_snake.y < seft.y:
            return 'd'
    # Increase x or y when snake moving
    def snake_increase_value(self, move):
        global failed
        match move:
            case 'u':
                if self.y <= 0:
                    failed = True
                    return
                self.y -= 1
            case 'd':
                if self.y >= size - 1:
                    failed = True
                    return
                self.y += 1
            case 'l':
                if self.x <= 0:
                    failed = True
                    return
                self.x -= 1
            case 'r':
                if self.x >= size - 1:
                    failed = True
                    return
                self.x += 1

# Reset linked list snake and draw it on screen
def snake_init():
    global list_snake_body, tail_snake
    list_snake_body = snake_body(2,0,snake_body(1,0,snake_body(0,0)))
    tail_snake = snake_body(0,0)
    play_screen.fill((125,125,125), (padding_space + block_size_padding , information_space + block_size_padding, snake_body_size, snake_body_size))
    play_screen.fill((125,125,125), (padding_space + block_size_padding + 1 * block_size, information_space + block_size_padding, snake_body_size, snake_body_size))
    play_screen.fill((125,125,125), (padding_space + block_size_padding + 2 * block_size, information_space + block_size_padding, snake_body_size, snake_body_size))
# Movement of snake
def snake_movement(default_value):
    global tail_snake, failed
    play_space_init()
    body = list_snake_body
    move = default_value
    tail_x = -1
    tail_y = -1
    while body != None:
        tail_x = body.x
        tail_y = body.y
        pre_move = body.pre_body_move_to(move)
        body.snake_increase_value(move)
        play_screen.fill((125,125,125), (padding_space + block_size_padding + body.x * block_size, information_space + block_size_padding + body.y * block_size, snake_body_size, snake_body_size))
        move = pre_move
        body = body.next_snake
    if list_snake_body.next_snake.exits(list_snake_body.x, list_snake_body.y):
        failed = True
    tail_snake.x = tail_x
    tail_snake.y = tail_y
# Apple init
def apple_init_random():
    check = True
    while check:
        x = random.randint(0, size - 1) 
        y = random.randint(0, size - 1)
        check = not apple_not_in_snake(list_snake_body, x, y)
    return x, y
# Check snake eat apple
def is_snake_ate_apple():
    global apple_x, apple_y, score
    if list_snake_body.x == apple_x and list_snake_body.y == apple_y:
        apple_x, apple_y = apple_init_random()
        list_snake_body.add()

        eat_apple_sound.play()
        score += 1
        display_score(score)
    else:
        play_screen.blit(apple_icon, (padding_space + apple_x * block_size, information_space + apple_y * block_size))
    

screen_init()
snake_init()
apple_x , apple_y = apple_init_random()
while True:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            back_ground_music.stop()
            pygame.quit()
            sys.exit()
        elif event.type ==  pygame.KEYDOWN and pre_move:
            if not reset:
                match event.key:
                    case pygame.K_a:
                        if not right_move and not left_move:

                            pre_move = False
                            left_move = True
                            right_move = up_move = down_move = False
                    case pygame.K_d:
                        if not left_move and not right_move:

                            pre_move = False
                            right_move = True
                            left_move = up_move = down_move = False
                    case pygame.K_w:
                        if not down_move and not up_move:

                            pre_move = False
                            up_move = True
                            right_move = left_move = down_move = False
                    case pygame.K_s:
                        if not up_move and not down_move:

                            pre_move = False
                            down_move = True
                            right_move = up_move = left_move = False
            elif event.key == pygame.K_SPACE:
                screen_init()
                snake_init()
                apple_x , apple_y = apple_init_random()
                snake_run_counter = -100000.1
                score = 0
                reset = False
                right_move = True
                left_move = up_move = down_move = False

    # Movement of snake
    if not reset:
        pre_current_counter = int(snake_run_counter)
        snake_run_counter += difficult
        if pre_current_counter != int(snake_run_counter):
            pre_move = True
            if right_move:
                snake_movement('r')
            elif left_move:
                snake_movement('l')
            elif up_move:
                snake_movement('u')
            elif down_move:
                snake_movement('d')
        is_snake_ate_apple()

    if failed:
        snake_hit_wall.play()
        # render transparent picture
        rect = (0,0,window_width,window_height)
        surface = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        surface.fill((200,200,200,150))
        play_screen.blit(surface, rect)
        # render text
        failed_render = failed_text.get_rect(center=(window_width / 2, window_height / 2))
        restart_render = restart_text.get_rect(center=(window_width / 2, window_height / 2 + 50))
        play_screen.blit(failed_text, failed_render)
        play_screen.blit(restart_text, restart_render)
        # disable snake movement
        reset = True
        failed = False
    
    clock.tick(30)
    pygame.display.update()