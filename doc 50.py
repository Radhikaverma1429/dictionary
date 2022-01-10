# Q50.Write a Python program to convert a given dictionary into a list of lists. 
# Original Dictionary:
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Convert the said dictionary into a list of lists:
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]


dic={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'} 
d=dic.items()
l=[]
for i in d:
    l.append(list(i))
print(l)


dict={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
l1=[]
for i in dict.items():
    l1.append(list(i))
print(l1)
