# Q38.. Write a Python program to drop empty Items from a given Dictionary. 
# Original Dictionary:
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}


a={'c1': 'Red', 'c2': 'Green', 'c3': None}
a.pop("c3")
print(a) 