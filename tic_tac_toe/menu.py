class Menu:
    def display_main(self):
        main_menu = '''
                    TIC-TAC-TOE 
            1.Start Game
            2.Quit Game 
            '''
        return self.display(main_menu)
            
            
    
    def display_endgame(self):
        end_menu = '''
                GAME OVER 
        1.Restart Game
        2.Quit Game 
        '''
        return self.__display_choices(end_menu,2)

    @staticmethod
    def display(menu_text):
        while True:
            choice = input(menu_text + "Please enter your choice: ")
            if choice in ['1','2']:
                return choice
            print('\tInvalid choice.Please choose 1 or 2')

        
