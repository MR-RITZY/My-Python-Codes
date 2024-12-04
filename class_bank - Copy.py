#import pyinputplus as pyin
class Bank_account():
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    def display(self):
        print(f'Dear {self.name},')
        print(f'Your account balance is: #{self.balance:.2f}.')
    def withdraw(self, amount):
        self.amount = amount
        self.balance -= self.amount
    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
myaccount = Bank_account('Faruq')
myaccount.deposit(1000)
myaccount.withdraw(200)
myaccount.display()
