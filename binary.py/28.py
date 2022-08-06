students_marks=[23,50,10,16,30]
length=len(students_marks)
index=0
total_marks=0
while index<len(students_marks):
    total_marks=students_marks[index]+total_marks
    index=index+1
print(total_marks)
