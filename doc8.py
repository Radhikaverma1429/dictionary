# Q8.Write a Python program to check whether a given key already exists in a dictionary.

a={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 
n=int(input("enter a number "))
if n in a:
    print("exists")
else:
    print("not exists") 