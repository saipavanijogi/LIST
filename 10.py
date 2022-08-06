names=["n","i","t","i","s"]
i=1
a=[]
while i<=len(names):
    b=names[-i]
    a.append(b)
    i=i+1
print(a)
if names==a:
    print("it is palindrome")
else:
    print("it is not palindrome")

    