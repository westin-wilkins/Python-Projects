import os

def main():
    while True:
        try:
            integers = integer_checker()
            
            if integers == False:
                return False
            
            else:
                integer_1 = integers[0]
                integer_2 = integers[1]
                
                math_operation(integer_1, integer_2)
        # Handles the case when the user tries to divide by zero. Prevents the program
        # from crashing
        except ZeroDivisionError:
                os.system('cls')
                print("Can't divide by zero\n")

# Function that checks the user's input to make sure that it is an integer or quit       
def integer_checker():
    while True:
        user_input = input("Input two integers or type Quit: >")
        
        if user_input.lower() == 'quit':
            os.system('cls')
            return False

        else:
            integer_check = user_input.split()
            # Checks if the user typed in to many numbers
            if len(integer_check) > 2:
                os.system('cls')
                print("Too many integers!\n")
            # Checks if the user typed in characters instead of numbers
            elif not integer_check[0].isdigit() or not integer_check[1].isdigit():
                os.system('cls')
                print("Please only input integers")
            # If the input is acceptable, the values are passed back to the main function
            else:
                return integer_check
            
# Function that performs the calculations depending on what is typed in
def math_operation(integer_1, integer_2):
    while True:
        user_input = input("| Addition | Subtraction | Multiplication | Division | >").lower()
        
        if user_input == "addition":
            add = addition(integer_1, integer_2)
            os.system('cls')
            print(f"{integer_1} + {integer_2} = {add}\n")
            
        elif user_input == "subtraction":
            subtract = subtraction(integer_1, integer_2)
            os.system('cls')
            print(f"{integer_1} - {integer_2} = {subtract}\n")
            
        elif user_input == "multiplication":
            multiply = multiplication(integer_1, integer_2)
            os.system('cls')
            print(f"{integer_1} x {integer_2} = {multiply}\n")
        
        elif user_input == "division":
            divide = division(integer_1, integer_2)
            os.system('cls')
            print(f"{integer_1} / {integer_2} = {divide}\n")
            
        else:
            os.system('cls')
            print("Invalid input")

# All of the possible operations
def addition(integer_1, integer_2):
    return int(integer_1) + int(integer_2)

def subtraction(integer_1, integer_2):
    return int(integer_1) - int(integer_2)

def multiplication(integer_1, integer_2):
    return int(integer_1) * int(integer_2)

def division(integer_1, integer_2):
    return int(integer_1) / int(integer_2)

if __name__ == '__main__':
    main()
    
    
    
