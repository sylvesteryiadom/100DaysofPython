programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.", }

# Adding new dictionary items
programming_dictionary["Loop"] = "Going over and over again"

# Create an empty dictionary
empty_dictionary = {}

# Wiping an existing dictionary
programming_dictionary = {}

#Editing an item in a dictionary
programming_dictionary["Bug"] = "A Moth" # changes the value of "Bug"
print(programming_dictionary)

# looping through a dictionary
for key in programming_dictionary:
    print(programming_dictionary[key]) # returns the value for each key


# Challenge

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
# loop through original and add key and values converted to grades
for student in student_scores:
    score = student_scores[student]
    if score > 90 and score <=100:
        student_grades[student] = 'Outstanding'
    elif score > 80 and score <=90:
        student_grades[student] = 'Exceeds Expectations'
    elif score > 70 and score <=80:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
    
    

# 🚨 Don't change the code below 👇
print(student_grades)





