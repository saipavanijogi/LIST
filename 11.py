# o/p[[2,3],[6,7],[8,9]]
list=[1,2,3,4,6,7,8,9,5,]
i=0
u=[]
while i<len(list):
    list[i]=[list[i+1],list[i+2]]
    u.append(list[i])
    i=i+3
print(u)

 