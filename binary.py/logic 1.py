# list=[-1,8,-9,5,12]
# i=0
# a=[]
# b=[]
# while i<len(list):
#     if list[i]<0:
#         a.append(list[i])
#     else:
#         b.append(list[i])
#     i=i+1
# print(a)
# print(b)

list=[-1,8,-9,5,12,32]
i=0
a=[]
s=0
while i<len(list):
    if list[i]<0:
        a.append(list[i])
    i=i+1
j=0
s1=0
while j<len(a):
    s1=s1+a[j]
    j=j+1
print(-s1)
     
    
        