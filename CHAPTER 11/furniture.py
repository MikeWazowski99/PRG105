"""
11.1 Inheritance Program


"""
class OfficeFurniture:
    def __init__(self, material, length, width, height, price):
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def __str__(self):
        return 'The desk is: ' + self.__material + '\nThe chair is: ' + self.__length + \
            '\nThe width is ' + self.__width + '\nThe height is: ' + self.__height + '\nThe price is: ' + self.__price



