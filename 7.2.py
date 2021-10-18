"""
7.2 Program

Create a coded message from the users txt and write it in a txt file

"""


def main():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                ' ', ',', '?', '!', '.']

    code = ['`', '@', '#', '$', '%', '^', '&', '*', '-', '+', '1', '2', '3',
            '4', '5', '6', '7', '8', '9', ' ', '_', 'q', 'w', 'e', 'r', 't',
            'y', 'u', 'i', 'p', ';', ':', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
            ',', '.', '?', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'P', 'A',
            'S', 'D', '?', '!', '.']

    coded_file = open('coded.txt', 'w')
    message = input('Please enter the message you want to be coded ')
    for letter in message:
        my_index = alphabet.index(letter)
        letter_out = code[my_index] + '\n'
        coded_file.write(letter_out)
    coded_file.close()


main()
