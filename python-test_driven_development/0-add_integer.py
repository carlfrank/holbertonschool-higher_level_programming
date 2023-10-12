
"""This module contains a function that adds two integers."""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
    - a: The first integer to add.
    - b: The second integer to add.

    Returns:
    - The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
