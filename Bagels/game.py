#Bagels Game

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(f''' I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
Pico         One digit is correct but in the wrong position.
Fermi        One digit is correct and in the right position.
Bagels       No digit is correct''')
    
    #main game logic
    while True:
        secret_number = getSecretNumber()
        print(f'''
        I thought of a number 
              You have {MAX_GUESSES} to guess it''' )
        numOfGuesses = 1
        while numOfGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numOfGuesses}')
                guess = input('>> ')
            clues = getClues(guess, secret_number)
            print(clues)
            numOfGuesses += 1

            if guess == secret_number:
                break
            if numOfGuesses > MAX_GUESSES:
                print(f'''You ran out of guesses 
                      The answer is >> {secret_number}''')
                
        #asking if they want to continue
        print('Do you want to play the game again "Yes" or "No" ')
        if not input("> ").lower().startswith('y'):
            break
    print("Thank you for playing")



def getSecretNumber():
    """Returns a 3 digit number from the randomly from 0-9"""
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_number = ''
    for i in range(NUM_DIGITS):
        secret_number += str(numbers[i])
    return secret_number


def getClues(guess, secret_number):
    """Returns the strings Pico , Fermi, Bagels associated with the guesses """
    if guess == secret_number:
        return "You got it!"
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append("Fermi")
        elif guess[i] in secret_number:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return  ' '.join(clues)

if __name__ == '__main__':
    main()