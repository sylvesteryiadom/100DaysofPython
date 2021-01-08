# HANGMAN
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words = ['banana', 'orange','melon','important']


chosenWord = random.choice(words)
print(f"{chosenWord}")
gameOver = False # state variable
lives = 6
# create blanks
display = []
for _ in chosenWord:
    display += '_'



while not gameOver:
    guess = input("Guess a letter: ").lower()[0] #capture 1 letter
    
    for i in range(0,len(chosenWord)):
        if guess == chosenWord[i]:
            display[i] =chosenWord[i]
    # jump out of the if loop into the for loop and do the check there
    if guess not in chosenWord:
        lives -=1
        if lives == 0:
            gameOver = True
            print('You Loose')
    print(display)
    print(stages[lives])
        
    if '_' not in display:
        gameOver = True # state variable
        print("You Win")
    

