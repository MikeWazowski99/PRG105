import furniture


class Desk(furniture.OfficeFurniture):
    def __init__(self, material, length, width, height, price, location_of_drawers, number_drawers):
        furniture.OfficeFurniture.__init__(self, material, length, width, height, price)
        self.__location_of_drawers = location_of_drawers
        self.__number_drawers = number_drawers

    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    def set_number_drawers(self, number_drawers):
        self.__number_drawers = number_drawers

    def get_location_of_drawers(self):
        return self.__location_of_drawers

    def get_number_drawers(self):
        return self.__number_drawers

    def __str__(self):
        return '\nThe desk material is: ' + self.get_material() + '\nThe length is: ' + self.get_length() +\
            '\nThe width is: ' + self.get_width() + '\nThe height is: ' + self.get_height() +\
            '\nThe price is: ' + self.get_price() + '\nThe location of the drawers are on the: ' + self.get_location_of_drawers() +\
            '\nThe number of drawers is: ' + self.get_number_drawers()
