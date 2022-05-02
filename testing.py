

import random



word_bank = ['music', 'guitar', 'piano', 'dragon', 'wizard', 'magic', 'ghost', 'flower', 'chocolate', 'castle']

secret_word = random.choice(word_bank)

letters_guessed = ''

guess_count = 7

while guess_count > 0:
    current_guess = input('Guess a letter: ')
    if current_guess in secret_word:
        print(f'Correct! {current_guess} is in the secret word!')
    else:
        guess_count -= 1
        print(f'Sorry, {current_guess} is not in the secret word. Try again!')
    
    letters_guessed = letters_guessed + current_guess
    wrong_letters_count = 0

    for letter in secret_word:
        if letter in letters_guessed:
            print(f'{letter}', end = '')
        else:
            print('_', end = '')
            wrong_letters_count += 1
    if wrong_letters_count == 0:
        print(f'\nHooray! The secret word was {secret_word}. You win!')
        break
else:
    print(f'\nWomp-womp. The secret word was {secret_word}. Game Over.')