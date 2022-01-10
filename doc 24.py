# Write a Python program to combine values in python list of dictionaries. 
# Expected Output: Counter({'item1': 1150, 'item2': 300})

data=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
sum=0
sum1=0
dic={}
for i in data:
    if i["item"]=="item1":
        sum=sum+i["amount"]
        dic["item1"]=sum
    else:
        sum1=sum1+i["amount"]
        dic["iten2"]=sum1 
print(dic) 
