import sys 
import os


def main():
    while True:
        try:
            integers = input("Input two integers or type Quit: ").split()
            
            if integers[0] == "quit":
                    return False
                
            elif len(integers) > 2:
                os.system('cls')
                print("Too many integers!\n")
            
            elif integers.isdigit() == False:
                os.system('cls')
                print("Please only input integers.")
            
            else:
                integer_1 = integers[0]
                integer_2 = integers[1]
                
                command = input("| Addition | Subtraction | Multiplication | Division | ").lower()
                
                if command == "addition":
                    add = addition(integer_1, integer_2)
                    os.system('cls')
                    print(f"{integer_1} + {integer_2} = {add}\n")
                    
                elif command == "subtraction":
                    subtract = subtraction(integer_1, integer_2)
                    os.system('cls')
                    print(f"{integer_1} - {integer_2} = {subtract}\n")
                    
                elif command == "multiplication":
                    multiply = multiplication(integer_1, integer_2)
                    os.system('cls')
                    print(f"{integer_1} x {integer_2} = {multiply}\n")
                
                elif command == "division":
                    divide = division(integer_1, integer_2)
                    os.system('cls')
                    print(f"{integer_1} / {integer_2} = {divide}\n")
                    
                else:
                    os.system('cls')
                    print("Invalid input")
            
        except ZeroDivisionError:
                os.system('cls')
                print("Can't divide by zero\n")
        except ValueError:
            os.system('cls')
            print("Invalid input\n")
            
            
        

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
    
    
    
