# Credit Score Homework

Credit = int(input("What is your credit score"))

if Credit <= 629:
    print("You have a Bad Credit Score")
elif 630 <= Credit <= 689:
    print("You have a Poor Credit Score")
elif 680 <= Credit <= 719:
    print("You have a Good Credit Score")
elif 720 <= Credit <= 850:
    print("You have an Excellent Credit Score")

