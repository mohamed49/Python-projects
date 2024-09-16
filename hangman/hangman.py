
    #        <>    <>     <>     <>     <>    <>>>>>        <>        <>     <>     <>     <>
    #        <>    <>   <>  <>   <><>   <>  <>      >>      <> <>  <> <>   <>  <>   <><>   <>
    #        <><><><>  <><><><>  <>  <> <>  <>              <>  <><>  <>  <><><><>  <>  <> <>
    #        <>    <>  <>    <>  <>   <><>  <>    <<<<      <>   <>   <>  <>    <>  <>   <><>
    #        <>    <>  <>    <>  <>     <>    <><><>>       <>        <>  <>    <>  <>     <>
    #                      
    #                   ______
    #                  |      |      
    #                  |      @
    #                  |     /|\     
    #                  |      |  
    #                  |     / \
    #    ______________|__________________
    #   /              |                 /| 
    #  /                                / |         
    # /________________________________/ /
    # |________________________________|/
    #

from words import words
import random


def get_valid_word(word_list,length):
    word = random.choice(word_list)
    while '-' in word or ' ' in word or len(word) != length :
        word = random.choice(word_list)
    return word

def hangman():
    logo = '''
            88                                                                            
            88                                                                            
            88                                                                            
            88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba, 
            88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8 88P'   `"8a 
            88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88 88       88 
            88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88 88       88 
            88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8 88       88 
                                                aa,    ,88                                
                                                "Y8bbdP" 
'''
    stages = ['''
                              ______
                             |      |      
                             |      @
                             |     /|\\     
                             |      |  
                             |     / \\
               ______________|__________________
              /              |                 /| 
             /                                / |         
            /________________________________/ /
            |________________________________|/
''', '''
                              ______
                             |      |      
                             |      @
                             |     /|\\     
                             |      |  
                             |     / 
               ______________|__________________
              /              |                 /| 
             /                                / |         
            /________________________________/ /
            |________________________________|/
''', '''
                              ______
                             |      |      
                             |      @
                             |     /|\\     
                             |      |  
                             |     
               ______________|__________________
              /              |                 /| 
             /                                / |         
            /________________________________/ /
            |________________________________|/
''', '''
                              ______
                             |      |      
                             |      @
                             |     /|\\     
                             |        
                             |     
               ______________|__________________
              /              |                 /| 
             /                                / |         
            /________________________________/ /
            |________________________________|/
''', '''
                              ______
                             |      |      
                             |      @
                             |     /|     
                             |        
                             |     
               ______________|__________________
              /              |                 /| 
             /                                / |         
            /________________________________/ /
            |________________________________|/
''', '''
                              ______
                             |      |      
                             |      @
                             |      |    
                             |        
                             |     
               ______________|__________________
              /              |                 /| 
             /                                / |         
            /________________________________/ /
            |________________________________|/
''', '''
                              ______
                             |      |      
                             |      @
                             |          
                             |        
                             |     
               ______________|__________________
              /              |                 /| 
             /                                / |         
            /________________________________/ /
            |________________________________|/
''', '''
                              ______
                             |      |      
                             |      
                             |          
                             |        
                             |     
               ______________|__________________
              /              |                 /| 
             /                                / |         
            /________________________________/ /
            |________________________________|/
''']
    lives = 7
    word = get_valid_word(words,lives).upper()
    word_letters = set(word)
    used_letters = set()
    print(logo)
    while len(word_letters) > 0: 
        wordlist = [letter if letter in used_letters else '-' for letter in word]
        #shows current state
        print(stages[lives])
        print('Your guessed letters : ', ' '.join(wordlist))
        print('your used letters : ',' '.join(used_letters))
        if lives > 0:   

            # take input from the user
            user_input = input('Guess a letter: ').upper()

            if user_input in used_letters:
                print("you have already guessed the letter", user_input)

            elif user_input in word:    
                word_letters.remove(user_input)
                used_letters.add(user_input)
            
            else:
                lives -= 1
                used_letters.add(user_input)

        else:
            input("you have lost !!!")
    input("YAY!! you have won !!!")


hangman()
 