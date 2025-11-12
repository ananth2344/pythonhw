
class Account:
    def __init__(self, name, balance):
        self._name = name        
        self._balance = balance  

    def display_details(self):
        return f"Account Holder: {self._name}, Balance: ₹{self._balance:.2f}"

    def __add__(self, other):
        if isinstance(other, Account):
            return self._balance + other._balance
        return NotImplemented

class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05  

class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02  

if __name__ == "__main__":
    savings = SavingsAccount("Ravi", 10000)
    current = CurrentAccount("Anjali", 15000)
    print("---- Savings Account ----")
    print(savings.display_details())
    print(f"Interest (5%): ₹{savings.calculate_interest():.2f}\n")
    print("---- Current Account ----")
    print(current.display_details())
    print(f"Interest (2%): ₹{current.calculate_interest():.2f}\n")
    total_balance = savings + current
    print("---- Total Balance ----")
    print(f"Combined Balance of Ravi and Anjali: ₹{total_balance:.2f}")
