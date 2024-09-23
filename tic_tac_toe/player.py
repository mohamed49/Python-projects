class Player:

    def __init__(self,name = '',symbol = ''):
        self.name = name 
        self.symbol = symbol
    
    def choose_name(self):
        while True: #the while is to keep asking the player to enter a valid name not containing numbers
            self.name = input('Please enter your name (LETTERS ONLY): ') 
            if self.name.isalpha():
                break
            print("Invalid input. Please enter letters only.")

    def choose_symbol(self):
        while True: #the while is to keep asking the player to enter a valid symbol X or O
            self.symbol = input(f'{self.name} please choose (X) or (O): ').upper()
            if self.symbol in ['X','O']:
                break
            print("Invalid input. Please enter (X) or (O) only.")

    def display_name(self):
        return self.name

    def display_symbol(self):
        return self.symbol

