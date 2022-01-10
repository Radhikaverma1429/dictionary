# Q48.Write a Python program to find the length of a given dictionary values. 
# Original Dictionary:
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}
# Original Dictionary:

# d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# l={}
# for i in d:
#     l[d[i]]=len(d[i])
# print(l)

d={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
l={}
for j in d:
    l[d[j]]=len(d[j])
print(l)