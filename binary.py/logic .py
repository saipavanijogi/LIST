n=int(input("enter the number"))
i=1
a=[]
while i<=n:
    j=1
    b=[]
    a.append(n)
    while j<=n:
        b=i*j
        a.append(b)
        j=j+1
    i=i+1
print(a)


