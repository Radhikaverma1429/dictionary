# Q51.Write a Python program to filter even numbers from a given dictionary values. 
# Original Dictionary:
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}

dict={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
d={}
for i in dict:  
    l=[]
    for j in dict[i]:
        if j%2==0:
            l.append(j)
    d[i]=l
print(d) 

dict={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
d={}
for i in dict:
    l=[]
    for j in dict[i]:
        if j%2==0:
            l.append(j)
    d[i]=l
print(d) 