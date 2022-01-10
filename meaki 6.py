dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
dic1={}
for i in dic:
    if i not in dic1:
        dic1[i]=dic[i]
print(dic) 