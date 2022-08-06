# students_marks=[23,45,89,90,56,80]
# length=len(students_marks)
# index=0
# total_marks=0
# while index<len(students_marks):
#  total_marks=students_marks[index]+total_marks
#  index=index+1
# print("total_marks:"+str(total_marks))  

list=[[1,2,3,],[4,5,6],[7,8,9]]
# o/p 1,2,3,4,5,6,7,8,9
i=0
while i<len(list):
    j=0
    while j<len(list):
        print(list[i][j],end=",")
        j=j+1
    i=i+1
