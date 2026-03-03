# Take:

# Account balance

# Withdrawal amount

# Rules:

# If withdrawal > balance → Insufficient balance

# If withdrawal <= balance → Deduct and print remaining balance

# If withdrawal <= 0 → Invalid amount

Acc_balane = 10000 
correct_pin = 2525
attempt = 0
max_attempt =3 
pin_verified = False

print("Hi welcome to ATM.. ")

while attempt < max_attempt:
    pin =int(input("Please Enter your pin : "))

    if pin==correct_pin:
        print("pin is correct you can withdraw your money..!")
        pin_verified = True
        break
    else:
     print("pin is incorrect plz enter correct pin..")
     attempt+=1
else: 
    print("sorry your card is blocked..!")
    print("you are not able to proceed transaction..")

if pin_verified :

    withdrawL_amt = int(input("Enter your withdrawal amt : "))
    if withdrawL_amt <= 0 :
        print("invalid amount please type valid amount..!")
    elif  withdrawL_amt > Acc_balane :
        print("Insufficient Balance")
    else:
        if withdrawL_amt > 5000:
            print("High amount withdrawal – please confirm")
        Acc_balane-= withdrawL_amt 
        print("withdrawl sucessfull..! ")
        print( "your remaing_balance is : " , Acc_balane )

