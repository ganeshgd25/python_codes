
# What is Exception?
# Exception = Error that happens during runtime

# User may enter wrong input
# File may not exist
# API may fail
# Database may disconnect
# If you don’t handle exceptions → your system crashes.

# syntax
# try:
#     # risky code
# except:
#     # error handling code

try:
    num = int(input("Enter a number: "))
    result = 100/num

except ZeroDivisionError:
    print("cannot divided by zero.!")

except ValueError:
    print("Invalid input please Enter integer value")

else:
    print("Result:", result)

finally:
    print("Execution completed.")