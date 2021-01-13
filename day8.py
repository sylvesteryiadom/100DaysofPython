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

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
def decode(plain_text, shift_amount):
  decypher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    decypher_text += alphabet[new_position]
  print(f"The decoded text is {decypher_text}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == 'encode':
  encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
  decode(plain_text=text, shift_amount=shift)