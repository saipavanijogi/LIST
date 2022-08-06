list=[2,3,4,5,6,7,11,13,17,19,21,23,29,31,37,41,43,51]
i=0
a=[]
while i<len(list):
    j=1
    while j>i:
        b=list[j],list[i]
        a.append(b)
        print(b,end="")
        j=j+1
        i=i+1

