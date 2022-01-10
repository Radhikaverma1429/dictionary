# .Write a Python program to match key values in two dictionaries. 
# Expected output: key1: 1 is present in both x and y

dic=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
l=[]
i=0
while i<len(dic):
    for key in dic[i]:
        if dic[i][key] not in l:
            l.append(dic[i][key])
        i+=1
print(l) 


# d={'key1': 1, 'key2': 3, 'key3': 2} 
# d1={'key1': 1, 'key2': 2}
# for i in d:
#     for j in d1:
        


# for i,j in d.items():
#     for k,r in d1.items(): 
#         if d1[j] in d1[r] :
#             print("present to boyh dictionaries") 
#         elif d[j] in d1[k]:
#             print("present to boyh dictionaries") 
#         else:
#             print("not present") 