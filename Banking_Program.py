#Python Banking Program
from random import choice


def show_balance(bal):
    print("******************")
    print(f"Your Current Balance is = ${bal:.2f}")
    print("******************")

def deposit():
    print("******************")
    amount = float(input("Enter the amount to deposit : $"))
    print("******************")

    if amount < 0:
        print("\nThat is not a valid amount")
        return 0
    else:
        return amount

def withdraw(bal):
    print("******************")
    amount = float(input("Enter to amount to be withdrawn : "))
    print("******************")

    if amount > bal:
        print("------------------")
        print("Insufficient Funds")
        print("------------------")
        return 0
    elif amount < 0:
        print("-----------------------------")
        print("Amount must be greater than 0")
        print("-----------------------------")
    else:
        return amount

def tax_calculator():
    pass

def main():
    balance = 0
    is_running = True

    while is_running:
        print("\n#####################")
        print("   Banking Program")
        print("#####################")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
            print(f"Now your current balance is = ${balance:.2f}")
        elif choice == "3":
            balance -= withdraw(balance)
            print(f"Now your current balance is = ${balance:.2f}")
        elif choice == "4":
            is_running = False
        else:
            print("--------------------------")
            print("That is not a valid choice")
            print("--------------------------")

        import time
        time.sleep(2)
    print("##########################")
    print("Thank you! Have a nice day")
    print("##########################")


if __name__ == "__main__":
    main()