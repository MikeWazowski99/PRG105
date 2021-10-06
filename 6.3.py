"""
6.3 Try and Except Statements

Find the error and report it to the user
Also detect if there is a bad file name and test it
"""


def main():
    total = 0.0
    try:
        infile = open('sales_error.txt', 'r')
        for line in infile:
            amount = float(line)
            total += amount
        infile.close()
    except FileNotFoundError:
        print("File not found")

    except ValueError:
        print("This number does not work")
        print(total)


main()
