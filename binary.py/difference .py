a=[1,2,3,4,5,6,7]
b=[2,3,1,0,6,7]
i=0
c=[]
while i<len(a):
    if a[i] not in b:
        c.append(a[i])
    i=i+1   
print(c)

     
         
         
         