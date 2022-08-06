
list=[10,20,7,18,14,25,30,31]
a=[]
i=0
while i<len(list):
    j=0
    c=0
    while j<len(list):
        if list[i]<list[j]:
           c+=1
        j=j+1
    i=i+1
    a.append(c)
print(a)
    
     
    
