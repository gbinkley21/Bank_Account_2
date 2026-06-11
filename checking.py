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

if __name__== "__main__":
    print("Testing the checking account")

    c1 = CheckingAccount("A",1000.0,150.0,"AB123","AB000",2)
    c1.print_balance()

    c1.withdraw(200)
    c1.withdraw(300)
    c1.withdraw(50)

    c2 = CheckingAccount("B",100.0,10.0,"BC123","A8900",6)
    c2.print_balance()
    c2.withdraw(180)