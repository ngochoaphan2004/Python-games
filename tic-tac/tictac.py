import pygame, sys
import os
pygame.init()
# Get current file path
base_path = os.path.dirname(__file__)
# Pause game
pause = False
# Variables
num_row = 20
table_width = 400
table_height = 400
information_space = 100
cell_size = table_height / num_row
tick_size = cell_size * 0.8
# Game variable
turn = 'X'
ma_table = [[-1 for x in range (num_row)] for y in range(num_row)]
# Some init feature
clock = pygame.time.Clock()
screen = pygame.display.set_mode((table_width,table_height + information_space))
x_symbol = pygame.image.load(base_path + "\\dist\\x.png")
o_symbol = pygame.image.load(base_path + "\\dist\\o.png")
x_symbol = pygame.transform.scale(x_symbol, (tick_size, tick_size))
o_symbol = pygame.transform.scale(o_symbol, (tick_size, tick_size))
# Method
def screen_init():
    # Color of screen
    screen.fill((189, 255, 253))
    # Play table
    for row in range(1, num_row):
        pygame.draw.line(screen, (0,0,0), (row * cell_size,information_space), (row * cell_size,table_height + information_space), 1)
    for col in range(1, num_row):
        pygame.draw.line(screen, (0,0,0), (0, col *cell_size + information_space),(table_width, col * cell_size + information_space), 1)
    pygame.draw.line(screen, (0,0,0), (0, information_space),(table_width, information_space), 1)    

def find_xy_possition(x, y):
    for row in range(1, num_row + 1):
        for col in range(1, num_row + 1):
            if(x < col * cell_size and y < row * cell_size + information_space):
                return (col-1, row-1)
def click_matrix(x, y):
    if(y < information_space):
        return
    global turn, pause

    possition = find_xy_possition(x,y)


    if(ma_table[possition[1]][possition[0]] == -1):
        ma_table[possition[1]][possition[0]] = 1 if turn == 'X' else 0
        draw_tictac(turn, possition[0] , possition[1])
        if(check_winner(possition[0], possition[1])):
            # Information
            screen.fill((189, 255, 253),(0,0, table_width , information_space))
            font = pygame.font.Font('freesansbold.ttf', 32)
            info_text = font.render("WINNER is " + turn, False, (0,0,0))
            info_rect = info_text.get_rect(center = (table_width / 2 , information_space / 2))
            screen.blit(info_text, info_rect)
            # Paused
            pause = True
            return
        turn = 'O' if turn == 'X' else 'X'
        status()

def draw_tictac(turn , x, y):
    draw_x_pos = x * cell_size
    draw_y_pos = information_space + y * cell_size
    if(turn == 'X'):
        screen.blit(x_symbol, (draw_x_pos + 0.1*cell_size, draw_y_pos + 0.1*cell_size))
    elif(turn == 'O'):
        screen.blit(o_symbol, (draw_x_pos + 0.1*cell_size, draw_y_pos + 0.1*cell_size))
    pygame.display.update()

def status():
    screen.fill((189, 255, 253),(0,0, table_width , information_space))
    font = pygame.font.Font('freesansbold.ttf', 32)
    info_text = font.render("Turn : " + turn, False, (0,0,0))
    info_rect = info_text.get_rect(center = (table_width / 2 , information_space / 2))
    screen.blit(info_text, info_rect)
    pygame.display.update()

def check_winner(x_possition , y_possition):
    # Check horizontal
    count = 1
    for col in range(x_possition - 4, x_possition + 4):
        if(col < 0 or col >= num_row - 1 or ma_table[y_possition][col] == -1):
            continue

        if ma_table[y_possition][col] == ma_table[y_possition][col + 1]:
            count += 1
            if(count == 5):
                line_x = (col - 3) * cell_size
                line_y = information_space + y_possition * cell_size
                line = cell_size/2
                pygame.draw.line(screen, (255,0,0), (line_x, line_y + line) , (line_x + 5 * cell_size , line_y  + line), 2)
                pygame.display.update()
                return True
        else:
            count = 1
    # Check verticel
    count = 1
    for row in range(y_possition - 4, y_possition + 4):
        if(row < 0 or row >= num_row - 1 or ma_table[row][x_possition] == -1):
            continue
        if ma_table[row][x_possition] == ma_table[row + 1][x_possition]:
            count += 1
            if(count == 5):
                line_y = (row - 3) * cell_size + information_space
                line_x = x_possition * cell_size
                line = cell_size/2
                pygame.draw.line(screen, (255,0,0), (line_x + line, line_y) , (line_x + line, line_y + 5 * cell_size ), 2)
                pygame.display.update()
                return True
        else:
            count = 1
    # Check top-left to bottom-right
    count = 1 
    for x1 in range(-4, 4):
        x_curent_pos = x_possition + x1
        y_curent_pos = y_possition + x1
        if(x_curent_pos < 0 or x_curent_pos >= num_row - 1 or y_curent_pos < 0 or y_curent_pos >= num_row - 1 or ma_table[y_curent_pos][x_curent_pos] == -1):
            continue

        if ma_table[y_curent_pos][x_curent_pos] == ma_table[y_curent_pos + 1][x_curent_pos + 1]:
            count += 1
            if(count == 5):
                line_x = (x_curent_pos - 3) * cell_size
                line_y = (y_curent_pos - 3) * cell_size + information_space
                pygame.draw.line(screen, (255,0,0), (line_x, line_y) , (line_x + 5 * cell_size, line_y + 5 * cell_size ), 2)
                pygame.display.update()
                return True
        else:
            count = 1
    # Check top-right to bottom-left
    count = 1 
    for x2 in range(-4, 4):
        x_curent_pos = x_possition - x2
        y_curent_pos = y_possition + x2
        if(x_curent_pos < 0 or x_curent_pos >= num_row - 1 or y_curent_pos < 0 or y_curent_pos >= num_row - 1 or ma_table[y_curent_pos][x_curent_pos] == -1):
            continue
        if ma_table[y_curent_pos][x_curent_pos] == ma_table[y_curent_pos + 1][x_curent_pos - 1]:
            count += 1
            if(count == 5):
                line_x = (x_curent_pos + 4) * cell_size
                line_y = (y_curent_pos - 3) * cell_size + information_space
                pygame.draw.line(screen, (255,0,0), (line_x, line_y) , (line_x - 5 * cell_size, line_y + 5 * cell_size ), 2)
                pygame.display.update()
                return True
        else:
            count = 1
    return False

def reset_table():
    global turn, ma_table
    ma_table = [[-1 for x in range (num_row)] for y in range(num_row)]
    turn = 'X'
    screen_init()



screen_init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not pause and event.type ==  pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_pos , y_pos = event.pos
            click_matrix(x_pos, y_pos)
        elif event.type ==  pygame.MOUSEBUTTONDOWN and event.button == 1:
            pause = False
            reset_table()
    clock.tick(30)
    pygame.display.update()