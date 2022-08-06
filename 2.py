a=[2,3,7,9,16,15,8,]
b=[6,9,8,9,3,7,8]
i=0
c=0
d=0
e=0
f=[]
while i<len(a):
    j=0
    while j<len(b):
        c=a[i]
        d=b[j]
        e=c*d
        f.append(e)
        j=j+1
        i=i+1
print(f)

