
# class -A class is a blueprint of an object 
# syntax
# class ClassNAme:
#   pass

# what is object?
# An object is a instance of class.

#ex 
class Student:
    pass

s1 = Student()
s2 = Student()
print(type(s2))


# in python varaible is declared inside class is known as class varaible.
# variable created inside an object is known as instance varaible 
# python first check instance varaibles its excuated and then print class varaible.
# if we change class varaibble with new value so it will changes for all objects also if objects dont has its own variables. 


#__init__() Constructor
class Student:
    def __init__(self):
        print("Object created")

s1 = Student()
s2 = Student()

# class Car:
#     def __init__(self, brand):
#         brand = brand

# c1 = Car("BMW")
# print(c1.brand)


# Inside class methods:
# self.variable → instance variable
# variable → local variable

class Car:
    def __init__(self, brand):
        self.brand = brand

c1 = Car("BMW")
c2 = c1

c2.brand = "Audi"

print(c1.brand)

#Variables store references, not objects

class Car:
    def __init__(self, brand):
        self.brand = brand

c1 = Car("BMW")
c2 = Car("BMW")

print(c1 == c2)
print(c1 is c2)

#For custom classes, Python by default compares object identity, not the attributes.

# == compare the values 
# is - compare with the refrence of an object.

#.copy() creates a new list object.

# =        → reference assignment
# .copy()  → new object copy
# ==       → value comparison
# is       → memory comparison

# Runtime created objects → usually new memory
# Literal constants → may be reused

a = "python"
b = "python"

print(a is b)

# True  In Python, small string literals that contain only certain characters (like letters, digits, and a few common symbols) are automatically interned — meaning Python reuses the same object in memory for identical string literals.
# Longer strings, strings with spaces + punctuation, or strings created at runtime (e.g. from input, concatenation, etc.) are usually not interned.


# What self Really Represents

# self represents the current object (instance) of the class.

# Why self Is Needed

# It allows the method to access object variables.

# What is constrctor---?

# A constructor is a special method that is automatically called when an object of a class is created to initialize the object's data.

# What is __init__?

#__init__ is a #special constructor method in Python that automatically runs when an object is created and is used to initialize the object's attributes.

# In Python, writing __init__() is not mandatory.

# If you don’t define it, Python automatically provides a default constructor.

# Constructor in Python = __init__()
# Not mandatory
# Python provides default constructor automatically
# pass = empty block (do nothing)

# Constructor runs once per object creation
# 3 object created it will run 3 times 

class A:
    def __init__(self):
        print("A")

a = A
a()