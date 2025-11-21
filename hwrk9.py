from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    def account_age(self):
        current_year = 2025
        return current_year - self.account_year
    @abstractmethod
    def get_role(self):
        pass

class Admin(User):
    def get_role(self):
        return "Admin"
    def __str__(self):
        return f"{self.name} is an {self.get_role()} with an account age of {self.account_age()} years."

class Guest(User):
    def get_role(self):
        return "Guest"

    def __str__(self):
        return f"{self.name} is a {self.get_role()} with an account age of {self.account_age()} years."

admin_user = Admin("Alice", 2018)
guest_user = Guest("Bob", 2023)
print(f"Role: {admin_user.get_role()}")
print(f"Account Age: {admin_user.account_age()} years")
print(admin_user)
print()
print(f"Role: {guest_user.get_role()}")
print(f"Account Age: {guest_user.account_age()} years")
print(guest_user)
