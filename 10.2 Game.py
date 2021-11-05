"""
10.2 Game Trivia

Import questions from questions.py

Create 10 sets of 4 questions
Need 2 players to answer 5 questions each which will determine who is the winner
"""

import questions


def main():
    q1 = questions.Questions("What is the name of the biggest technology company in South Korea", "A. Apple",
                             "B. Microsoft", "C. Samsung", "D. SAP", "C")

    q2 = questions.Questions("Which animal can be seen on the Porsche logo?", "A. Frog", "B. Horse", "C. Bull", "D. Cat", "B")

    q3 = questions.Questions("Which two countries have not missed one of the modern-day Olympics?", "A. Greece + Australia", "B. USA + Canada",
                             "C. Japan + Brazil", "D. Canada + France", "A")

    q4 = questions.Questions("What sport is dubbed the 'king of the sports'", "A. Soccer", "B. Football", "C. Basketball", "D. Baseball", "A")

    p1 = 0      # Player 1's Score
    p2 = 0      # Player 2's Score

    set_1 = [q1, q2]
    set_2 = [q3, q4]

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

    print('Player 1 earned ' + str(p1) + " points.")

main()
