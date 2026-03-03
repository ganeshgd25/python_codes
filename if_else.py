
num = int(input("Enter a number : "))

if num > 0 :
    print("Given no is positive ")
elif num < 0:
    print("given no is negative ")
else:
    print("number is zero")
    
    
if num % 2 == 0:
    print("number  is even  ")
else:
    print("number is odd  ")

num = int(input("Enter a number : "))

if num % 2 == 0 and num > 0:
    print("Even and positive")
elif  num % 2 == 0 and num < 0:
    print("Even but negative")
elif num % 2 != 0 and num > 0:
    print("odd and positive")
elif num % 2 != 0 and num < 0:
    print("odd but negative")
else :
    print("number is zero")

'''Check if number is:
Even and Positive
Even and Negative
Odd and Positive
Odd and Negative
Or Zero'''

num = int(input("Enter a number : "))

if num == 0:
    print("Number is zero")

elif num % 2 == 0:
    if num > 0:
        print("Even and positive")
    else:
        print("Even and negative")

else:
    if num > 0:
        print("Odd and positive")
    else:
        print("Odd and negative")

#tried
num = int(input("Enter a number : "))

if num % 3 == 0 :
    print("divisible by 3")
elif num % 5 == 0:
    print("divisible by 5 ")
elif num % 3 == 0 and num % 5 == 0: 
    print("Divisible by both")
else:
    print("Not divisible by either")

'''correct way 
 If number is:
 Divisible by 3
 Divisible by 5
 Divisible by both
 Not divisible by either '''

# num = int(input("Enter a number : "))

# if num % 3 == 0 and num % 5 == 0:
#     print("Divisible by both 3 and 5")

# elif num % 3 == 0:
#     print("Divisible by 3")

# elif num % 5 == 0:
#     print("Divisible by 5")

# else:
#     print("Not divisible by either")


# num = int(input("Enter a number : "))

# if num % 3 ==0 or num % 5 ==0 :
#     print("divible by both")
# else:
#     print("not divisible by both ")


num = 0

if num:
    print("True block")
else:
    print("False block")