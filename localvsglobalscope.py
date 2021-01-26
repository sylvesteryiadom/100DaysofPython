# ##############SCOPE

# enemies = 1 #global scope

# def increase_enemies():
#     # local scope
#     enemies = 2
#     print(f"enemies inside the function: {enemies}")
    
    
# increase_enemies()

# global scope
# print(f"enemies inside the function: {enemies}")


levels = 3
enemieList = ['zombie','skeleton','dwarfs']

if levels > 2:
    new_enemie = enemieList[0]
    
print(new_enemie) # this will print zombie

# levvels = 3
# enemieList2 = ['zombie','skeleton','dwarfs']

# def newEnemy():
#     if levvels > 2:
#         another_enemie = enemieList[1]

# print(another_enemie) #this is out of scope because another_enemie is inside a function


enemies = 1 #global scope

def increase_enemies():
    # local scope
    print(f"enemies inside the function: {enemies}")
    return enemies +1
    
    
enemies = increase_enemies()
print(f"enemies inside the function: {enemies}")