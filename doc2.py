a='w3resource'
b=list(a)
c={}
for i in b:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)

