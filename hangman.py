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

if __name__ == "__main__":
    print("Welcome to Hangman game!\nType 'exit' to exit the game.")
    words = ['pristina', 'police', 'python']
    user_input = None
    while user_input != 'exit':
        word = random.choice(words)
        guess = ["_" for i in range(len(word))]
        guessed_words = []