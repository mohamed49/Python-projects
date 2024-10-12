import numpy as np

class Board:
    def __init__(self) -> None:
        self.height = 6
        self.width = 7
        self.board = np.zeros((self.height,self.width))

    def drop_piece(self,col,turn):
        for i in range(self.height):
            if( self.board[self.height-1-i,col] == 0 ):
                self.board[self.height-1-i,col] = turn
                break

    def is_valid_location(self,col):
        return self.board[0,col] == 0
    
    def print_board(self):
        print(self.board)
