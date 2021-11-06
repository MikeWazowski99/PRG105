"""
10.2 Game Trivia
Import questions from questions.py
Create 10 sets of 4 questions
Need 2 players to answer 5 questions each which will determine who is the winner
"""

import questions


def main():
    q1 = questions.Questions("What is the name of the biggest technology company in South Korea?", "A. Apple",
                             "B. Microsoft", "C. Samsung", "D. SAP", "C")

    q2 = questions.Questions("Which animal can be seen on the Porsche logo?", "A. Frog", "B. Horse", "C. Bull", "D. Cat", "B")

    q3 = questions.Questions("Which two countries have not missed one of the modern-day Olympics?", "A. Greece + Australia", "B. USA + Canada",
                             "C. Japan + Brazil", "D. Canada + France", "A")

    q4 = questions.Questions("What sport is dubbed the 'king of the sports'", "A. Soccer", "B. Football", "C. Basketball", "D. Baseball", "A")

    q5 = questions.Questions("What is Earth's largest continent?", "A. America", "B. Europe", "C. Asia", "D. Australia", "C")

    q6 = questions.Questions("Which country won the first-ever soccer World Cup in 1930?", "A. Mexico", "B. Japan", "C. USA", "D. Uruguay", "D")

    q7 = questions.Questions("What was the first feature-length animated movie ever released?", "A. Cinderella", "B. Snow White and the Seven Dwarfs"
                             , "C. Shrek", "D. Beauty and the Beast", "B")

    q8 = questions.Questions("What is the opposite of matter?", "A. White Matter", 'B. Black holes', 'C. Antimatter', "D. Zero-Matter", "C")

    q9 = questions.Questions("A group of ravens is known as?", "A. Unkindness", "B. Flock", "C. Pairs", "D. Murder", "A")

    q10 = questions.Questions("Which of Newton’s Laws states that ‘for every action, there is an equal and opposite reaction?",
                              "A. 1st Law", "B. 2nd Law", "C. 3rd Law", "D. 4th Law", "C")

    p1 = 0      # Player 1's Score
    p2 = 0      # Player 2's Score

    set_1 = [q1, q2]
    set_2 = [q3, q4]
    set_3 = [q5, q6]
    set_4 = [q7, q8]
    set_5 = [q9, q10]

    print("Player 1: ")
    for query in set_1:
        print("\n")
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Please enter the letter that you think is the correct answer: ")
        if guess.upper() == query.get_answer():
            print("That is the right answer!")
            p1 += 1
        elif guess.upper() != query.get_answer():
            print("That is not the right answer")

    print('Player 1 earned ' + str(p1) + " points.")

    print("\nPlayer 2: ")
    for query in set_2:
        print("\n")
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Please enter the letter that you think is the correct answer: ")
        if guess.upper() == query.get_answer():
            print("That is the right answer!")
            p2 += 1
        elif guess.upper() != query.get_answer():
            print("That is not the right answer")

    print('Player 2 earned ' + str(p2) + " points.")

    print("\nPlayer 1: ")
    for query in set_3:
        print("\n")
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Please enter the letter that you think is the correct answer: ")
        if guess.upper() == query.get_answer():
            print("That is the right answer!")
            p1 += 1
        elif guess.upper() != query.get_answer():
            print("That is not the right answer")

    print('Player 1 earned ' + str(p1) + " points.")

    print("\nPlayer 2: ")
    for query in set_4:
        print("\n")
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Please enter the letter that you think is the correct answer: ")
        if guess.upper() == query.get_answer():
            print("That is the right answer!")
            p2 += 1
        elif guess.upper() != query.get_answer():
            print("That is not the right answer")

    print('Player 2 earned ' + str(p2) + " points.")

    print("\nPlayer 1: ")
    for query in set_5:
        print("\n")
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Please enter the letter that you think is the correct answer: ")
        if guess.upper() == query.get_answer():
            print("That is the right answer!")
            p1 += 1
        elif guess.upper() != query.get_answer():
            print("That is not the right answer")

    print('Player 1 earned ' + str(p1) + " points.")

    print('Player 1 earned ' + str(p2) + " points.")
    if p1 > p2:
        print("Player 1 is the winner with " + str(p1), "points!")
    elif p2 > p1:
        print("Player 2 is the winner with " + str(p2), "points!")
    elif p1 == p2:
        print("Both players got the same amount of points so the result is a draw!")


main()
