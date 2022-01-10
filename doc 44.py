# Q44.Write a Python program to split a given dictionary of lists into list of dictionaries.
# Original dictionary of lists:
# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]


d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]} 
l=[]
d1={}
for i in d:
	r=d[i]
	for j in r:
		if i=="Science":
			d1[i]=d[i]
	print(d1)