#!/usr/bin/python3
from models.base import Base
"""A class Rectangle that inherit from the base"""
class Rectangle(Base):
    """Class constructor"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): An optional integer ID.

        Attributes:
            id (int): The unique ID for each instance.
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
