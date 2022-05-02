import random

word_bank = ['music', 'guitar', 'piano', 'dragon', 'wizard', 'magic', 'ghost', 'flower', 'chocolate', 'castle']

secret_word = random.choice(word_bank)

def display_sw(missed, correct, secret_word):
    print ('Missed letters:', end='')
    for letter in missed:
        print(letter, end='')

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end='')

def guessing(guessed):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Invalid answer. Please enter a single letter. ")
        elif guess not in alphabet:
            print('Please enter a letter. ')
        else:
            return guess 

def play_game():
    missed = ''
    correct = ''
    while True:
        display_sw(missed, correct, secret_word)
        guess = guessing(missed + correct)
        if guess in secret_word:
            correct = correct + guess
        else:
            missed = missed + guess 

def play_again():
    response = input('Would you like to play again? (y/n): ').lower()
    if response == 'y':
        play_game()
    else:
        print('Goodbye!')



        

