
#!/usr/bin/python3

from bank6 import BankAccount

# Create a new bank account
account = BankAccount("John Doe", "123456789")

# Test deposits
account.deposit(1000)
account.deposit(500)

# Test withdrawals
account.withdraw(200)
account.withdraw(2000)  # Should show insufficient balance

# Print account details
print(account)

# Show transaction history
print("\nTransaction History:")
for transaction in account.get_transaction_log():
    print(f"{transaction['type']}: ${transaction['amount']}, Balance after: ${transaction['balance_after']}")
