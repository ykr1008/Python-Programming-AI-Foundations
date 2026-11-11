"""bank.py - a small class hierarchy demonstrating the four OOP pillars."""
import re
from abc import ABC, abstractmethod


class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount:.2f}; balance is only {balance:.2f}")


class Account(ABC):
    def __init__(self, number, owner, balance=0.0):
        if not self.validate_account_number(number):
            raise ValueError(f"Invalid account number: {number!r}")
        self.number = number
        self.owner = owner
        self.__balance = 0.0          # name-mangled -> _Account__balance
        if balance:
            self.deposit(balance)

    # --- encapsulation: read-only view of the balance ---
    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.__balance:
            raise InsufficientFundsError(self.__balance, amount)
        self.__balance -= amount

    # --- abstraction: every subclass MUST implement this ---
    @abstractmethod
    def calculate_interest(self):
        ...

    # --- alternative constructor ---
    @classmethod
    def from_dict(cls, data):
        return cls(data["number"], data["owner"], data.get("balance", 0.0))

    # --- utility that needs neither cls nor self ---
    @staticmethod
    def validate_account_number(number):
        return isinstance(number, str) and re.fullmatch(r"\d{10}", number) is not None

    def __str__(self):
        return f"{type(self).__name__} #{self.number} ({self.owner}): {self.balance:,.2f}"

    def __repr__(self):
        return (f"{type(self).__name__}(number={self.number!r}, "
                f"owner={self.owner!r}, balance={self.balance!r})")


class SavingsAccount(Account):
    RATE = 0.04  # 4% a year

    def calculate_interest(self):
        return self.balance * self.RATE


class CurrentAccount(Account):
    RATE = 0.001  # 0.1% a year

    def calculate_interest(self):
        return self.balance * self.RATE


if __name__ == "__main__":
    s = SavingsAccount.from_dict({"number": "1234567890", "owner": "Yadhu", "balance": 1000})
    c = CurrentAccount("0987654321", "Yadhu", 1000)

    # polymorphism: same call, different behaviour
    for acct in (s, c):
        print(acct, "-> interest:", acct.calculate_interest())
    print(repr(s))

    # encapsulation
    try:
        s.balance = 1_000_000
    except AttributeError as e:
        print("No setter:", e)
    print("Mangled name:", s._Account__balance)   # reachable, but a deliberate 'keep out' signal

    # custom exception
    try:
        s.withdraw(5000)
    except InsufficientFundsError as e:
        print("Caught:", e)

    # abstraction
    try:
        Account("1234567890", "X")
    except TypeError as e:
        print("Abstract:", e)

    print(Account.validate_account_number("123"), Account.validate_account_number("1234567890"))