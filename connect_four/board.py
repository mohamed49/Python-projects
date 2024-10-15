import numpy as np
import pygame

RADIUS = 45
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
        def check_axial(board,player):
            """Check for a streak of 4 for the given player in the board vertically and horizontally."""
            max_streak = 0
            rows, cols = board.shape
            for r in range(rows):    
                for c in range(cols - 3):
                    if board[r,c] == player:
                        length = 1
                        while length < 4 and board[r,c + length] == player:
                            length += 1
                        max_streak = max(length, max_streak)
            return max_streak
        
        def check_diag(board, player):
            """Check for a diagonal streak of 4 for the given player in the board."""
            max_streak = 0
            rows, cols = board.shape
            for r in range(rows - 3):
                for c in range(cols - 3):
                    if board[r, c] == player:
                        length = 1
                        while length < 4 and board[r + length, c + length] == player:
                            length += 1
                        max_streak = max(length, max_streak)
            return max_streak
    
        orig_board = self.board
        tran_board = np.flip(orig_board.T)
        flipped_board = np.fliplr(orig_board)

        # Check for horizontal, vertical ,negative diagonal and positive diagonal wins
        streak_1 = max(check_axial(orig_board,1),check_axial(tran_board,1),check_diag(orig_board,1),check_diag(flipped_board,1))
        streak_2 = max(check_axial(orig_board,2),check_axial(tran_board,2),check_diag(orig_board,2),check_diag(flipped_board,2))

        if streak_1 >= 4:
            return 1
        elif streak_2 >= 4:
            return 2
        else:
            return -1

    def is_valid_location(self,cell):
        return self.board[0,cell] == 0
    
    def print_board(self):
        print(self.board)

    def draw_board(self,win,rows,columns,square_size,screen_length,screen_width):
        pygame.draw.rect(win,"blue",(0,square_size,screen_width,screen_length))

        for r in range(rows):
            for c in range(columns):
                if self.board[r][c] == 0:
                    pygame.draw.circle(win, "black", (square_size*c+50,square_size*r+150), RADIUS)   
                elif self.board[r][c] == 1:
                    pygame.draw.circle(win, "red", (square_size*c+50,square_size*r+150), RADIUS)   
                else:
                    pygame.draw.circle(win, "orange", (square_size*c+50,square_size*r+150), RADIUS)   
