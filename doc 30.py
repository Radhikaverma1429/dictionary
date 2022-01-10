# Q30.Write a Python program to remove spaces from dictionary keys.

# New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} Original dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'EnglOriginal dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'EngOriginal dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}Original dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}lish']}ish']}
dictionary={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
str1=" "
d={}
for i in dictionary:
    s=" "
    for j in i:
        if j!=str1:
            s+=j
    d[s]=dictionary[i]
print(d)
    

