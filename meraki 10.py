d =  {'Alex': ['subj1', 'subj2', 'subj3','neetu 4'],'David': ['subj1', 'subj2']}
a=list(d.values())
c=0
for i in a:
    for j in i:
        c+=1
print(c) 

