"""
CRUD Program

Display a menu that lets the user look up a person's email address, add a new name and email address,
change an existing email address, and delete an existing name and email address.
The program should pickle the dictionary and save it to a file when the user exits the program.

"""

import pickle

Look_up = 1
Add = 2
Change = 3
Delete = 4
Exit = 5


def main():
    try:
        input_file = open('customer_file.dat', 'rb')
        customers = pickle.load(input_file)
        print(customers)
        input_file.close()
    except (FileNotFoundError, IOError):
        print('File not found, please add a customer then quit to create the file')
        customers = {}

    choice = 0

    # while choice != Exit:
    choice = menu()
    print(choice)

    if choice == Look_up:
        look_up(customers)
    elif choice == Add:
        add(customers)
    elif choice == Change:
        change(customers)
    elif choice == Delete:
        delete(customers)
    elif choice == Exit:
        save(customers)


def menu():
    print('\nCustomer Email Lookup')
    print('-------------------------')
    print('1. Look up')
    print('2. Add')
    print('3. Change')
    print('4. Delete')
    print('5. Quit')
    # Under is the code that lets the user choose an option
    choice = 0
    while choice < 1 or choice > 5:
        choice = int(input('Enter a valid choice: '))
    return choice


def look_up(customers):
    name = input("Enter a customer's name: ")
    print(customers.get(name, 'Not Found'))


def add(customers):
    name = input("Enter a customer's name: ")
    email = input("Enter a customer's email: ")
    if name not in customers:
        user = {name: email}
        customers.update(user)
    else:
        print("That user already exists")
    save(customers)


def change(customers):
    name = input("Enter a customer's name: ")
    if name in customers:
        email = input("Please enter the new email address: ")
        customers[name] = email
        customers.update()
    else:
        print('That user does not exist')
    save(customers)


def delete(customers):
    name = input("Enter a customer's name: ")
    if name in customers:
        del customers[name]
    else:
        print("The customer was not found")
    save(customers)


def save(customers):
    print(customers)
    print("The data file has been updated with your changes. ")
    save_file = open('customer_file.dat', 'wb')
    pickle.dump(customers, save_file)
    save_file.close()
    menu()

main()
