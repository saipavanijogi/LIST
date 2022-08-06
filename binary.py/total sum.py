number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
c=[]
while i<len(n)-3:
    j=1
    while j<len(n):
        if n[i]+n[-j]==number:
            c.append([n[i],n[-j]])
        j=j+1
    i=i+1
print(c)
      
    
    