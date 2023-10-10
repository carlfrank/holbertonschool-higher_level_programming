#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """Square class with a private attribute -
    size.
    """

    def __init__(self, size=0):
        """Initializes the size variable as a private
        instance artribute
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the value
        of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to protect and set the value
        of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method that returns
        the current square area
        """
        return self.__size ** 2
