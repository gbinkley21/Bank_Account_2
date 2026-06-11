from BankAccUpdate import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):

        super().__init__(
            customer_name,
            current_balance,
            minimum_balance
        )

        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest

        print(f"Interest added: ${interest:.2f}")
        print(f"New Balance: ${self.current_balance:.2f}")

    if __name__ == "__main__":

        sav1 = SavingsAccount("S1", 1000, 100, 0.05)
        sav1.print_balance()
        sav1.add_interest()
        sav1.print_balance()

        print("\n")

        sav2 = SavingsAccount("S2", 5000, 200, 0.03)
        sav2.print_balance()
        sav2.add_interest()
        sav2.print_balance()