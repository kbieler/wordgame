#Create a program that allows a user 7 chances to guess the correct word. If they do not guess the word 
# #after 7 tries, the player loses and the program will print the correct word. Otherwise, the play #
# wins and the game.

#How to build the program
#When you start the game, you will need to select a random word from a list of at least 10 words 
#(You have full control over which words you want to use for you program). This will be your secret word. 
#Your secret word will be represented in the program as a group of underscores. For as long as the word is,
# you should also have that many underscores.
#Once the word is selected, your game will commence. Perform a Google search to figure out how to select a 
#random word from a list using Python.

#Hint* There's package you can import into your application that does this for you.
#The end user will have a total of 7 chances to guess the correct letter from the secret word. If the end 
# user makes 7 incorrect guesses, the game will end.
#As you guess the correct letters, the letters you have guess will then take place of the underscores that 
# letter represents.

#For Example*: If your secret word is 'watermelon' and so far you have guessed the letters 'a' and 'e', 
# the word you're trying to guess will appear as follows: _ a _ e _ _ e _ _ _.

#Keep in mind* that if you guess a letter that appears more than once in your secret word, make sure that 
# the letter is populated anywhere that letter would be.

import random

class Wordbank:
    def __init__(self):
        self.words = []

    def generate_random(self):
        secret_word = random.choice(self.words)
        return secret_word


word_bank1 = Wordbank()
word_bank2 = Wordbank()
word_bank3 = Wordbank()

word_bank1.words = ['dragon', 'wizard', 'magic', 'ghost','haunted', 'spooky', 'legend', 'knight', 'sword', 'castle']
word_bank2.words = ['music', 'guitar', 'piano', 'dance', 'trumpet', 'disco', 'record', 'banjo', 'orchestra', 'symphony']
word_bank3.words = ['solicitude', 'trifling', 'scrupulous', 'contrived', 'reverie', 'vogue', 'entreaty', 'persevere', 'fastidious']


class Display:

    def __init__(self):
        self.rights = []
        self.wrongs = []

    def wrong_answer(self):
        wrong1 = random.choice(self.wrongs)
        print(wrong1)
    
    def right_answer(self):
        right1 = random.choice(self.rights)
        print(right1)

nope = Display()
yep = Display()

nope.wrongs = ['That guess was more disappointing than an unsalted pretzel. Try again.\n', \
     'Your brain is as dry as the remainder biscuit after a voyage. Try again.\n', \
        'Your mother was a hampster and your father smelt of elderberries. Try again.\n', \
            'A bowl of alphabet soup would give better answers. Try again.\n', \
                "Have you seen of Seasame Street? I hear it's a wonderful program. Try again.\n", \
                    'NO! Try again.\n', \
                        "Wow, this really isn't your game. Try again.\n"]
yep.rights = ['Whoomp, there it is!\n', 'Gold star!\n', 'Crushed it!\n', 'Awesomesauce.\n', 'Bravo!\n', 'Fantastic!\n', \
    'Hurrah!\n']
    

class Game(Wordbank, Display):

    def guessing(word_list):
        secret_word = Wordbank.generate_random(word_list)
        letters_guessed = ''
        guess_count = 7
        while guess_count > 0:
            current_guess = input('\nGuess a letter: ')
            if current_guess in secret_word:
                print(Display.right_answer(yep))                
            else:
                guess_count -= 1
                print(Display.wrong_answer(nope))
                
            wrong_letters_count = 0
            letters_guessed = letters_guessed + current_guess
            
            print("Letters you've guessed so far: ")
            print(letters_guessed)

            for letter in secret_word:
                if letter in letters_guessed:
                    print(f'{letter}', end = '')
            else:
                print('_', end = '')
                wrong_letters_count += 1
            if wrong_letters_count == 0:
                print(f'\nWoohoo! The secret word was {secret_word}. You win!')
                break
        else:
            print(f'\nWomp-womp. The secret word was {secret_word}. Game Over.')


def start_play(word_list):
    print('~oOo~ Welcome to the Secret Word game! ~oOo~\n')
    rules = input('Would you like instructions how to play? (y/n) \n')
    if rules.lower() == 'y':
        print('The rules are as follows:\n \
            -A secret word will be chosen at random.\n \
            -Each turn, you may guess one letter to see if it is in the secret word.\n \
            -Please only enter alpha characters.\n \
            -For every incorrect letter guessed, you earn a strike.\n \
            -After seven strikes, you lose the game.\n \
            -To win, you must guess all the letters in the word before earning seven strikes.\n')
       
    print("Alright, let's play!")
    Game.guessing(word_list)
        


start_play(word_bank1)












      
   





