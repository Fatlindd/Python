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
