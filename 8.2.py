"""
8.2 Homework

Check if the data is valid or not
Tell user what bad data is
Find the total and average and display it
Display formatted results

"""


def main():
    try:
        file = open("rainfall-totals.txt", 'r')
    except IOError:
        print("File can not be found")
    rain_list = file.readlines()
    file.close()
    print(rain_list)
    total = 0
    count = 0


    for month in rain_list:
        rain_data = month.split()
        month = rain_data[0]
        inches = rain_data[1].rstrip("\n")
        print(inches)
        valid = True
        for item in inches:
            if not item.isdigit() and item != ".":
                valid = False
        if not valid:
            print("The data for " + month + " is " + inches + ", which is not numeric")
        else:
            total += float(inches)
            count += 1

    print("The total of valid entries is: " + format(total, ',.2f'))
    print("The total of valid entries is: " + format(total/count, ',.2f'))


main()
