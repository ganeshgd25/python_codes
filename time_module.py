
import time

print(time.time())
#✔ Returns seconds since 1 Jan 1970 (Unix epoch)
# ✔ Float value deta hai
# ✔ Mostly performance measure ke liye use hota hai


print("start")
time.sleep(2)
print("End")
# Program 2 seconds rukega
# ✔ Use for delay / retry simulation

print(time.ctime())
# Readable date-time format deta hai.

lt = time.localtime()
print(lt)
# seprate year ,month,day,hour

formatted = time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)
# give formatted time 

start = time.time()
for i in range(1000000):
    pass
end = time.time()
print("Time taken : " , end-start)

# Concept:
# ✔ Start time lo
# ✔ End time lo
# ✔ Difference nikalo



print(time.ctime())
start = time.time()
time.sleep(3)
print(time.ctime())
end= time.time()
print("Time taken :", end-start)

# If you want milliseconds precision, what should you use instead of time.time()?
time.perf_counter()
# More accurate for performance measurement.
