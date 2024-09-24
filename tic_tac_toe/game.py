from player import Player
from menu import Menu
from board import Board
import os
import time

class Game:
    def __init__(self) :
        self.players = [Player(),Player()]
        self.board = Board()
        self.menu = Menu()
        self.player_idx = 0

    
    #the order of the game is : start_game => if choose (1) => setup_players => play_game => display_board
    #                                                       => play_turn (choose_cell => update_board =>switch_player)
    #                                                       => check if win or dra
    #                                                                           
    #                                         if choose (2) => quit_game

    def start_game(self):
        main_menu_choice = self.menu.display_main() #this has the player choice from the main menu screen
        if main_menu_choice == 1:
            time.sleep(0.7) #it delays the game for 1 sec before clearing the terminal screen
            self.__clear_screen() 
            self.setup_players()
            self.__clear_screen()
            self.play_game()
        elif main_menu_choice == 2:
            self.quit_game()

    def setup_players(self):
        for idx,player in enumerate(self.players,start=1):
                print(f"Player {idx}. Please enter your details:")
                player.choose_name()
                player.choose_symbol()
                print("-"*40 if idx < 2 else "")


    def play_game(self):
        while True:
            if self.check_win() or self.check_draw():
                if self.check_win(): 
                    self.board.display_board()
                    print(f"\n\t!!  {self.players[1-self.player_idx].display_name().upper()} WINS  !!")
                elif self.check_draw(): 
                    self.board.display_board()
                    print("\n\t!! IT'S A TIE !!")
                time.sleep(3)
                self.__clear_screen()
                end_choice = self.menu.display_endgame()
                if end_choice == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                    break
                
            else:
                self.board.display_board()
                self.play_turn(self.player_idx)


    def play_turn(self,player_idx):
        cell_choice = input(f"{self.players[player_idx].display_name()}'s turn ({self.players[player_idx].display_symbol()}) choose a number: ")
        if self.board.update_board(cell_choice,self.players[player_idx].symbol):
            self.switch_current_player()
            self.__clear_screen()
            
    def check_win(self):
        b = self.board.board
        transposed_b = [[row[i] for row in b] for i in range(len(b[0]))]
        b_left_diag = [b[i][i] for i in range(3)] 
        b_right_diag = [b[i][2-i] for i in range(3)] 
        x_win = ['X','X','X']
        o_win = ['O','O','O']

        for row in b: #check rows horizontally
            if row == x_win or row == o_win:
                return True
        for row in transposed_b: # check columns vertically
            if row == x_win or row == o_win:
                return True
        if b_left_diag == x_win or b_left_diag == o_win or b_right_diag == x_win or b_right_diag == o_win :
                #this conditions checks the diagonalls
                return True
        return False

    def check_draw(self):
        return all(self.board.board[j][i].isalpha() for i in range(3)for j in range(3))
    
    # def check_draw(self):
        # for row in self.board.board:
        #     for col in row:
        #         if col.isdigit():
        #             return False
        # return True
        
    
    def game_end(self):
        choice = self.menu.display_endgame()
        if choice == 1:
            self.restart_game()
        else:
            self.quit_game()

    def restart_game(self):
        self.board.reset_board()
        self.player_idx = 0
        self.__clear_screen()
        self.play_game()

    def quit_game(self):
        print("\n\tThank you for playing !!!".upper())
        time.sleep(1)

    def switch_current_player(self):
        self.player_idx = 1 - self.player_idx

    @staticmethod
    def __clear_screen(): #function to clear the terminal screen
        os.system('cls')


game = Game()
game.start_game()

    