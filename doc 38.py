# Q39.Write a Python program to filter a dictionary based on values. 
# Original Dictionary:
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

a={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
d={}
for i in a:
    if a[i]>170:
        d[i]=a[i]
print(d)