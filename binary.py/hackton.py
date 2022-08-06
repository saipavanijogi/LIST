list=[85, 25 ,65 ,21 ,84]
i=0
b=0
while i<len(list):
    if list[i]%10==0:
        print("yes")
    else:
        p=list[i]%10
        b=b*10+p
    i=i+1
print(b)
if b%10==0:
        print("yes")
else:
        print("no")
        
    
        
        
        

