# Write a Python program to remove a specified dictionary from a given list. 
# Original list of dictionary:
# Remove id #FF0000 from the said list of dictionary:
# [{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]


a=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
b=input("enter anything ")
for j in range (len(a)):
    if a[j]["id"]==b:
        del a[j]
        break
    elif a[j]["color"]==b:
        del a[j]
        break
print(a)
        