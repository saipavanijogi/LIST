list=[1,2,3,4,6,8,9] 
i=1
while i<=len(list):
    j=0
    while j<i:
        if i not in list:
            list.append(i)
            list.sort()
        j=j+1
    i=i+1
print(list)