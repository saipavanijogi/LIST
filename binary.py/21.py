# Write a function named is_anagram that takes two strings as its parameters.
# Your function should return True if the strings are anagrams, and False otherwise.
# For example, the call is_anagram("typhoon", "opython") 
# should return True while the call is_anagram("Alice", "Bob") should return False
# list=["typhoon","opython"]
# i=0
# while i<len(list):
    
n=input("enter the string ")
n1=input("enter the string ")
i=0
while i<len(n):
    if n[i]  in n1:
        print("true")
    else:
        print("false")
    i=i+1 