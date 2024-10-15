import numpy as np
from board import Board
import pygame

# Size constants
ROWS = 6
COLUMNS = 7
SQUARE_SIZE = 100
SCREEN_WIDTH = (ROWS + 1) * SQUARE_SIZE
SCREEN_LENGTH = COLUMNS * SQUARE_SIZE
RADIUS = 48

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Connect Four')
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))
clock = pygame.time.Clock()

# Initialize game variables
turn = 0
board = Board()
bold_font = pygame.font.SysFont('comicsans', 28, True)

def play_turn(turn, x_click):
    """Handles a player's turn."""
    col = x_click // SQUARE_SIZE
    if board.is_valid_location(col):
        board.drop_piece(col, turn + 1)
    else:
        print('This is an invalid location')

def draw_hover_piece(x, turn):
    """Draws the piece that follows the mouse cursor."""
    pygame.draw.rect(win, "black", (0, 0, SCREEN_WIDTH, SQUARE_SIZE))
    color = "red" if turn == 0 else "orange"
    pygame.draw.circle(win, color, (x, SQUARE_SIZE/2), RADIUS)

def check_winner():
    """Checks for a winner and prints the result."""
    winner = board.check_win()
    if winner == 1:
        print('Red wins !!')
        text = bold_font.render('RED WINS!!!', 1, 'red')
        win.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_LENGTH // 2 - text.get_height() // 2))
        return True
    elif winner == 2:
        print('Orange wins !!')
        text = bold_font.render('ORANGE WINS!!!', 1, 'orange')
        win.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_LENGTH // 2 - text.get_height() // 2))
        return True
    return False

# Main game loop
run = True
while run:
    board.draw_board(win, ROWS, COLUMNS, SQUARE_SIZE, SCREEN_LENGTH, SCREEN_WIDTH)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_click = event.pos[0]
            play_turn(turn, x_click)
            turn = (turn + 1) % 2
        elif event.type == pygame.MOUSEMOTION:
            x = event.pos[0]
            draw_hover_piece(x, turn)

    if check_winner():
        run = False

    pygame.display.update()
    clock.tick(60)

pygame.time.wait(3000)
pygame.quit()
