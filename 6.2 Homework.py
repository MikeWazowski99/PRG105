"""
6.2 Reading files in a program Homework

Count all the numbers and add them all up to the running total and then format and display them

"""


def main():
    sales_info = open('sales_totals-1.txt', 'r')
    total = 0.0
    count = 0
    print("Here are the total sales")
    line = sales_info.readline()
    while line != '':
        amount = float(line)
        count += 1
        print('Sale #', count, ': ', format(amount, ',.2f'), sep='', )
        total += amount
        print(format(total, ',.2f'))
        line = sales_info.readline()
        average = total/count
        print('\n' + 'The total average is: ' + format(average, '22,.2f'))
    sales_info.close()
    print("The total amount of sales is: " + format(total, '15,.2f'))
    print('The total number of entries is:', format(count, '8,.2f'))


main()
