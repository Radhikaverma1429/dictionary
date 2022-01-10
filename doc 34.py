# QQ35. Write a Python program to count the number of items in a dictionary value that 
# is a list
# Sample output: 5


dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
a=list(dict.values())
c=0
for i in a:
    for j in i:
        c+=1
print(c) 