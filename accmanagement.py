class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def check_balance(self):
        return f"Current balance for {self.account_holder}'s account: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount:.2f} deposited. New balance: ${self.balance:.2f}"
        else:
            return "Invalid deposit amount. Please enter a positive amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"${amount:.2f} withdrawn. New balance: ${self.balance:.2f}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Please enter a positive amount."
        else:
            return "Insufficient funds. Withdrawal cannot be processed."

# Example usage:
if __name__ == "__main__":
    # Create a new account
    account1 = BankAccount("Dibya Ranjan Pati", 1000.00)

    # Check initial balance
    print(account1.check_balance())

    # Make a deposit
    print(account1.deposit(500.50))

    # Make a withdrawal
    print(account1.withdraw(200.25))

    # Check the final balance
    print(account1.check_balance())
