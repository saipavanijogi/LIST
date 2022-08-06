l=[10,17,15,22,25,12]
i=0
s=0
while i<len(l):
    if l[i]%5!=0:
        s=s+l[i]
        i=i+1
    i=i+1
print(s)
        
