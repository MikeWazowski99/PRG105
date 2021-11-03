import desk
import furniture


def main():
    my_furniture = furniture.OfficeFurniture('Stone', '6 feet', '2 feet', '50 inches', '$1200')
    print(my_furniture)

    my_desk = desk.Desk('Wood', '8 feet', '2 feet', '50 inches', '$1000', 'Left', '2')
    print(my_desk)


main()
