def Check_balance(balance):
    print(f"Your balance ₹{balance:.2f}")

def deposit():
    amount = int(input("Enter the amount you want to add: "))
    if amount < 0:
        print("Amount cannot be negative")
        return 0
    else:
        return amount        

def withdraw(balance):
    amount = int(input("Enter amount you want to remove: "))
    if amount > balance:
        print("Insufficient balance")
        return 0
    elif amount < 0:
        print("Amount cannot be negative")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True
    while is_running:
        print("***************")
        print("Welcome to Bank")
        print("1 Check balance") 
        print("2 Deposit")
        print("3 Withdraw amount")
        print("4 Exit")
        val = int(input("Enter operation you want to perform: "))
        if val == 1:
            Check_balance(balance)
        elif val == 2:
            balance += deposit()
        elif val == 3:
            balance -= withdraw(balance)
        elif val == 4:
            print("Thank you for visiting the bank.")
            is_running = False
        else:
            print("Invalid entry")

if __name__ == '__main__':
    main()
