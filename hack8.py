num1=int(input("enter the time started"))
num2=int(input("enter the stop time"))
i=0
time=0
while i<num1:
    if num2>i:
        if (num1-num2)>3:
            print("yes")
            break
        else:
            print("no")
            break
   