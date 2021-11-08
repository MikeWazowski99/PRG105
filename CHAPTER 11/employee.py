"""
11.2 Inheritance Program

Create an employee class and a sub class called production worker


"""


class Employee:
    def __init__(self, employee_name, employee_num):
        self.__employee_name = employee_name
        self.__employee_num = employee_num

    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set_employee_num(self, employee_num):
        self.__employee_num = employee_num

    def get_employee_name(self):
        return self.__employee_name

    def get_employee_num(self):
        return self.__employee_num

    def __str__(self):
        return "\nEmployee's Name: " + self.get_employee_name() + "Employee's # " + str(self.get_employee_num())


class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_num, shift_num, hourly_pay):
        Employee.__init__(self, employee_name, employee_num)

        self.__shift_num = shift_num
        self.__hourly_pay = hourly_pay

    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num

    def set_hourly_pay(self, hourly_pay):
        self.__hourly_pay = hourly_pay

    def get_shift_num(self):
        return self.__shift_num

    def get_hourly_pay(self):
        return self.__hourly_pay

    def __str__(self):
        return "\nEmployee Name: " + self.get_employee_name() + "\nEmployee Number: " + str(self.get_employee_num()) +\
            "Employee Shift: " + str(self.get_shift_num()) + "\nEmployee Pay Rate: " + str(self.get_hourly_pay())
