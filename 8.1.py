"""
Homework 8.1

Get user to type a string
Make that into an acronym
"""

def main():
    phrase = input("Please enter a phrase you would like to be converted into an acronym ")
    phrase_list = phrase.split()
    acronym = ""
    for word in phrase_list:
        letter = word[0]
        acronym += word[0]
    print(acronym.upper())


main()
