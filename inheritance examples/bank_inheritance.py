class BasicAccount:
    def __init__(self, holder_name, balance=0):
        self.holder = holder_name
        self.balance = balance
        self.type = "Basic Account"
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

# SavingsAccount inherits from BasicAccount
class SavingsAccount(BasicAccount):
    def __init__(self, holder_name, balance=0):
        # Call parent's __init__ first
        super().__init__(holder_name, balance)
        # Add savings-specific attributes
        self.type = "Savings Account"
        self.interest_rate = 0.05  # 5% interest
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)  # Uses parent's deposit method
        print(f"Added ${interest} in interest")

# Test the accounts:
print("=== Basic Account ===")
basic = BasicAccount("John")
basic.deposit(100)    # From BasicAccount
basic.withdraw(50)    # From BasicAccount
print(f"\nAccount type: {basic.type}")  # "Basic Account"

print("\n=== Savings Account ===")
savings = SavingsAccount("Mary")
savings.deposit(100)  # Inherited from BasicAccount
savings.add_interest()  # New method in SavingsAccount
print(f"Account type: {savings.type}")  # "Savings Account"