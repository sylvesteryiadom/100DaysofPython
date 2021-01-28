import random
from numberart import logo

print(logo)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
# generate random number
randomInt = random.randint(1,100)
# print(f"The correct answer is {randomInt}") # for debugging
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
#number of attempts (Global)
attempts = {
    'easy': 10,
    'hard': 5,
}

def gameInit():
    number_of_attempts = attempts[difficulty]
    print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    # state variable
    is_guess_correct = False #global
    
    while not is_guess_correct:
        user_guess = int(input("Make a guess: ")) # stops the loop and prompts user for input
            
        if user_guess > randomInt:
            print("Too high!")
            print("Guess again")
            number_of_attempts -= 1 
            print(f"You have {number_of_attempts} attempts remaining to guess the number.")
            if number_of_attempts == 0:
                is_guess_correct = True
                print(f"Game Over! the correct answer was {randomInt}")
        elif user_guess < randomInt:
            print("Too low.")
            print("Guess again")
            number_of_attempts -= 1 
            print(f"You have {number_of_attempts} attempts remaining to guess the number.")
            if number_of_attempts == 0:
                is_guess_correct = True
                print(f"Game Over! the correct answer was {randomInt}")
        
        else:
            print(f"You got it! the answer was {randomInt}")
            is_guess_correct = True

gameInit()
    
    

        

