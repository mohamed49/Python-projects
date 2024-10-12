import numpy as np
from board import Board

def play_turn(turn):
        #ask player number {turn} to choose a column to play on 
        col = int(input(f'Player {turn + 1} ,please enter your input (0-6) : '))


#main game loop
run = True
turn = 0

while run:
    play_turn(turn)
    
    #changes turns after each player plays on his turn
    turn += 1
    turn = turn % 2
    