numbers=[50,40,23,70,56,12,5,10,7,24,30 ]
list_length=len(numbers)
index=0
count=0
while index<list_length:
    if numbers[index]>20 and numbers[index]<40:
        count=count+1
    index=index+1
print(count)

    