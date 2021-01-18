import art
print(art.logo)
print("Welcome to the secret auction program")
# create empty dict and add to the dictionary Global variables
auction_list = {}
bidding_over = False

while not bidding_over:
  name = input("What is your name?: ")
  bid_amount = int(input("What's your bid?: $"))
  auction_list[name] = bid_amount #append to dict
  userAnswer = input("Are there any other bidders? Type 'yes' or 'no'") #check for gameOver
  if userAnswer =='no':
      bidding_over = True

max = 0;
#sample dict {"Angela":100, "James":110}

# loop to print autction and compare to max value
for key in auction_list:
  amount = auction_list[key]
#   logic for determining max value
  if amount > max:
    max = amount

print(f"{key} is the winner of the auction with an amount of ${max}")