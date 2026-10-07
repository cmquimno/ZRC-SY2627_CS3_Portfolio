class BankAccount:
    def __init__(self, account_number: int, balance: float):
        self.__account_number = account_number
        self.__balance = 0.0
        self.set_balance(balance)         

    def set_account_number(self, account_number: int):
        self.__account_number = account_number

    def set_balance(self, balance: float):
        if balance >= 0:
            self.__balance = float(balance)
        else:
            print("The balance must be not be a negative number.")

    @property
    def account_number(self) -> int:
        return self.__account_number

    @property
    def balance(self) -> float:
        return self.__balance

a1 = BankAccount(12345, 1000)

print("Account 1")
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")

print("\nUpdate balance to -100")
a1.set_balance(-100)

print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")                      
