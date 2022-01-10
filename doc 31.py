# Q31.. Write a Python program to get the top three items in a shop. Go to the editor
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

my_dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
m1=0
m2=0
m3=0
for i in my_dict:
    if my_dict[i]>m1:
        m1=my_dict[i]
        f_key=i
for j in my_dict:
    if my_dict[j]<m1:
        if my_dict[j]>m2:
            m2=my_dict[j]
            s_key=j
for k in my_dict:
    if my_dict[k]<m1:
        if my_dict[k]<m2:
            if my_dict[k]>m3:
                m3=my_dict[k]
                t_key=k
print(f_key,m1) 
print(s_key,m2)
print(t_key,m3) 