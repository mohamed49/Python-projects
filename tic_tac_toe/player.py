class Player:

    def __init__(self,name = '',symbol = ''):
        self.name = name
        self.symbol = symbol
    
    def choose_name(self):
        while True:
            self.name = input('Please enter player name (LETTERS ONLY): ')
            if self.name.isalpha():
                break
            print("Invalid input. Please enter letters only.")

    def choose_symbol(self):
        while True:
            self.symbol = input('Please choose (X) or (O): ').upper()
            if self.symbol in ['X','O']:
                break
            print("Invalid input. Please enter (X) or (O) only.")


