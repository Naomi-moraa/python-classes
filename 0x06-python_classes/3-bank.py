#!/usr/bin/python3
"""Module that defines a BankAccount class with attributes and methods"""


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

    # Getter methods
    def get_name(self):
        """Return the account holder's name"""
        return self.__name

    def get_account_number(self):
        """Return the account number"""
        return self.__account_number

    def get_balance(self):
        """Return the current balance"""
        return self.__balance

    # Setter methods
    def set_name(self, name):
        """Set a new account holder's name"""
        self.__name = name

    def set_balance(self, amount):
        """Set a new balance"""
        self.__balance = amount

    # Deposit method
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount.")
