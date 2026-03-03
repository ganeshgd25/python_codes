from datetime import datetime 

# Get current date and time 
now = datetime.now()
print(now)

# Get only date
print(now.date())

# get only time
print(now.time())

#Access Individual Parts
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# formatted date and time 
formatted = now.strftime("%d-%m-%Y %H-%M-%S")
print(formatted)

# %Y → Full year (2026)
# %m → Month (03)
# %d → Day (03)
# %H → Hour (24-hour)
# %M → Minute
# %S → Second

# Convert String → Datetime
date_string = "03-03-2026 15:45:10"

dt = datetime.strptime(date_string , "%d-%m-%Y %H:%M:%S")
print(dt)


# Write a program that:

# Prints current date-time

# Prints only year

# Prints formatted like:
# 03 March 2026, 03:45 PM

now = datetime.now()
print(now)
formatted = now.strftime("%d %b %Y , %I:%M %p")
print(formatted)
print("year",now.year)
change = now.strftime("Today is %A , %d %B %Y ")
print(change)
