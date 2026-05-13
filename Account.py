class Account:
    def __init__ (self,owner,balance=0):
        self.owner = owner
        self.__balance = balance
    
    def deposit (self,amount):
        if amount > 0:
            self.__balance += amount
            print (f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive and greater than zero")

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"withdrawed amount ${amount}. balance: ${self.__balance}")
        else:
            print ("invailid withdrawql amount or insufficient funds.")

    def get_balance(self):
        return self.__balance
    