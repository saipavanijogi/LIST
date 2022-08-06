
list=[-3,-2,-4,-7,1,2,3]
i=0
sum=0
count=0
while i<len(list):
    if list[i]>0:
        count=count+1
    else:
        list[i]<0
        sum=sum+list[i]
    i=i+1
print(count,sum)



        
        
    
    