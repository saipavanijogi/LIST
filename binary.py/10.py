list=['p','q']
n=5
a=[]
i=1
while i<=n:
    j=0
    while j<len(list):
        c=list[j]+str(i)
        a.append(c)
        j+=1
    i+=1
print(a)

