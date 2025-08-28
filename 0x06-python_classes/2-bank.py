#!/usr/bin/python3
"""Module that defines a BankAccount class with attributes and getter methods"""


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

    def get_name(self):
        """Return the account holder's name"""
        return self.__name

    def get_account_number(self):
        """Return the account number"""
        return self.__account_number

    def get_balance(self):
        """Return the current balance"""
        return self.__balance
