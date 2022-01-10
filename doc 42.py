# Q43.Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists. 
# Original list:
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}


dict=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)] 
l=[]
l1=[]
l2=[]
d={}
for i,j in dict:
    if i=="yellow":
        l.append(j)
        d[i]=l
    elif i=="blue":
        l1.append(j)
        d[i]=l1
    else:
        l2.append(j) 
        d[i]=l2
print(d) 