"""
student: $5.00
Veteran: $7.00
Show Sponsor: $2.00
Retiree: $6.00
General public: $10.00



People buying 4 - 8 tickets get a 10% discount.

People buying 9-15 tickets get a 15% discount.

People buying more than 15 tickets get a 20% discount
"""

print("1. Student\n2. Veteran\n3. Show Sponsor")

customer = int(input("Please select the number that correlates to you the most: "))

price = 10.00

if customer == 1:
    price = 5.00
elif customer == 2:
    price = 7.00
elif customer == 3:
    price = 2.00
else:
    price = 10.00

tickets = int(input("How many tickets would you like to purchase? "))
total = price * tickets
print("The total amount before the discount is: $" + format(total, ",.2f"))

discount = 0

if tickets > 15:
    discount = .20
if tickets <= 15:
    discount = .15
if tickets <= 8:
    discount = .10

total_discount = total * discount
overall_total = total - total_discount

print("The amount of tickets you purchased have a % " + format(discount, '.2f') + " discount")
print("The overall total is: $" + format(overall_total, ",.2f"))
