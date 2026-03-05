
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

# else runs ONLY if no exception happened in try.
# It does NOT check errors separately.
# It simply runs because no error was triggered.

# 1️ Python runs code inside try
# 2️ If an error occurs → it immediately jumps to matching except
# 3️ If NO error occurs → it skips all except blocks
# 4️ Then else runs
# 5️ finally always runs