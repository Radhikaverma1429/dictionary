# Q28.Write a Python program to convert a list into a nested dictionary of keys.
# Sample output:
# {1: {2: {3: {4: {}}}}}


num_list = [1, 2, 3, 4]
e={}
dic=e
for i in num_list:
    e[i]={}
    e=e[i]
print(dic)