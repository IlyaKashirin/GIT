class Account:
    def __init__(self, name, balance, history):
        self.name = name
        self.balance = balance
        self.history = history
    def replenish(self, up):
        self.balance += up
        self.history.append(f'Пополнение счета на {up} рублей')
    def withdraw(self, down):
        self.balance -= down
        self.history.append(f'Снятие со счета {down} рублей')

score = Account('ILYA', 0, [])
print(score.__dict__)
score.replenish(1000)
print(score.__dict__)
score.withdraw(300)
print(score.__dict__)
score.replenish(5000)
print(score.__dict__)


