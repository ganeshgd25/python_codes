
# map -- Transform all data
# filter - filter the data according to condition 
# reduce - reduce whole data and given a single value output 
# lambda - a small anosymas fun which is using for do operation without using def keyword.

# Transform data

a = [1,2,3,4,5]
result =map(lambda x : x *5 , a)
print(list(result))

# filter data

gd = (2,4,5,6,7,8,9,10)

output = filter(lambda a : a%2 == 0 ,gd)
print(tuple(output))

# reduce

from functools import reduce

nums = [2,4,5,6,78,9,12,15,18,21,22]

x =reduce(lambda a,b: a+b ,nums )
print(x)

# developer must be replace map and filter with list comprehension

lst = [1,2,3,4,56,7,8,9,10]

re=[a for a in lst if a>10 ]
print(re)