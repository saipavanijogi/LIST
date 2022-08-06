list="pavanijogi"
# # [p:1,a:2,v:1,n:1,i:2,j:1,0:1,g:1]
i=0
c=[]
p=[]
while i<len(list):
    a=list.count(list[i])
    b=list[i],a
    c.append(b)  
    if c[i] not in p:
        p.append(c[i])
    i=i+1
print(p)


