question_list = ["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]
options_list =[["1.Four", "2.Nine", "3.Seven", "4.Eight"],["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
solution_list = ["3", "4", "1"]
answer_list1=["1.nine","2.seven"],["1.Delhi","chennai"],["1.software","2.tourism"]
answer_list=["2","1","1"]
i=0
while i<len(question_list):
    print(i+1,question_list[i])
    j=0
    while j<=len(options_list):
        print(j+1,options_list[i][j])
        j=j+1
    user=(input("enter the number"))
    if user==solution_list[i]:
        print("congrates")
    elif user=="50:50":
        print(answer_list1[i])
        user=(input("enter the number"))
        if user==answer_list[i]:
            print("congrates")
        else:
            print("sorry wrong answer")
            break
    else:
        print("sorry wrong answer")
    i=i+1
        
        
        
    
    


     
    
    
    
    
    
    