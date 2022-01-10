key1 = ['red', 'green', 'blue']
value1 = ['#FF0000','#008000', '#0000FF']
d={}
for i in key1:
    for j in value1:
        d[i]=j
        value1.remove(j)
        break
print(d) 