"""
Name: Kiran G
Program: using oops create a python class called circle with constructor which will take a List as an argument for the task. 
The List is [10, 501, 22, 37, 100, 999, 87, 351]

"""

import math

class Circle:
    def __init__(self, radii):
        """Constructor that takes a list of radii."""
        self.radii = radii

    def area(self, radius):
        """Method to calculate the area of a circle given its radius."""
        return math.pi * radius ** 2

    def calculate_areas(self):
        """Method to calculate areas for all circles defined by the radii."""
        areas = []
        for radius in self.radii:
            areas.append(self.area(radius))
        return areas

    def display_areas(self):
        """Method to display the areas of the circles."""
        areas = self.calculate_areas()
        for radius, area in zip(self.radii, areas):
            print(f"Radius: {radius}, Area: {area:.2f}")

# Example usage
radii_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii_list)
circle.display_areas()
