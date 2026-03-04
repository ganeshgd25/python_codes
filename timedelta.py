from datetime import datetime , timedelta

# Calculate subscription expiry
# Calculate log retention period
# Find days between login & logout
# Data aging in pipelines
# Spark partition filtering by date

# add days
now = datetime.now()
print("Now:", now)

future = now + timedelta(days=5)
print("After 5 days" , future)

#substract days
past = now-timedelta(days=10)
print("10 days ago :", past)

# add hours
after_hours = now+timedelta(hours=3)
print("After 3 hrs", after_hours)

# add minutes
after_minutes = now+timedelta(minutes=30)
print("After 30 minutes", after_minutes)

# calculate diff between 2 dates 
date1 = datetime(2026,4,10)
date2 = datetime(2026,3,3)

difference = date1 - date2
print("Difference:", difference)
print("Days:" ,difference.days)


# Write code that:
# Takes user input (number of days)
# Adds that many days to today
# Prints future date

d = int(input("Enter no of days: "))

after_day = now+timedelta(days=d)
print("After 40 days :",after_day)