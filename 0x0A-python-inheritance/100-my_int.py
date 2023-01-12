#!/usr/bin/python3
""" MyInt class """


class MyInt(int):
    """MyInt class (inherits int)"""

    def __eq__(self, value):
        """Checks out equality"""
        return self.real != value

    def __ne__(self, value):
        """Checks out non-equality"""
        return self.real == value
