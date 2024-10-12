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

    def check_win(self):
        streak_1 = 0
        streak_2 = 0
        orig_board = self.board
        tran_board = np.flip(orig_board.T)

        #check for horizontal win
        for r in range(self.height):    
            for c in range(4):
                if (orig_board[r,c] == 1):
                    length = 1
                    while(length < 4 and orig_board[r,c + length] == 1):
                        length += 1
                    streak_1 = max (length,streak_1)
                elif (orig_board[r,c] == 2):
                    length = 1
                    while(length < 4 and orig_board[r,c + length] == 2):
                        length += 1
                    streak_2 = max (length,streak_2)

        #check for vertical win
        for r in range(self.width):    
            for c in range(3):
                if (tran_board[r,c] == 1):
                    length = 1
                    while(length < 4 and tran_board[r,c + length] == 1):
                        length += 1
                    streak_1 = max (length,streak_1)
                elif (tran_board[r,c] == 2):
                    length = 1
                    while(length < 4 and tran_board[r,c + length] == 2):
                        length += 1
                    streak_2 = max (length,streak_2)

        if streak_1 >= 4:
            return 1
        elif streak_2 >= 4:
            return 2
        else:
            return -1

    def is_valid_location(self,col):
        return self.board[0,col] == 0
    
    def print_board(self):
        print(self.board)
