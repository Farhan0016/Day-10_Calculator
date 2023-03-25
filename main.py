#import logo from art.py module
from art import logo

#Addition function
def add(number1, number2):
    return number1 + number2

#Subtraction function
def subtract(number1, number2):
    return number1 - number2

#Multiplication function
def multiply(number1, number2):
    return number1 * number2

#Divison function
def divide(number1, number2):
    return number1 / number2

def calculator():
    #Print calculator logo
    print(logo)

    #Take first number
    first_number = float( input("What's the first number?: ") )

    #Loop run infinite number of time because calculation is not stop until we live
    while True:
        #Print the list of operations which is defined
        for operation in operations:
            print(operation)

        #Get the operator from user
        operator = input("Pick an operation: ")
        #operator = input("+ \n- \n* \n\\ \nPick an operation: ")
        #If user choose invalid operator other than arithmatic
        if operator not in operations:
            print("You chose an invalid operation.")
            continue

        #Take second number
        second_number = float( input("What's the next number?: ") )

        #store the value of operation based on key into the function variable
        function = operations[operator]

        #Calculate the result by calling the function
        answer = function(first_number, second_number)
        # if operator == "+":
        #     answer = add(first_number, second_number)
        # elif operator == "-":
        #     answer = subtract(first_number, second_number)
        # elif operator == "*":
        #     answer = multiply(first_number, second_number)
        # else:
        #     answer = divide(first_number, second_number)

        #Print results
        print(f"{first_number} {operator} {second_number} = {answer}")

        #Ask user if they want to continue with previous result or start with new inputs
        result = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:").lower()

        #If user want to continue with previous result than store the answer into the first_number else again call the calculator() function
        if result == 'y':
            first_number = answer
        else:
            should_continue = False
            calculator()
            #print(logo)
            #first_number = float(input("What's the first number?: "))

#Operations
operations = {
        "+" : add,
        "-" : subtract,
        "*" : multiply,
        "/" : divide
    }

#Call the calculator() function
calculator()