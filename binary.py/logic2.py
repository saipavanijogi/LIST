list=["7",4,9,2.5,True]
i=0
a=[]
b=[]
c=[]
d=[]
while i<len(list):
    if type(list[i])==str:
        a.append(list[i])
    elif type(list[i])==int:
        b.append(list[i])
    elif type(list[i])==float:
        c.append(list[i])
    elif type(list[i])==bool:
        d.append(list[i])
    i=i+1
print("string=",a)
print("string=",b)
print("string=",c)
print("string=",d)

    
    