import random

first = """
    ------
   |     | 
   | 
   | 
   | 
   | 
  _|_ 
"""

second = """
    ------
   |     | 
   |     O
   | 
   | 
   | 
  _|_ 
"""

third = """
    ------
   |     | 
   |     O
   |     |
   |     |
   | 
  _|_ 
"""

fourth = """
    ------
   |     | 
   |     O
   |    /|\\
   |     |
   | 
  _|_ 
"""

fifth = """
    ------
   |     | 
   |     O
   |    /|\\
   |     |
   |    / \\
  _|_ 
"""
images = [first, second, third, fourth, fifth]

def print_guess():
    print(' '.join(guess))

def find(word, letter):
    """ Return idecies of letter in word. """
    return [indx for indx in range(len(word)) if word[indx] == letter]

def fill_guess(indecies, user_input):
    global guess
    for indx in indecies:
        guess[indx] == user_input

if __name__ == "__main__":
    print("Welcome to Hangman game!\nType 'exit' to exit the game.")
    words = ['pristina', 'police', 'python']
    user_input = None
    while user_input != 'exit':
        word = random.choice(words)
        guess = ["_" for i in range(len(word))]
        guessed_words = []
        wrong_guesses = 0
        print(f'\nGuess the word with {len(word)} letters!')
        print('\n')
        print_guess()
        while True:
            user_input = input('\nGuess a letter: ')
            if user_input == 'exit':
                break

            if user_input.isalpha() and len(user_input) == 1:
                
                if user_input not in guessed_words:
                    guessed_words.append(user_input)
                else:
                    print('You already guessed this letter.')
                    continue

                indecies = find(word, user_input)
                if indecies:
                    fill_guess(indecies, user_input)
                    print(' '.join(guess))
                    if "_" not in guess:
                        print('You won.')
                        user_input = input("\nPress Enter to play again or type 'exit' to exit the program: ")
                        break
                else:
                    print(images[wrong_guesses])
                    wrong_guesses += 1
                    if wrong_guesses == 5:
                        print('You failed.')
                        user_input = input("\nPress Enter to play again or type 'exit' to exit the program: ")
                        break
            else:
                print(f'{user_input} is not a valid input.')                
