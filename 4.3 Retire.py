"""
4.3 Retirement Plan Homework

Make a retirement plan that tells user when they can retire with the time it will take them to retire and stuff

contribution = income * saving %

Got help from a tutor
"""

year = 1
age = int(input("How old are you? "))
retire = int(input("What age would you like to retire? "))
income = float(input("What is your yearly income? "))
save = float(input("What percentage of your income do you save? "))
percentage = save/100
savings = float(input("How much do you already have saved? "))
total_savings = savings
contribution = income/save

print("\nThis projection assumes a 3% raise each year and a 6% yearly return on investment\n")


print("Year \t Income \t Savings Contributions \t Total Savings")
years = retire - age
while year < years + 1:
    print(format(year, '2.0f') + format(income, "13,.0f") + format(contribution, "20,.0f") + format(total_savings, "24,.0f"))
    year += 1
    income = income * 1.03
    contribution = income/save
    total_savings = savings * 1.06
    total_savings += contribution
