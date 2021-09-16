total = 0
sales = 0
print("-----------------")
print("Day\t        Sales")
print("-----------------")

for counter in range(7):
    sales = float(input("Enter the amount of sales of everyday this week "))
    total = total + sales

print("-----------------")
print("Day\t        Sales")
print("-----------------")

for day in ("Monday ", "Tuesday", "Wednesday", "Thursday", "Friday  ", "Saturday", "Sunday  "):
    print(day, '\t', sales)
total_avg = total / 7
print("--------------------")
print("Your total sales of the week is ", + total)
print("Your total average per day is ", + total_avg)
