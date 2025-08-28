class BankAccount:
    def __init__(self, name, account_number):
        self.__name = name
        self.__account_number = account_number
        self.__balance = 0
        self.__transactions = []

    # Getter methods
    def get_name(self):
        return self.__name

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_transaction_log(self):
        return self.__transactions

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_balance(self, amount):
        self.__balance = amount

    # Transaction methods
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.log_transaction("deposit", amount)
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                self.log_transaction("withdraw", amount)
            else:
                print("Insufficient funds")
        else:
            print("Withdrawal amount must be positive")

    def log_transaction(self, trans_type, amount):
        transaction = {
            "type": trans_type,
            "amount": amount,
            "balance_after": self.__balance
        }
        self.__transactions.append(transaction)
