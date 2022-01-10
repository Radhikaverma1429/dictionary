l="MISSISSIPPI"
j=list(l)
dic={}
for i in j:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
# {'M':1,'I':4,'S':4,'P':2} 