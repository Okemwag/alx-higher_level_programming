#!/usr/bin/python3
""" Magic class """
import math


class MagicClass:
    """ Defines the Magic Class"""

    def __init__(self, radius=0):
        """Initialize class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """ Calculates the area """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ Calculate the circumference"""
        return (2 * math.pi) * self.__radius
