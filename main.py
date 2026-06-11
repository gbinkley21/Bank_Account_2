#Put the instances here to check functionality
from SavingsAccount import SavingsAccount
from checking import CheckingAccount

#CheckingAccount instances





















#SavingsAccount Instances
#trying again 2
print("---- Savings Account #1 ----")
sav1 = SavingsAccount("S1", 1000, 100, 0.05)
sav1.print_balance()
sav1.deposit(200)
sav1.withdraw(300)
sav1.add_interest()
sav1.print_balance()

print("\n---- Savings Account #2 ----")
sav2 = SavingsAccount("S2", 5000, 200, 0.03)
sav2.print_balance()
sav2.deposit(500)
sav2.withdraw(1000)
sav2.add_interest()
sav2.print_balance()
