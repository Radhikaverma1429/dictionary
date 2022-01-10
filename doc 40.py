# Q41.Write a Python program to filter the height and width of students, which are stored in a dictionary. 
# Original Dictionary:
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}Q41.Write a Python program to filter the height and width of students, which are stored in a dictionary. 
# Original Dictionary:
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)


d={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
a={}
for i in d:
    k=d[i]
    j=0
    while j<len(k):
        if k[0]>6 and k[1]<=70:
            key=i
            a[key]=(k[0],k[1])
        j+=1
print(a) 