
list=[12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
i=0
o=[]
while i<len(list):
    a=[list[i],list[i+1],list[i+2]]
    o.append(a)
    i=i+3
print(o)

 