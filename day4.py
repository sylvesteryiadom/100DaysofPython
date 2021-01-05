# Randomization and Python List
import random

# randomInteger = random.randint(1,10)
# print(randomInteger)

# # Random float
# random_float = random.random() * random.randint(1,5)
# print(random_float)

# random_number =  random.randint(0,1)

# if random_number == 0:
#     print('Heads')
# else:
#     print('Tails')


# Python List - Similar to JS arrays

#  states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america[0])
# print(states_of_america[random.randint(0,10)]) #choosing a random state

# states_of_america.extend(["Additional State Added"])
# print(states_of_america[-1])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# import random
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# random_name = names[random.randint(0,len(names)-1)]
# print(f"{random_name} is going to buy the meal today!")

# NESTED LIST
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
row='row' # creating row to pull out of map
rowNum = 0 # placeholder variable
newrow= row+position[0] #pulling out numbers
colNum = int(position[1])-1


if(newrow == 'row1'):
    rowNum = 0
    map[colNum][rowNum] = 'X'
elif (newrow == 'row2'):
    rowNum = 1
    map[colNum][rowNum] = 'X'
elif (newrow == 'row3'):
    rowNum = 2
    map[colNum][rowNum] = 'X'


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
