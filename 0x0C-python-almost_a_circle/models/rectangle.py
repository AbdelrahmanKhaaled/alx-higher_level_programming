#!/usr/bin/python3
'''Module for rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''A rectangleclass.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width of rectangle'''
        return self.__width

    @width.setter
    def width(self, val):
        self.__width = val

    @property
    def height(self):
        '''height of rectangle'''
        return self.__height

    @height.setter
    def height(self, val):
        self.__height = val

    @property
    def x(self):
        '''x of rectangle'''
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        '''y of rectangle'''
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val
