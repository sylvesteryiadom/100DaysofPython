# FOR LOOP

# fruits = ['apple','peach','pear']
# for fruit in fruits:
#     print(fruit)
    
# student_heights = [180, 124, 165, 173, 189, 169, 146]

# total = 0;
# for height in student_heights:
#     total+=height

# average = total/len(student_heights)
# print(average)

# Max and Min Functions

# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# max = 0 #start with max value holder

# # loop through student score
# for score in student_scores:
#     if score > max:
#         max = score
#jump out of the loop 
# print(f'The highest score in the class is: {max}')

the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1495785517,
    1858250798,
    1693786723,
    1871655963,
    374455497,
    430158267,
]
# highestScore = 0
# for num in the_list:
#     if num > highestScore:
#         highestScore = num
# print(highestScore)

# sum = 0
# for num in range(1,101):
#     sum +=num

# print(sum)
# total = 0
# for num in range(1,101):
#     if num%2 == 0:
#         total +=num
# print(total)

# FIZZBUZZ  3 = Fizz , 5 = Buzz both 3 and 5 = FizzBuzz
# for num in range(1,101):
#     if num % 3 == 0 and num % 5 == 0: # start with multiple because there might be certain numbers that passes and passes the single ones as well
#         print('FizzBuzz') # if condition passes append something else instead
#     elif num% 3 ==0: 
#         print('Fizz') # if condition passes append something else instead
#     elif num % 5 == 0:
#         print('Buzz') # if condition passes append something else instead
#     else:
#         print(num)
        
        
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# loop based on user number input
passWord = ''
for i in range(0,nr_letters):
    passWord +=letters[random.randint(0,len(letters)-1)]

for i in range(0,nr_symbols):
    passWord +=symbols[random.randint(0,len(symbols)-1)]

for i in range(0,nr_numbers):
    passWord +=(numbers[random.randint(0,len(numbers)-1)])


print(f"Here is your password: {passWord}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# EASY-HARD
randomPass = ''.join(random.sample(passWord,len(passWord)))
print(f"Here is your password: {randomPass}")




