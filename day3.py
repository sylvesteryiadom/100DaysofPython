# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >=120:
#   print("You can ride the rollercoaster")
# else:
#   print("You cannot ride, too short")

#   Challenge 3-1
# 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# if number % 2 == 0:
#     print("This is an even number.")
# elif number % 2 != 0:
#     print("This is an odd number.")


# height = float(input("Enter your height in m: "))
# weight = int(input("Enter your weight in kg: "))
# bmi = int(weight/ (height*height))

# if bmi <= 18.5:
#     print(f"Your bmi is {bmi}, you are underweight")
# elif bmi > 18.5 and bmi <= 25.0:
#     print(f"Your bmi is {bmi}, you have a normal weight")
# elif bmi > 25.0 and bmi <=30.0:
#     print(f"Your bmi is {bmi}, you are slightly overweight")
# elif bmi > 30.0 and bmi <=35.0:
#     print(f"Your bmi is {bmi}, you are obese")
# else:
#     print(f"Your bmi is {bmi}, you are clinically obese")

# LEAP YEAR

# year = int(input("Enter a year: "))


# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 ==0:
#         print("Leap Year")
#     else:
#         print("Not leap year")
#   else:
#       print("Leap year")
# else:
#     print("Not leap Year")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >=120:
#   print("You can ride the rollercoaster")
#   age = int(input("What is your age? "))
#   if age < 12:
#       bill = 5
#       print(f"Kids tickets are ${bill}")
#   elif age <=18:
#       bill = 7
#       print(f"Youth tickets are ${bill}")
#   else:
#      bill = 12
#      print(f"Adult tickets are ${bill}")
#     # Additional conditions
#   wants_photo = input('Do you want your photo taken? Y or N> ')
#   if wants_photo[0] == 'Y':
#       print(f"You bill is {bill+3}")

#   print(f"You bill is {bill}")
# else:
#   print("You cannot ride, too short")

# PIZZA

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
# bill = 0
# if size[0] == 'S':
#     bill += 15
# elif size[0] == 'M':
#     bill += 20
# elif size[0] == 'L':
#     bill += 25

# if add_pepperoni[0] =='Y':
#     if size == 'S':
#         bill +=2
#     else:
#         bill+=3

# if extra_cheese[0] =='Y':
#     bill+=1
# else:
#     bill

# print(f"Your final bill is: ${bill}.")

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n").lower()

# name2 = input("What is their name? \n").lower()
# both_names = name1+name2
# #TRUELOVE count
# love = 0
# true = 0
# true+=both_names.count('t')
# true+=both_names.count('r')
# true+=both_names.count('u')
# true+=both_names.count('e')
# love+=both_names.count('l')
# love+=both_names.count('o')
# love+=both_names.count('v')
# love+=both_names.count('e')
# loveScore = int(str(true) + str(love))
# print(loveScore)
# if loveScore < 10 or loveScore > 90:
#     print(f"Your score is {loveScore}, you go together like coke and mentos.")
# elif loveScore >=40 and loveScore<=50:
#     print(f"Your score is {loveScore}, you are alright together.")
# else:
#     print(f"Your score is {loveScore}")

# TREASURE ISLAND
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
leftORright = input('You\'re at a cross road. Where do you want to go? "left" or "right" ')

if leftORright == 'left':
    swimOrWait = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across ')
    if swimOrWait == 'wait':
        redYellowBlue = input("You arrive at the island unharmed. There is ahouse with 3 doors. One red, one yellow and one blue. Which color do you choose? ")
        if redYellowBlue == 'yellow':
            print("You win!")
        elif redYellowBlue == 'blue':
            print("Eaten by beasts. Game Over")
        elif redYellowBlue == 'red':
            print("Burned by fire. Game Over")
        else:
            print("Game Over")
    elif swimOrWait !='wait':
        print('Attacked by trout. Game Over.')
else:
    print("Fall into a hole. Game Over.")
