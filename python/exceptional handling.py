#Exceptional Handling

#eception handling- errors that occurs while program is running
#a=10, b=0 print(a/b) it gives zero division error


#types of erro
#exceptions                      #example
#value error                     int("abc")
#type error                      "10"+5
#zero division error             10/0
#index error                     nums[10] when list has only 3 elements
#key error                       student["age"] where "age" doesn't exist
#indentation error               giving spaces
#file not found error            opening a file that doesn't exist

#1)example program
# try:
#     num=int(input("enter number:"))
#     print("you entered:",num)
# except ValueError:
#     print("please enter valid number")

#try - code that may cause an error 
# except - code to handle the error

#2)example program
# try:
#     a=int(input())
#     b=int(input())
#     result=a/b
#     print("result:",result)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("please enter number only")

#3)example program
# try:
#     a=int(input())
#     b=int(input())
#     result=a/b
#     print("result:",result)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("please enter number only")
# finally:
#     print("done")

#finally - it will execute even if error ocuurs

#4)example program
# try:
#     a=int(input())
#     b=int(input())
#     result=a/b
#     print("result:",result)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("please enter number only")
# else:
#     print("done with caluculation")    
# finally:
#     print("done")


try:
    age=int(input("enter age:"))
    if age<0:
        raise ValueError("age can't be negative")
    print("age",age)
except ValueError as e:
    print("error",e)    

                     