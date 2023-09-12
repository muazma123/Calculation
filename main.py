#--------------------<< Menu Loader >>--------------------

def menuLoad(menu):

    count = 1



    for z in menu:

        print(f"{count}. {z}")

        count += 1

    print(f"0. EXIT")



    choice = input("Enter Number: ")



    if choice.isnumeric():

        choice = int(choice)

        if choice in range(0, count):

            answer = choice

        else:

            print("Error: Number out of RANGE.")

            answer = 99

    else:

        print("Error: Input NOT a number.")

        answer = 99



    return answer



#--------------------<< Addition Function >>--------------------

def addition(x, y):

    return x + y



#--------------------<< Subtract Function >>--------------------

def subtract(x, y):

    return x - y



#--------------------<< Multipy Function >>--------------------

def multiply(x, y):

    return x * y



#--------------------<< Divide Function >>--------------------

def divide(x, y):

    if y == 0:

        print("Divide by Zero error!")

        return 0

    else:

        return x / y



#--------------------<< Main Program >>--------------------



import math

menu = ["Addition", "Subtraction", "Division", "Multiply"]



while True:

    pick = menuLoad(menu)



    if pick == 0:

        print("Thank you ... Goodbye")

        break



    elif pick == 99:

        continue



    else:

        num1 = input("Enter FIRST number: ")

        num2 = input("Enter SECOND number: ")



        if num1.isnumeric() and num2.isnumeric():

            num1 = int(num1)

            num2 = int(num2)



            if pick == 1:

                ans = addition(num1, num2)

                sym = '+'



            elif pick == 2:

                ans = subtract(num1, num2)

                sym = '-'



            elif pick == 3:

                ans = divide(num1, num2)

                sym = '/'



            else:

                ans = multiply(num1, num2)

                sym = '*'



            print(f"\n{num1} {sym} {num2} = {ans}\n")



        else:

            print("Input Error, Not a Number")
