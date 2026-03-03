account_balance = 50000 
ATM_pin =2525
attempt=0
max_attempt =3
transactions = []
print("Welcome to ATM... ")

while attempt < max_attempt:
    pin = int(input("pleaase Enter your pin : "))

    if pin ==ATM_pin :
        print("Login Sucessfull..!")
        break 
    else:
        print("Incorrect pin..!")
        attempt+=1
else:
    print("card Blocked..!")
    exit()

while True:  
    print("1: check Balance")
    print("2: Deposit")
    print("3: withdraw")
    print("4: History")
    print("5: Exit")

    choice = input("Enter your choice :")

    if choice == "1" :
        print("Your account_balance is : " ,account_balance)

    elif choice == "2" :
        amount = int(input("Enter your Deposit amount: "))
        if amount<= 0:
            print("Invalid deposit amount.")
        else:
            account_balance+= amount 
            print("Deposit Sucessfull..!")
            print("Updated balance : ", account_balance)
            transactions.append(f"Deposited {amount}")

    elif choice == "3" :
        if pin == ATM_pin :
            amount = int(input("Enter withdrawl amount:"))

            if amount <=0:
                print("Invalid amount..!")
            elif amount > account_balance:
                print("insufficient Balance..!")
            else:
                if amount > 5000:
                    print("High amount withdrawal – please confirm")
                account_balance -= amount
                print("Withdrawl sucessfull..!")
                print("Remaining balance:" , account_balance)
                transactions.append(f"withdrawn {amount}")
        else:
            print("Incorrect Pin..!")

    elif choice == "4" :
        if len(transactions) == 0:
            print("No transactions yet..!")
        else:
            print("Trsactions History:")
            for t in transactions:
                print(t)

    elif choice == "5" :
        print(" Thank you for using ATM")
        break
    else:
        print("Invalid choice")
 