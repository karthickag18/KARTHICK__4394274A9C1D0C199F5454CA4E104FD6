
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"${amount} deposited successfully."
        else:
            return "Deposit amount must be greater than zero."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"${amount} withdrawn successfully."
        elif amount > self.__account_balance:
            return "Insufficient funds."
        else:
            return "Withdrawal amount must be greater than zero."

    def display_balance(self):
        return f"Account Balance: ${self.__account_balance}"

# Test the BankAccount class
if __name__ == "__main__":
    account = BankAccount("12345", "John Doe", 1000)

    print(account.display_balance())  # Display initial balance
    print(account.deposit(500))       # Deposit $500
    print(account.display_balance())  # Display updated balance

    print(account.withdraw(200))      # Withdraw $200
    print(account.display_balance())  # Display updated balance
    print(account.withdraw(1500))     # Attempt to withdraw $1500 (insufficient funds)
