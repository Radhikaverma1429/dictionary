# my_dict = {'data1':100,'data2':-54,'data3':247}
# sum=0
# for i in my_dict:
#     sum=sum+my_dict[i]
# print(sum) 
def table(num):
    i=1
    sum=1
    while i<=num:
        j=1
        while j<=10:
                print(i,"*",j,"=",i*j)
                j+=1
        i+=1
    print("🌼🌸🌺🌺🌼🌸")
table(num=int(input("enter a name"))) 