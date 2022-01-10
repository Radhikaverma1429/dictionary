# Q33.Python: Print a dictionary line by line
# Sample Output:
# Aex                                                                                                           
# class : V                                                                                                     
# rolld_id : 2                                                                                                  
# Puja                                                                                                          
# class : V                                                                                                     
# roll_id : 3 

students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}} 
for i in students:
    for j in i:
        print()
    # pprint.pprint(j,k)