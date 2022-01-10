dic=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
l=[]
i=0
while i<len(dic):
    for key in dic[i]:
        if dic[i][key] not in l:
            l.append(dic[i][key])
        i+=1
print(l) 
