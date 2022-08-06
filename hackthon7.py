# 13th one....   
a=[0,1,0,3,12]
i=0
c=[]
b=[]
while i<len(a):
    if a[i]>0:
        c.append(a[i])
    else:
        b.append(a[i])
    i=i+1
print(c+b)