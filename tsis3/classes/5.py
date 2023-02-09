class Account:
    owner = "Amanbol Kanatuly"
    balance = 0

    def __init__(self, name, cash):
        self.owner = name
        self.balance = cash

    def deposit(self, cash):
        self.balance += cash

    def withdraw(self, cash):
        if self.balance < cash:
            print("Not enough money")
        else:
            self.balance -= cash


me = Account("Amanbol", 100)
print(me.balance)
me.deposit(100)
print(me.balance)
me.withdraw(100)
print(me.balance)
me.withdraw(150)
print(me.balance)
me.withdraw(100)
print(me.balance)

