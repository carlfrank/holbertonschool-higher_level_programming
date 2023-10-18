#!/usr/bin/python3
"""Write a class MyList that inherits from list"""


class MyList(list):
    """
    This class inherts from list"""
    def print_sorted(self):
        """This function prints in ascending order of integers"""
        list_sorted = []
        for num in self:
            list_sorted.append(num)
        list_sorted.sort()
