
h=[4,2,7,10,5,9,7,20,6]
i=0
a=[]
while i<len(h):
    j=0
    c=0
    while j<len(h):
        if h[i]>h[j]:
            c+=1
        j=j+1
    a.append(c)
i=i+1
print(a)