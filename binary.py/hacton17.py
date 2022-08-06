# Write a function named capital_indexes.
# The function takes a single parameter, which is a string. 
# Your function should return a list of all the indexes in the string that have capital letters.

string=("HellO")
i=0
a=[]
while i<len("HellO"):
    if string[i]==string[i].upper():
        a.append(i)
    i=i+1
print(a)
    
