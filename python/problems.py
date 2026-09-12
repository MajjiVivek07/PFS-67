#1)identify number either positive or negative or zero

# num = int(input("enter number:"))
# if num >0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")  

#2) identify number either even or odd
          
# num = int(input("enter number:"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")   

#3) largest of two numbers

# num1=int(input("enter first number"))
# num2=int(input("enter second number"))  
# if num1> num2:
#     print("first number is larger")   
# elif num2> num1:
#     print("second number is larger")
# else:
#     print("both are equal")

#4) college admission

# marks=int(input("enter marks:"))
# enterance = input("did you pass the enterance exam?(yes,no):")  
# if marks>=60 and enterance=="yes":
#     print("eligible for admission")
# else:
#     print("not eligible") 

#5)login system
# username=input("enter a username:")
# password=input("enter a password")
# if username == "admin" and password == "password123":   
#     print("login succesful")
# else:
#     print("invalid username or password") 

#6)driving licence 
# under 18 - too young to drive
# 18+ but no licence - valid lincence required  
# 18+ with licence - you can drive

# age =int(input())
# licence_valid= input("yes/no:")

# if age>=18:
#     if licence_valid=="yes":
#         print("you can drive")
#     else:
#         print("valid licence required")
# else:
#     print("too young to drive")  

#7)movie ticket pricing
# below 5 - free
# 5-12 - 100
# 13-59-200
# 60 and above-120     

age=int(input("enter your age:"))
if age<5:
    print("ticket is free")
elif 5<=age<=12:
    print("ticket price is 100 ")
elif 13<=age<=59:
    print("ticket price is 200")
else:
    print("ticket price is 120")  

#8) leap year
year=int(input("enter a year:"))
if year%400==0 or (year%4==0 and year%100!=0):
    print("it is a leap year")
else:
    print("it is not a leap year")  

#9)employee management system
# performance>90 and experience >5 =20% hike
# performance>90 and experience >5 =10% hike 
# performance>80 = 10% hike
# performance>70 = 5% hike    


