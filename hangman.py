# hangman.py

import random

def choose_word():
    words = ["python", "hangman", "challenge", "programming", "development"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |   
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |   
           |
        """,
        """
           ------
           |    
           |    
           |    
           |   
           |
        """,
        """
           ------
           |    
           |    
           |    
           |   
           |
        """
    ]
    return stages[tries]

def play_hangman():
    word = choose_word()
    guessed = ""
    tries = 6

    print("Welcome to Hangman!")
    
    while tries > 0:
        print(display_hangman(tries))
        print("Word: " + " ".join([letter if letter in guessed else "_" for letter in word]))
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed:
            print("You already guessed that letter.")
        elif guess not in word:
            tries -= 1
            guessed += guess
            print("Wrong guess!")
        else:
            guessed += guess
            print("Good guess!")

        if all(letter in guessed for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(display_hangman(tries))
        print(f"Sorry, you ran out of tries. The word was: {word}")

if __name__ == "__main__":
    play_hangman()
