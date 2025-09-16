#!/usr/bin/python3
"""Module that defines a BankAccount class with attributes"""


class BankAccount:
    """Class that defines a bank account"""

    def __init__(self, name, account_number):
        
        self._name = name
        self._account_number = account_number
        self._balance = 0
