# 4.2 Song Homework
# Make a song that will take a bottle down until it reaches 0 

num = int(input("How many bottles are there on the wall? "))

while num > 0:
    print(num, "Bottles of beer on the wall")
    print(num, "bottles of beer")
    print("Take one down, pass it around")
    num = num - 1
    print(num, "bottles of beer on the wall\n\n")
