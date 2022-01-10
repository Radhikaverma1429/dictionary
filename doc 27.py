student = [{'id': 1, 'success': True, 'name': 'Lary'},
{'id': 2, 'success': False, 'name': 'Rabi'},
{'id': 3, 'success': True, 'name': 'Alex'}]
i=0
sum=0
user=input("enter a anything :")
while i<len(student):
    if user=="id":
        sum=sum+student[i][user]
    else:
        sum=sum+student[i][user]
    i+=1
print(sum)


