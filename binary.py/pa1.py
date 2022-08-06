list1=[7000,7000,13000,12000,6900]
list2=[6910,7010,7000,12000,18000,15000,10450]
i=0
l=[]
while i<len(list1):
    if list1[i] not in list2:
        l.append(list1[i])
    i=i+1
print(l)
    