def addition(a, b): #Addition
    return a + b

def subtraction(a, b): #Subtraction
    return a - b

def multiplication(a, b): #Multiplication
    return a * b

def division(a, b): #Division
    return a / b #Error handling in readinput()



def readInput(input): #Read user input
    equation = input.split(" ")
    if (len(equation) == 3):
        try:
            equation[0] = int(equation[0])
            equation[2] = int(equation[2])

            if equation[1] == "+":
                print(addition(equation[0], equation[2]))
            elif equation[1] == "-":
                print(subtraction(equation[0], equation[2]))
            elif equation[1] == "*":
                print(multiplication(equation[0], equation[2]))
            elif equation[1] == "/":
                print(division(equation[0], equation[2]))
            else:
                raise TypeError("Invalid operator")

            return True #Successful return
        except TypeError as e: #Raised when operator isn't correct
            print("Error: %s" %(e))
        except ValueError: #Raised when float conversion fails
            print("Error: Invalid operands")
        except ZeroDivisionError: #Raised when dividing by 0
            print("Error: Divide by Zero")
    else: #Invalid input
        print("Error: Invalid Input")
        print("Syntax: 2 + 2")
    return False #Unsuccessful return

if __name__ == "__main__": #Main code
    value = ""
    while(value != "exit"): #Main loop
        print("Enter exit to exit")
        value = input("Enter equation: ")
        if value != "exit":
            readInput(value)
        print()
