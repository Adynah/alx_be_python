class BankAccount:
    def __init__ (self, initial_balance=0):
        self.__account_balance = initial_balance
    
    def deposit (self, amount):
        if amount < 0:
            self.__acccount_balance += amount

    def withdraw (self, amount):
        if 0 < amount <= self.account_balance:
            return True
        return False
    
    def display_balance (self):
        print(f"Current Balance: ${self.__account_balance:.2f}")