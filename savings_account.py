from Account import Account

class SavingsAccount(Account):
    def __init__ (self,owner, balance=0, interest_rate=0.02, withdrawal_limit=100):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        self.withdrawal_limit = withdrawal_limit
    
    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest} applied")

    def withdraw(self, amount):
        # Check for invalid amount first
        if amount <= 0:
            print("Withdrawal must be a positive amount")
        elif amount > self.withdrawal_limit:
            print("Withdrawal limit exceeded")
        elif amount > self.get_balance():
            print("Insufficient funds")
        else:
            super().withdraw(amount)  # Let Account handle the actual balance update


print("--- Savings Account ---")
savings = SavingsAccount("Alice", 1000)
savings.apply_interest()
savings.withdraw(80)
print(savings.withdrawal_limit)  # attribute, no parentheses