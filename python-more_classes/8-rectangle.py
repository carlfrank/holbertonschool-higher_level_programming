#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle"""


class Rectangle:
    """A magical Rectangle class that can compare who's the biggest!"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Make a new magical rectangle!"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # ... [rest of the properties and methods remain the same as before]

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Rectangle is the biggest, or if they're both just as magical!"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

# Example usage
# r1 = Rectangle(3, 5)
# r2 = Rectangle(4, 4)
# biggest = Rectangle.bigger_or_equal(r1, r2)
# print(biggest)
