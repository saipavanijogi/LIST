list=[1,2,3,4,5,6]
i=0
c=[]
while i<len(list)-1:
    b=list[i]-list[i+1]
    c.append(b)
    i=i+2
print(c)
        