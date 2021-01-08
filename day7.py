# HANGMAN
import random


words = ['banana', 'orange','melon','important']

randomWord = words[random.randint(1,len(words)+1)]
print(randomWord)
userGuess = input("Guess a letter")
