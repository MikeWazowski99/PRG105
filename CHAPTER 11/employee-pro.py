"""
11.2 Inheritance

Import the stuff into here and ask the user to put data
"""

from employee import *


def main():
    name = input("Employee's name: ")
    num = input("Employee's # ")
    shift = int(input("Employee's Shift: "))
    pay = input("Employee's pay rate: ")
    if shift == 1:
        shift = str("Day")
    elif shift == 2:
        shift = str("Night")

    new_employee = ProductionWorker(name, num, shift, pay)

    # new_employee.set_employee_name(input("Please give me a name: "))
    # new_employee.set_employee_num(input("give employee id: "))
    # print(new_employee.get_employee_name())
    # print(new_employee.get_employee_num())

    print("\nEmployee Name: " + new_employee.get_employee_name() + "\nEmployee's #: " + new_employee.get_employee_num() +
         "\nEmployee's Shift: " + new_employee.get_shift_num() + "\nEmployee's pay rate: " + new_employee.get_hourly_pay())


main()
