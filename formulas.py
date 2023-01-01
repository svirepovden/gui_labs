#!/usr/bin/python3

import math


def semi_perim(a, b, c):
    return (a+b+c)/2


def is_positive(number):
    if number > 0:
        return number
    else:
        print("Некорректный ввод")
        return False


def herons_formula(a, b, c, p):
    result = math.sqrt( p * ( p - a ) * ( p - b ) * ( p - c ) )
    return result


def check_triangle_validity(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True


def triangle_area(a, b, c):
    if not(is_positive(a) and is_positive(b) and is_positive(c)):
        return "Только положительные числа"

    if check_triangle_validity(a, b, c):
        p = semi_perim(a, b, c)
        S = herons_formula(a, b, c, p)
        print(S)
        return S
    else:
        print("Triangle does not exist")
        return "Triangle does not exist"


def circle_area(r):
    if not is_positive(r):
        return "Только положительные числа"

    area = math.pi * r**2
    return area


def triangle_coordinates(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 0, 0, 0, 0, 0, 0
    # Calculate the semi-perimeter of the triangle
    s = semi_perim(a, b, c)

    # Calculate the area of the triangle using Heron's formula
    area = herons_formula(a, b, c, s)

    # Calculate the height of the triangle
    height = 2 * area / c

    # Calculate the coordinates of the vertices
    x1, y1 = 0, 0
    x2, y2 = c, 0
    x3, y3 = c / 2, height

    return x1, y1, x2, y2, x3, y3
