a={1:2,2:3,3:4}
b={4:5,5:6,6:7}
c={} 
for i in a:
    for j in b:
        c[i]=j
        c.update(a)
        c.update(b)
print(c)    