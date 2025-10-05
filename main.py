# Starting balance
balance = 1000
while True:
    print("\nWelcome to the ATM")
    print("Your balance is", balance)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Choose an option (1, 2, 3, or 4): ")

    if choice == '1':
        print("Your current balance is:", balance)

    elif choice == '2':
        amount = input("How much do you want to deposit? ")
        amount = float(amount)  
        if amount > 0:
            balance = balance + amount  
            print("You deposited sucessufuly", amount)
            print("New balance is:", balance)
        else:
            print("Please enter a positive amount!")
    elif choice == '3':
        amount = input("How much do you want to withdraw? ")
        amount = float(amount)  
        if amount <= balance:
            balance = balance - amount  
            print("You withdraw successufly", amount)
            print("New balance is:", balance)
        else:
            print("Insufficient funds!")
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break 
    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")
  
