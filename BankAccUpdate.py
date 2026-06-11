class BankAccount:

    bank_t = "Truist Bank"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, d_amount):
        if d_amount > 0:
            self.current_balance += d_amount
            print(f"${d_amount} deposited.")
            print(f"New balance: ${self.current_balance}")
        else:
            print("Invalid amount.")

    def withdraw(self, d_amount):
        if self.current_balance - d_amount < self.minimum_balance:
            print(f"Cannot withdraw ${d_amount}. No balance left.")
        elif d_amount < 0:
            print("Amount must be positive.")
        else:
            self.current_balance -= d_amount
            print(f"${d_amount} withdrawn.")
            print(f"New balance: ${self.current_balance}")


    def print_balance(self):
        print(f"\n- {BankAccount.bank_t} -")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: ${self.current_balance}")
        print(f"Minimum Balance: ${self.minimum_balance}")

if __name__ == "__main__":

    acc1 = BankAccount("A1", 300, 100)
    acc1.print_balance()

    acc1.deposit(100)
    acc1.withdraw(100)
    acc1.withdraw(700)  # This should nto work.

    acc1.print_balance()

    print("\n")

    acc2 = BankAccount("A2", 300, 100)
    acc2.print_balance()

    acc2.deposit(300)
    acc2.withdraw(200)
    acc2.deposit(-200)  # This should not work.
    acc2.withdraw(700)  # This should not work.

    acc2.print_balance()