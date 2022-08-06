# second max
number=[50,40,23,70,56,12,5,10,7]  
i=0
max=0
sec_max=number[i]
while i<len(number):
    if number[i]>max:
        max=number[i]
    elif number[i]>sec_max and sec_max<max:
       sec_max=number[i]
    i=i+1
print(sec_max)
    
