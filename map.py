#<===============map===============>
'''list1=[5,10,15,20,25]
def add(x):
    if x%2==0:
        return  "even"
    #else:
        #return "odd"
x=list(map(add,list1))
print(x)'''
#<================filter=============>
'''list1=[5,10,15,20,25]
def add(x):
    if x%2==0:
        return True
    #else:
        #return "odd"
x=list(filter(add,list1))
print(x)'''  
'''list1=[5,10,15,20,25]
def add(x):
    if x%2!=0:
        return  "even"
    #else
        #return "odd"
x=list(filter(add,list1))
print(x)'''
#==================prime no==============>
'''list1=[5,10,15,20,25]
def add(x):
    if x<=1:
       return True
    for i in range(2,int(x**0.5)+1):
        if num%i==0
    #else:
        #return "odd"
x=list(map(add,list1))
print(x)'''
#==================lambda==================>
'''x=lambda name:print("hello",name)
x("sanchita")
x=lambda x,y:x+y
print(x(10,20))
y=input("enter your name")
x(y)
x=lambda x,y:x+y
p=input("enter your name")
q=input("enter your name")
print(x(p,q))'''
'''my_list=[2,4,6,8,10]
x=list(map(lambda x:x**2,my_list))
print(x)'''
'''my_list=[2,1,3,6,7,4,6,8,10]
x=list(filter(lambda x:x%2==0,my_list))
print(x)'''
#=============reduce function=======>
# in a single output any collection then use reduce
'''from functools import reduce
my_list=[1,3,6,9,88,99]
def max(x,y):
    #if x>y:
    #if y>x:
    if x+y:
        return x+y
    else:
        return y
x=reduce(max,my_list)
print(x)'''
#range collection 
#left shift<<2 ka multiply
#right shift>>2 se divide
#range(start,st0p,step)
#note====end-1 for+ve direction
#end+1 for-ve direction

#x=range(0,10)
#x=range(-1,-11,-1)
'''x=range(1,11,-1)
print(list(x))
print(tuple(x))'''
from functools import reduce
#my_list=[2,4,6,8,10,8,7,9,20,35,25]
'''def max(x,y):
    if x>y:
      return x
    else:
       return y
x=reduce(max,my_list)'''
x=input("enter any no:")
'''n=list(map(lambda x:x**2,x))
print(n,x)'''
n=int(input("enter any no:"))
def fact(n):
   i=1
   while n>=1:
      n=i*n
      n=n-1
print("factorial:",fact(n))
      
      









    