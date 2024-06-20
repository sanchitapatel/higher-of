'''my_list=[10,20,30,40,50]
new_list=[]
for i in my_list:
    x=i+5
new_list.append[x]
print(new_list)'''
my_list=[10,20,30,40,50]
def add(x):
    return x+5
x=map(add,my_list)
print(x)
print(list(x))
