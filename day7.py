# HANGMAN
import random
import hangman_art
import hangman_words


print(hangman_art.logo) #import hangman logo and print it once

chosenWord = random.choice(hangman_words.word_list) #import wordslist and use it

print(f"Psssst, the solution is {chosenWord}")
gameOver = False # state variable
lives = 6
# create blanks
display = []
for _ in chosenWord:
    display += '_'


while not gameOver:
    guess = input("Guess a letter: ").lower()[0] #capture 1 letter
    
    if guess in display:
        print(f"You already guessed {guess}, try a different letter")
    
    for i in range(0,len(chosenWord)):
        if guess == chosenWord[i]:
            display[i] = chosenWord[i]
            
              
    # jump out of the if loop into the for loop and do the check there
    if guess not in chosenWord:
        print(f"You guessed {guess} that is not in the word, you loose a life")
        lives -=1
        if lives == 0:
            gameOver = True
            print('You Loose')
    print(display)
    print(hangman_art.stages[lives])

    if '_' not in display:
        gameOver = True # state variable
        print("You Win")
        


    
