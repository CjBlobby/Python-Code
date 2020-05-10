class Bankount():

    def __init__(self, owner="Sir", balance=100):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Owned by {self.owner} with a balance of £{self.balance}"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"{self.owner}, you do not have sufficient funds to withdraw £{amount}")
        
