class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited Amount : {amount}')
        
    def withdrawal(self, amount):
        if amount > self.balance:
            print('Insufficient Balance')
        else:
            self.balance -= amount
            print(f'Withdrawal Amount :{amount}')
            
    def check_balance(self):
        print(f'Available Balance :{self.balance}')
        
acc = BankAccount('Deepak', 20000)

acc.deposit(2000)
acc.withdrawal(23000)
acc.check_balance()
