class Menu:
    def display_main(self):
        main_menu = '''
                TIC-TAC-TOE 
        1. Start Game
        2. Quit Game 
        '''
        return self.__display_choices(main_menu)
            
    def display_endgame(self):
        end_menu = '''
                GAME OVER 
        1. Restart Game
        2. Quit Game 
        '''
        return self.__display_choices(end_menu)

    @staticmethod
    def __display_choices(menu_text):
        while True:
            choice = input(menu_text + "Please enter your choice: ")
            if choice.isdigit():
                choice = int(choice)
                if choice in range(1,3):
                    return choice
                print('\tInvalid choice.Please choose 1 or 2')
            else:
                print('\tCan\'t choose a letter. Please choose 1 or 2')
