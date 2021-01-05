import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options1 = [rock, paper, scissors] # putting image in a list
options2 = ['rock', 'paper', 'scissors'] # string list of options
cRandom = random.randint(0,len(options1)-1) #creating random number generator for computer
computerChoice = options1[cRandom] # selecting computer choice based on random Number
uchoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")) #asking for user input
userChoice = options1[uchoice] #selecting options based on user input
print("You chose:\n") #displaying user input
print(userChoice)
userChoice = options2[uchoice] #using the userNumber to select same string option
print("Computer chose:\n") #displaying computer input
print(computerChoice)
computerChoice = options2[cRandom] #using random number to select string option for comparison


# implementing RPS rules
if(userChoice == 'rock') and (computerChoice == 'scissors'):
    print("You win")
elif (userChoice == 'scissors') and (computerChoice == 'rock'):
    print("You loose")
elif (userChoice == 'scissors') and (computerChoice == 'paper'):
    print("You win")
elif (userChoice == 'paper') and (computerChoice == 'scissors'):
    print("You loose")
elif (userChoice == 'paper') and (computerChoice == 'rock'):
    print("You win")
elif (userChoice == 'rock') and (computerChoice == 'paper'):
    print("You loose")
else:
    print("Its a tie")

