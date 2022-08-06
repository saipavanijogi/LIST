names=["n,t,i,t,n"]
i=1
a=[]
while i<=len(names):
    b=names[-i]
    a.append(b)
    i=i+1
print(a)
if names==a:
    print("it is a palindroma")
else:
    print("not")

    