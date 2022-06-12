from math import sqrt
from random import randint, random


def calc_equation_sqrt(a: float, b: float, c: float):
    if a == 0 or (discriminant := (b**2 - 4 * a * c)) < 0:
        return False,
    elif discriminant == 0:
        return -1 * b / (2 * a),
    else:
        return (-1 * b + sqrt(discriminant)) / (2 * a), (-1 * b - sqrt(discriminant)) / (2 * a)


def rand_colors(blue: int = 0, green: int = 0, red: int = 0):
    print(blue, green, red)
    if blue == green == red == 0:
        pass
    elif green >= blue - 1:
        return "b"
    elif red >= green:
        return "g"
    if (dice := randint(1, 10)) % 2:
        return "b"
    elif dice in (4, 6):
        return "r"
    else:
        return "g"
