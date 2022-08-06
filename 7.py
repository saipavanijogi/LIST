   
a=[[1,2,3,4,5,6],[7],[8,9,10]]
i=0
sum=0
while i<len(a):
    j=0
    while j<len(a[i]):
        b=a[i][j]
        sum=sum+b
        j=j+1
    i=i+1
print(sum)
        
