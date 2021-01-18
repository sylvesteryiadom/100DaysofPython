# functions with Outputs

def format_name(fname, lname):
    """ Takes two names and capitalizes the first letter of both names"""
    return fname.title() + ' ' + lname.title()


new_name = format_name("nana", "kwesi")
print(new_name)

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return month_days[month-1] +1
#     else:
#         return month_days[month-1]


# #🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)
# Calculator

# CALCULATOR
# Add

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

# dictionary


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = int(input("What's your first number?: "))
    symbols = ""
    for sym in operations:
        symbols+= sym +' '
    print(symbols)
    should_continue = True # flag
    while should_continue:
        op_sym = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation = operations[op_sym]
        answer = calculation(num1,num2)
        
        print(f"{num1} {op_sym} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating from {answer}, or type 'n' to exit: ") =='y':
            num1 = answer
        else:
            should_continue = False
            calculator() #recursion - code calling itself

calculator()
            
        



