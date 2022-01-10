# Write a Python program to print a dictionary in table format.
# Sample Output:
# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11

# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]} 
# for j in my_dict:
#     print(j,end=" ")
# print(" ")
# i=0
# while i<len(my_dict):
#     for k in my_dict:
#         print(my_dict[k][i],end=' ')
#     print(" ")
#     i+=1

# i=0
# while i<len(my_dict):
#     for j in my_dict:
#         print(my_dict[j][i],end=" ")
#     print(" ")
#     i=i+1

# l1=['S001', 'S002', 'S003', 'S004']
# l2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# l3=[85, 98, 89, 92]
# d={}
# dic={}
# l=[]
# for i in l1:
#     for j in l2:
#         for n in l3:
#             d[i]={j:n}
#             l2.remove(j)
#             break
#         l3.remove(n)
#         break
         
# print(d)

# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}