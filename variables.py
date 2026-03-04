
# varaible created outside the functions its a global varaible
# varaible created inside the function its a local varaible 
# reading global inside function allowded 
# if we want to modify gloabl varaible inside function then use global keyword 


a =10   # global 

def greet():
    a =20     # local 
    print(a)   # not modified beacuse we dont use global keyword here so it prints 20 and then 10 

greet()
print(a)


m = 15

def gd():
    global m 
    m = 20
gd()
print(m)


x =5

def md():
#print(x)
    global x
    x=10

md()
print(x)