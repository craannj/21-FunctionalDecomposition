"""
Hangman.

Authors: Daniel Decker and Nathaniel Craan.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.


####### Do NOT attempt this assignment before class! #######


import random


def main():
    play_game()


def get_word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
    possible = []
    limit = min_length()
    for k in range(len(words)):
        if len(words[k]) > limit:
            possible.append(words[k])
    r = random.randrange(0, len(possible))
    # print(possible[r])
    return possible[r]


def min_length():
    minimum = int(input('What minimum length do you want for the word?'))
    return minimum


def get_guess():
    guess = str(input('Please enter a letter:'))
    print(guess)
    return guess


def compare_guess():
    attempts = num_attempts()
    c = get_word()
    guess = []
    for k in range(len(c)):
        guess.append('-')
    print(guess)
    while attempts > 0:
        d = get_guess()
        if d in c:
            print('Correct!')
            for k in range(len(c)):
                if c[k] == d:
                    guess[k] = d
            print(guess)
        if d not in c:
            print('Incorrect!')
            print(guess)
            attempts = attempts - 1
            print('You have attempts', attempts, 'remaining')
        if '-' not in guess:
            print('CONGRATULATIONS!')
            break
    if attempts == 0:
        print('GAME OVER!', 'The secret word was', c,'!')



def num_attempts():
    attempts = int(input('How many attempts would you like?'))
    return attempts


def play_game():
    compare_guess()
    option = str(input('Would you like to play again? Enter Y or N:'))
    if option == 'y':
        play_game()
    if option == 'n':
        print('Thanks for playing!')


main()
