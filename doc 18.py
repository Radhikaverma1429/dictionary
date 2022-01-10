# Q18.Write a Python program to get the maximum and minimum value in a dictionary.

dic={'x':500, 'y':5874, 'z': 560}
m=0
m1=0
for i in dic:
    if dic[i]>m:
        m=m1
        m1=dic[i]
print(m)
print(m1) 