class Account:

    def __init__(self, number, holder, balance, limit):
        print("Construindo objeto... {}".format(self))
        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit

    def statement(self):
        print("Saldo de R${} do titular {}.".format(self.balance, self.holder))

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
