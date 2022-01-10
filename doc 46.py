# Q46.Write a Python program to convert string values of a given dictionary, into integer/float datatypes. Go to the editor
# Original list:
# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
# Original list:
# [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# String values of a given dictionary, into float types:
# [{'x': 10.12, 'y': 20.23, 'z': 30.40}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]



d=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
d1={} 
d2={}
l=[]
for i in range(len(d)):
    a=d[0]
    b=d[1]
    for j in a:
        d1[j]=float(a[j])
    for k in b:
        d2[k]=float(b[k])
l.append(d1)
l.append(d2)
print(l)