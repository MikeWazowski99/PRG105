""""
5.1 Menu Homework

Make a menu with 5 things that you're interested in and when the user types it into the console print the
following information about that topic/thing


"""

print("Select one of the following menu options to learn more about it. \nA. Video Games \nB. Books \nC. Pets\nD. Movies \nE. Coding")


def main():
    x = input("Please enter the letter of your choosing to learn about one of the topics ")
    if x == "A":
        main2()
    elif x == "B":
        main3()
    elif x == "C":
        main4()
    elif x == "D":
        main5()
    elif x == "E":
        main6()


def main2():
    print("\nVideo games are games that can be played online on a computer,laptop,console or your phone and for the most part are a good form of entertainment because of all the different generes of games")
    print("You can either play a single player game or a multiplayer game both of which can be an amazing experience since you can play a story single player game or a multiplayer game with your friends.")


def main3():
    print("\nBooks can be an amazing way to learn certain things or can be an amazing way of entertainment. For example you can learn how to code with the Starting out with python Book or Ebook.")
    print("There also a variety of books in the world such as fiction, non fiction, biography, novels, etc.")


def main4():
    print("\nPets are one of the best friends that you can have in this world because of how funny they can be or how playful they can be and just the way they act can make you happy. Whether its a dog or a cat")
    print("you can always have fun with a pet. For example if you want a playful and energetic friend you can get a dog because they are usually very energetic but if you want a pet that is relaxed and is cute get a cat")


def main5():
    print("\nMovies are one of the most popular things in this world because of how big and ambitious some movies have become such as The Avengers Endgame which had used CGI in such a way that made it feel as if it was happening in real life")
    print("Not only that there are other movies that all have different generes such as Romantic movies, Action movies, Horror Films, Mysterious movies, and the list could go on and on about all the movies generes")


def main6():
    print("\nCoding is one of the hardest things to learn but can be one of the most interesting skills you can learn in life mainly because of the fact that you are not limited with what you can make.")
    print("For example you can make a robot that can do clean like a Roomba or you can create a program on your computer that can tell you when there is a sale going on somewhere on the internet or you can make a video game.")
    print("As long as you have the time and resources to program something you can make almost anything you want which makes coding one of the most interesting things in the world")


main()
