class Board:
    def __init__(self) -> None:
        #this is a 3*3 list filled with each row a number from 1-3 added to 3 multiplied by row no.(start from 0)  
        #so for cell (1,1)==> 1+3(0) and for cell (5,5)==> 2+3(1)
        self.board = [[str(j*3+i) for i in range(1,4)]for j in range(3)]

    #this function displays the board with the current state for all the cells 
    def display_board(self):
        for i,row in enumerate(self.board):
            print("\t  "," | ".join(row))
            if i < 2: #this prints the horizontal line for the first 2 rows only
                print("\t  ---+---+--- ")

    #this functions updates the board according to the players choosen cell no,it takes 2 paramaters 
    # the first is the cell no of choice and the second is the player symbol
    def update_board(self,choice="",sym=""): 
    #checking the value of the choosen cell if between 1-3 then choose 1st row, if 4-6 then 2nd row and so on,
        row = 0
        if choice.isdigit():
            choice = int(choice)
            if 0 < choice < 4:
                row = 0
            elif 3 < choice < 7:
                row = 1
            elif 6 < choice < 10:
                row = 2
            else: # error message if the chosen value is not between 1-9
                print("Invalid Choice!! Choose a number between 1 and 9")
                return False
        else:
                print("Can't choose a letter!! Choose a number between 1 and 9")
                return False
    #checking if the cell is empty or not ,if true update the cell if false give error
        if self.check_cell(row,choice,sym):
            self.board[row][(choice % 3)-1] = sym #this code takes the modulus of 3 for the choice to determine which cell to add the symbol to
            return True
        else :
            print("this cell is taken. Choose another one!! ")
            return False

    #this function resests the board with the numbers from 1-9 in case of a game restart 
    def reset_board(self):
        self.board = [[str(j*3+i) for i in range(1,4)]for j in range(3)]

    #this func. checks if the cell is empty or not to play on it, if it's empty then it assigns the symbol to the cell 
    #if it's not empty it gives an error message
    def check_cell(self,row,choice,sym):
            #this code takes the modulus of 3 for the player choice to check if empty or not
            if self.board[row][(choice % 3)-1].isdigit():
                return True
            else:  
                return False
