from higherart import logo
from higherart import vs
from game_data import data
import random
 
print(logo)
current_score = 0


computer_res = ''
def print_compare(persA, persB):
    if(persA != persB):
        print(f"Compare A: {persA['name']}, a {persA['description']}, from {persA['country']}.")
        print(vs)
        print(f"Against B: {persB['name']}, a {persB['description']}, from {persB['country']}. ")
        
# state variable 
should_continue = True

while should_continue:
    random_person1 = data[random.randint(0,len(data)-1)]
    random_person2 = data[random.randint(0,len(data)-1)]
    A = random_person1['follower_count']
    B = random_person2['follower_count']
    print_compare(random_person1, random_person2)
    
    user_response = input("Who has more followers? Type 'A' or 'B': ")
    # Capturiing user response
    if user_response == 'A':
        user_response = A
        computer_res = B
    else:
        user_response = B
        computer_res = A

    # BUG
    # print(user_response)
    # print(computer_res)

    if user_response > computer_res:
        current_score+=1
        print(f"You're right! Current score: {current_score}")
        
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}")
        should_continue = False