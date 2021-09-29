class Account:

    def __init__(self, number, holder, balance, limit):
        print("Construindo objeto... {}".format(self))
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def statement(self):
        print("Saldo de R${} do titular {}.".format(
            self.__balance, self.__holder))

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def transfer(self, amount, destination):
        self.withdraw(amount)
        destination.deposit(amount)
