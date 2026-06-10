#!/usr/bin/env python3

class Coffee:
    """
    A class representing a coffee item in the bookstore.
    """
    def __init__(self, size, price):
        """
        Initialize a new Coffee object.

        Args:
            size (str): The size of the coffee (Small, Medium, or Large).
            price (float): The price of the coffee.
        """
        self.size = size
        self.price = price

    @property
    def size(self):
        """Get the size of the coffee."""
        return self._size

    @size.setter
    def size(self, value):
        """
        Set the size of the coffee.
        Validates that the size is one of: Small, Medium, Large.
        """
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        """
        Leave a tip for the coffee.
        Prints a message and increases the price by 1.
        """
        print("This coffee is great, here’s a tip!")
        self.price += 1
