#!/usr/bin/python3
""" Module """


class Square:
    """ Define the Square Class    """
    def __init__(self, size=0, position=(0, 0)):
        """initialize """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Getter of size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter of size """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Get postion attribute """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter of position """
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Get area """
        return self.__size ** 2

    def my_print(self):
        """ Print a square """
        if self.size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)

    def __str__(self):
        """ Defining printing behavior of the class """
        if self.__size == 0:
            return ''
        new_lines = '\n' * self.position[1]
        spaces = ' ' * self.position[0]
        hashes = '#' * self.size
        return new_lines + '\n'.join(spaces + hashes for e in range(self.size))
