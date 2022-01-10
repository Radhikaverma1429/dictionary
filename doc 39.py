# Q40. Write a Python program to convert more than one list to nested dictionary. 
# Original strings:
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003':
# {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]


a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
n=zip(a,b,c)
n=set(n) 
print(n)

# def add(x,y):
#     z=x+y
#     return z
# x=int(input("enter a number "))
# y=int(input("enter a number "))
# d=add(x,y)
# def sub(a,b):
#     c=a+b+d
#     return c 
# l=sub(5,6) 
# print(l)