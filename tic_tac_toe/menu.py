class Menu:
    def display_main(self):
        main_menu = '''
                    TIC-TAC-TOE 
            1.Start Game
            2.Quit Game 
            '''
        return self.__display_choices(main_menu,2)
            
            
    
    def display_endgame(self):
        end_menu = '''
                GAME OVER 
        1.Restart Game
        2.Quit Game 
        '''
        return self.__display_choices(end_menu,2)

    @staticmethod
    def __display_choices(menu_text,no_of_choices):
        while True:
            choice = input(menu_text + "Please enter your choice: ")
            if choice in str(range(1,no_of_choices)):
                return choice
            print('\tInvalid choice.Please choose 1 or 2')

        
