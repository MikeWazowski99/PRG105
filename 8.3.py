"""
8.3 Homework

Read both files into lists
Check for any errors
Display customer information
"""


def main():
    try:
        account = open('accounts.txt', 'r')
        overdue = open('over90.txt', 'r')
        over = overdue.readlines()
        acct = account.readlines()
        for act in over:
            act = act.rstrip('\n')
            for accounts in acct:
                if act in accounts:
                    print(accounts)

        account.close()
        overdue.close()
    except IOError:
        print("File does not exist")


main()
