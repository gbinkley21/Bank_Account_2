
from SavingsAccount import SavingsAccount
from checking import CheckingAccount

print("----- Savings Account #1 -----")
sav1 = SavingsAccount("S1", 1000, 100, "S0000", "PPPPP", 0.05)

sav1.print_balance()
sav1.deposit(200)
sav1.withdraw(300)
sav1.add_interest()
sav1.print_balance()


print("\n----- Savings Account #2 -----")
sav2 = SavingsAccount("S2", 5000, 200, "SAV222", "TT888", 0.03)

sav2.print_balance()
sav2.deposit(500)
sav2.withdraw(1000)
sav2.add_interest()
sav2.print_balance()


print("\n----- Checking Account #1 -----")
chk1 = CheckingAccount("C1", 2000, 100, "CHK111", "PT888", 500)

chk1.print_balance()
chk1.deposit(300)
chk1.withdraw(200)
chk1.withdraw(400)
chk1.print_balance()


print("\n----- Checking Account #2 -----")
chk2 = CheckingAccount("C2", 3000, 100, "CHK222", "O03RT", 1000)

chk2.print_balance()
chk2.deposit(500)
chk2.withdraw(500)
chk2.withdraw(1200)
chk2.withdraw(800)
chk2.print_balance()