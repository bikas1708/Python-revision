# Program a banking app in PYTHON


def show_bal(balance):
    print("***************************")
    print(f"Your Balance is ${balance:.2f}")
    print("***************************")


def deposit():
    print("***************************")
    amount: float = float(input("Enter an amount to be deposited: "))
    print("***************************")
    if amount < 0:
        print("***************************")
        print("Not a valid amount")
        print("***************************")
        return 0
    else:
        return amount


def withdraw(balance):
    print("***************************")
    amount: float = float(input("Enter Amount to be withdrawn: "))
    print("***************************")
    if amount > balance:
        print("***************************")
        print("Insufficient Funds")
        print("***************************")
        return 0
    elif amount < 0:
        print("***************************")
        print("Amount must be greater than Zero")
        print("***************************")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("**********WELCOME**********")
        print("***************************")
        print("        Banking App        ")
        print("***************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("***************************")
        choice: str = str(input("Enter your choice: "))

        if choice == "1":
            show_bal(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("***************************")
            print("That is not a valid choice")
            print("***************************")
    print("***************************")
    print("Thank You, Have a nice Day")
    print("***************************")


if __name__ == "__main__":
    main()
