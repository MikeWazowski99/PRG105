# Financial Aid Homework
Eligible = True

student = input("Are you are returning student? Answer with either Y or N ")
gpa = float(input("What is your gpa? "))
crime = input("Have you had a criminal record for drugs? Answer with either Y or N ")
classes = int(input("How many credit hour of classes are you taking? "))
money = int(input("What is your gross yearly income? "))

if student == "Y" or student == "y":
    Eligible = False
if gpa < 2.0:
    Eligible = False
if crime == "Y" or crime == "y":
    Eligible = False
if classes < 6:
    Eligible = False
if money > 50000:
    Eligible = False

if Eligible:
    print("You are eligible for financial aid")
else:
    print("You are not eligible for financial aid")
