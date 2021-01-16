import art
print(art.logo)
print("Welcome to the secret auction program")

name = input("What is your name?: ")
bid_amount = int(input("What's your bid?: "))

# create empty dict and add to the dictionary
auction_list = {}
auction_list[name] = bid_amount
userAnswer = input("Are there any other bidders? Type 'yes' or 'no'")

while userAnswer == 'yes':
  name = input("What is your name?: ")
  bid_amount = int(input("What's your bid?: "))
  auction_list[name] = bid_amount #append to dict
  userAnswer = input("Are there any other bidders? Type 'yes' or 'no'") #check for gameOver

max = 0;

# loop to print autction and compare to max value
for key in auction_list:
  amount = auction_list[key]
#   logic for determining max value
  if amount > max:
    max = amount
    
print(f"{key} is the winner of the auction with an amount of {amount}")