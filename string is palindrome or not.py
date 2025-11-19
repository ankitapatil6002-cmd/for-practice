# string is palindrome or not
str=input("enter the string:")
str[::-1]
if str==str[::-1]:
    print("it is palindrome")
else:
    print("not palindrome")    
 
print("well done")   