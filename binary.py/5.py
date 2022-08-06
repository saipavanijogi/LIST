list1=["shogun","tapioca","express","buger king","kfc"]  
list2=["pitta","the grill at torrey pines","hunger hunter steakhouse","shogun"]
i=0
a=[]
while i<len(list1):
    if list1[i] in list2:
        a.append(list1[i])
    i=i+1
print(a)