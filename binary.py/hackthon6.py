chocolates_have=int(input("enter the how many chocolate he have"))
chocolates_want=int(input("enter the how many chacolate he want"))
chocolates=5
i=0
rs=0
while i<chocolates_have:
    if chocolates_want>i:
        rs=(chocolates_want-chocolates_have)*chocolates
    i=i+1
print(rs)
