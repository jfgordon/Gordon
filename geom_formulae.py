__author__ = 'joseph'
from numbers import Number
from math import *


def rectangle_area(length, breadth) -> Number:

    """
    calculate the area of the rectangle
    :param length: the length
    :param breadth: the breadth
    :return: The area of the rectangle
    >>> rectangle_area (5,4)
    20
    """
    return length*breadth


def rhombus_area(diagonal1, diagonal2) -> Number:
    """

    :param diagonal1: the length of diagonal1
    :param diagonal2: the length of diagonal2
    :return:the area of rhombus
    >>> rhombus_area (6,4)
    12
    """
    return 0.5*diagonal1*diagonal2


def rhombus_area2(base, height) -> Number:
    """
    Find the area of rhombus
    :param base: length of the base
    :param height: length of the height
    :return:the area of rhombus
    >>> rhombus_area(3,5)
    15
    """
    return base*height


def circle_area(radius) -> Number:
    """
    Calculate the area of a circle
    :param radius: the radius
    :return:the area of circle
    >>> circle_area(2)
    12.568
    """
    return pi*radius*radius


def triangle_area(base, height) -> Number:
    """
    Calculate the area of the triangle
    :param base: the base
    :param height: the height
    :return:the area of triangle
    >>> triangle_area(4,3)
    6
    """
    return 0.5*base*height


def cube_volume(length) -> Number:
    """
    Calculate the volume of a cube
    :param length: the length
    :return:the volume of a cube
    >>> cube_volume(3)
    27
    """
    return length * length * length


def cuboid_volume(length, breadth, height) -> Number:
    """
    Calculate the volume of a cuboid
    :param length:the length
    :param breadth: the breadth
    :param height: the height
    :return:volume of a cuboid
    >>> cuboid_volume(3,4,5)
    60
    """
    return length*breadth*height


def kite_area(diagonal1, diagonal2) -> Number:
    """
    Calculate the area of a kite
    :param diagonal1: the length of diagonal1
    :param diagonal2: the length of diagonal2
    :return:the area of a kite
    >>> kite_area(5,10)
    25
    """
    return 0.5*diagonal1*diagonal2


def trapezium_area(parallel1, parallel2, height) -> Number:
    """
    Calculate the area of a trapezium
    :param parallel1: the parallel1 side
    :param parallel2: the parallel2 side
    :param height: the height
    :return:area of a trapezium
    >>> trapezium_area(3,5,4)
    16
    """
    return 0.5*(parallel1+parallel2)*height


def parallelogram_area(base, height) -> Number:
    """
    Calculate the area of a parallelogram
    :param base: the base
    :param height: the height
    :return:area of a parallelogram
    >>> parallelogram_area(3,5)
    15
    """
    return base*height


def cylinder_volume(radius, height) -> Number:
    """
    Calculate the volume of a cylinder
    :param radius: the radius
    :param height: the height
    :return:the volume of a cylinder
    >>> cylinder_volume(7,5)
    769.6902001294993
    """
    return pi*radius*radius*height