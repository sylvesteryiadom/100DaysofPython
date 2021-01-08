# HANGMAN
import random
words = ['banana', 'orange','melon','important']

# randomWord = words[random.randint(0,len(words))]
chosenWord = random.choice(words)
print(f"{chosenWord}")

display = []

for _ in chosenWord:
    display += '_'

while len(chosenWord) == len(display):
    guess = input("Guess a letter: ").lower()[0] #capture 1 letter

    for i in range(0,len(chosenWord)):
        if guess == chosenWord[i]:
            display[i] =chosenWord[i]
    print(display)

print('You win!')



