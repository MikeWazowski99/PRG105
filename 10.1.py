"""
10.1 Homework Personal Info Class Program

Create 3 instances that will hold your info, your family's info, and your friend's info

Info will be name, phone #, age ,and address
"""

class Info:
    def __init__(self, name, age, phone, address):
        self.__name = name
        self.__age = age
        self.__phone = phone
        self.__address = address

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def set_address(self, address):
        self.__address = address

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    def get_address(self):
        return self.__address


def main():
    info1 = Info("Name", "Age", "Phone Number", "Address")
    info2 = Info("Name", "Age", "Phone Number", "Address")
    info3 = Info("Name", "Age", "Phone Number", "Address")

    info1.set_name("Monkey")
    info1.set_age("20")
    info1.set_phone("815-888-9999")
    info1.set_address("1600 Address Wood")

    info2.set_name("Jacob")
    info2.set_age("18")
    info2.set_phone("815-777-8888")
    info2.set_address("1601 Address Wood")

    info3.set_name("Mom")
    info3.set_age("42")
    info3.set_phone("815-555-9898")
    info3.set_address("1602 Address Wood")

    print("\n\nPersonal: \n" + info1.get_name() + "\n" + info1.get_age() + "\n" + info1.get_phone() + "\n" + info1.get_address())
    print("\n\nFriend: \n" + info2.get_name() + "\n" + info2.get_age() + "\n" + info2.get_phone() + "\n" + info2.get_address())
    print("\n\nFamily: \n" + info3.get_name() + "\n" + info3.get_age() + "\n" + info3.get_phone() + "\n" + info3.get_address())


main()
