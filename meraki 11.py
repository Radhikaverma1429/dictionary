my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
m1=list(my_dict.values())
m2=0
m3=0
m4=0
i=0
a={}
while i<len(m1):
    if m1[i]>m2:
        m2=m3
        m3=m4 
        m4=m1[i]
    i+=1
b=m2,m3,m4
print(set(b))
# /=list(b)
# a={}
# for i in my_dict:
#     for j in e:
#         a[i]=j
#         e.remove(j)
#         break
# print(a)

