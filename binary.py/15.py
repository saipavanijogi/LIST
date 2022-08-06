a= [1,2,4]
b= [5,6,4]
i=0
x=" "
while i<len(a):
    x=str(x)+str(a[i])
    i+=1
sum=" "
j=0
while j<len(b):
    sum=str(sum)+str(b[j])
    j+=1
value=int(sum)+int(x)
c=str(value)
d=list(c)
e=[]
f=0
while f<len(c):
    e.append(int(c[f]))
    f+=1
print(e)

    
        
        
    