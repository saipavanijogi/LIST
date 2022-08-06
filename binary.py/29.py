student_marks=[1,5,7,23,24,26,27,44,54,65,23,34,54,78,67,97,88,]
index=0
less_than=0
more_than=0
while index<len(student_marks):
    if student_marks[index]<50:
        less_than=less_than+1
    elif student_marks[index]>50:
        more_than=more_than+1
    index=index+1
print(more_than)
print(less_than)




