"""
Ask user to plug in a number from 20 to 100

Send users number to a function to validate the number

use a while loop to keep asking the user for a valid number

return number to main function

Program 3 functions to figure out if its divisible by 2,3 or 5
"""


def main():
    x = int(input("Please enter a number between 20 to 100 "))

    valid = validate(x)
    division(valid)


def validate(x):
    while x < 20 or x > 100:
        print("Number is not valid. \nPlease enter a valid number")
        x = int(input("Please enter a number between 20 to 100 "))
    return x


def division(x):
    if x % 3 == 0:
        print('Number is divisible by 3') #is divisible by 3
    else:
        print("Number is not divisible by 3")
    if x % 2 == 0:
        print('Number is divisible by 2')
    else:
        print('Number is not divisible by 2')
    if x % 5 == 0:
        print('Number is divisible by 5')
    else:
        print('Number is not divisible by 5')


main()
