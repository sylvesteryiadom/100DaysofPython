# def greet():
#     print("Hello")
#     print("Hello 2")
#     print("Hello 3")
    
# greet()


# function that allows for input

# def greet_with_name(name):
#     print(f"Hello there {name}, how do you do?")
    
# greet_with_name("Sylvester")
# greet_with_name("Sam")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in the {location}")
    
# greet_with('Sylvester', 'United States')

#Keyword arguments = default arguments


# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"Whats the weather like in the {location}")
    
    
# greet_with(name="Jane Doe",location='USA')

# import math

# test_h = int(input("test_h: "))
# test_w = int(input("test_w: "))
# number of cans = (wall height ✖️ wall width) ÷ coverage per can.

# def paint_calc(height,width,cover):
#   num_of_cans = math.ceil((height * width )/cover)
#   print(f"You'll need {num_of_cans} cans of paint.")





#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# number divisible by 1 and itself.


# CESAR CYPHER
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(userText = text, shift = shift, encodeOrDecode = direction):
  plain_text = ""
  if direction == 'encode':
    for letter in text:
      position = alphabet.index(letter)
      new_position = position + shift
      plain_text += alphabet[new_position]  
    print(f"The encoded text is {plain_text}")
  elif direction == 'decode':
    for letter in text:
      position = alphabet.index(letter)
      new_position = position - shift
      plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text,shift,direction)
