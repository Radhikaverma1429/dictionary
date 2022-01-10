# Q21.Write a Python program to print all unique values in a dictionary. 
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}


Sample_Data=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
d=[]
for i in Sample_Data:
    for j,k in i.items():
        if k not in d:
            d.append(k)
print(set(d))             
