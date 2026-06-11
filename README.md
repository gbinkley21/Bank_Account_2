# Bank_Account_2
# Bank Account Inheritance Project

## Group Members
- Gavin Binkley
- Bindu Harini Gunturi

## Project Description
This project demonstrates object-oriented programming concepts in Python using inheritance.

The project extends a base `BankAccount` class by creating:

- `SavingsAccount` – supports interest accumulation
- `CheckingAccount` – includes transfer limitations

The program also demonstrates:

- Inheritance
- Class attributes
- Instance attributes
- Private members
- Method overriding and extension
- Multiple account instances
- Module imports

## File Structure

```text
BankAccUpdate.py      # Base BankAccount class
SavingsAccount.py     # Savings account subclass
CheckingAccount.py    # Checking account subclass
```

## Features

### BankAccount
- Deposit funds
- Withdraw funds
- Minimum balance protection
- Display account information

### SavingsAccount
- Inherits from BankAccount
- Applies interest to account balance

### CheckingAccount
- Inherits from BankAccount
- Supports transfers with a transfer limit
