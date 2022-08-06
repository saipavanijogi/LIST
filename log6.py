list=[[19,12],[6,2],[17,11],[8,56]]
i=0
b=[]
while i<len(list):
      j=1
      while j<len(list[i]):
            a=sum(list[i])
            b.append([a])
            j=j+1
      i=i+1
print(b)



      
