from os import name


class BankAccount:
    def __init__(self, holder_name, initial_balance=0):
        # Your code here: store holder_name, balance, and create empty transactions list
        self.name = holder_name
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount):
        # Your code here: add amount to balance and store transaction
        # Return new balance
        self.balance += amount
        self.transactions.append(f'Depost: +${amount}')
        return self.balance
    
    def withdraw(self, amount):
        # Your code here: subtract amount from balance if sufficient funds
        # If insufficient funds, print "Insufficient funds!"
        # Return new balance or None if withdrawal failed
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f'Withdraw: -${amount}')
            return self.balance
        else:
            print('Insufficient funds')

    
    def show_balance(self):
        # Your code here: print holder name and current balance
        print(f'Holder name: {self.name}  Current Balance: {self.balance}')
    

    def show_transactions(self):
        # Your code here: print all transactions
        for transaction in self.transactions:
            print(transaction)
    


# Test your code:
account = BankAccount("John Doe", 100)
account.deposit(50)    # Balance: 150
account.withdraw(70)   # Balance: 80
account.withdraw(100)  # Should print: "Insufficient funds!"
account.show_balance()
account.show_transactions()