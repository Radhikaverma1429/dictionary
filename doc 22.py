my_dict = {'A': 67, 'B': 23, 'C': 45,'D': 56, 'E': 12, 'F': 69} 
d={}
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