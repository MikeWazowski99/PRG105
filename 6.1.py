"""
6.1 Homework Assignment

Simple make a program that asks for name, email and phone number and print it all with a function


"""


def main():
    entries = int(input("How many people would you like to add to the file? "))
    info_file = open("information.txt", "w")
    for x in range(entries):
        name = input("What is the name of the person? ")
        email = input("What is their email address? ")
        phone = input("What is their phone number? ")
        info_file.write(name + " ," + phone + " ," + email + "\n")

    info_file.close()


main()
