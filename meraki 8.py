n=int(input("enter the range of loop "))
dic={}
for i in range (n):
    name=input("enter a name ")
    marks=int(input("enter a marks "))
    dic[name]=marks
print(dic)