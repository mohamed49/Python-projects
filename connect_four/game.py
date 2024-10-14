import numpy as np
from board import Board
import pygame

ROWS = 6
COLUMNS = 7
SQUARE_SIZE = 100

pygame.display.set_caption('Connect Four')
screen_width = (ROWS + 1) * SQUARE_SIZE
screen_length = COLUMNS * SQUARE_SIZE
win = pygame.display.set_mode((screen_width,screen_length))

def play_turn(turn):
        #ask player number {turn} to choose a column to play on 
        col = int(input(f'Player {turn + 1} ,please enter your input (0-6) : '))
        if board.is_valid_location(col):
          board.drop_piece(col,turn + 1)
        else:
          print('this is an invalid location')

#main game loop
run = True
turn = 0
board = Board()
board.print_board()
pygame.init()
while run:
    play_turn(turn)
    
    #changes turns after each player plays on his turn
    turn += 1
    turn = turn % 2
    
    #check if any player wins and if so, prints a message for the winner and breaks the main loop
    if board.check_win() == 1:
        print('Red player wins !!')
        run = False
    elif board.check_win() == 2:
        print('Blue player wins !!')
        run = False
    else:
        print("")
pygame.quit()
    board.print_board()
