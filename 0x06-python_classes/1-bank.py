#!/usr/bin/python3
"""Module that defines a BankAccount class with attributes"""


class BankAccount:
    """Class that defines a bank account"""

    def __init__(self, name, account_number):
        """Initialize a new bank account
        Args:
            name (str): account holder's name
            account_number (str): account number
        """
        self.__name = name
        self.__account_number = account_number
        self.__balance = 0
