d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
c={}
for i in d1:
    for j in d2:
        if i in d2:
            c[i]=d1[i]+d2[i]
        elif j not in d1:
            c[j]=d2[j]
        elif i not in d2:
            c[i]=d1[i]
print(c) 