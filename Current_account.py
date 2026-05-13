from Account import Account

class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdradft_limit =500):
        super().__init__(owner, balance)
        self.overdraft_limit =  overdradft_limit

    def withdraw(self, amount):
        available_funds = self.get_balance() + self.overdraft_limit
        if 0 < amount <= available_funds:
            print(f"withdrawal of ${amount}approved (using overdraft if necessary).")
        else:
            print("withdrawal denied: Exceeds Overdraft limit")
print ("\n---- CURRENT ACCOUNT----")
current = CurrentAccount ("Bob", 100)
current.withdraw(400)