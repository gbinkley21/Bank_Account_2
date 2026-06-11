from BankAccUpdate import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, t_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)

        self.t_limit = t_limit
        self.t_made = 0

    def withdraw(self, am):
        if self.t_made >= self.t_limit:
            print(f"Transaction denied.")
        else:
            ini_balance = self.current_balance
            super().withdraw(am)

            if self.current_balance < ini_balance:
                self.t_made += 1
                print(f"Transaction made: {self.t_made}")
