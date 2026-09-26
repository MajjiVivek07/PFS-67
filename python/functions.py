#functions introduction

#function - block of code to do particular task

#why do we need fuction- to avoid the repetition 

#function syntax: def function_name(parameters):
                       #function body

#user defined functions
#basic program
#function_creation
def greet():    #greet()-function name
    #function_body
    return "hello students"
#function_calling
print(greet())  

#types of functions
#type 1: no parameters, no return value

def greet():
    print("hello students")
greet()    

#type 2: parameters but no return value
def greet(name):
    print("hello",name)
greet("vivek")

#type 3:no parameters, but return value
def get_number():
    return 100
result=get_number()
print(result)

#type 4: parameters and return value
def add(a,b):    #a,b are parameters
    return a+b
result=add(2,3)  #2,3 are aruguments
print(result)
#result - gives the result back to the program

#returning multiple values
def calc(a,b):
    add = a+b
    sub = a-b
    return add, sub
x, y =calc(20,10)
print(x)
print(y)

#positional aruguments
#arguments are matched based on their position
#order is important

def student(name,age):
    print("name:",name)
    print("age:",age)
#function_calling
student("vivek",22)   

#keyword arguments
def student(name, age):
    print(name)
    print(age)
student(name="vivek",age=22)

#default arguments
def greet(name="student"):
    print("hello",name)
greet("codegnan")

#variable-length arguments(*args)
def add(*numbers):
    total=0
    for number in numbers:
        total+=number
    return total
print(add(10,20))
print(add(1,2,3,4,5,6,7,8,9))
#*args - it collects multiple positional arguments into a tuple

#keyword variable-length arguments(**kwargs)
#accepts multiple keyword arguments
# **kwargs -> dictionary  
def student_details(**details):
    print(details)
student_details(
    name="vivek",
    age=22,
    city="hyd"
)

#both combine
def example(*args,**kwargs):
    print(args)
    print(kwargs)
example(10, 20, 30, name="vivek",age=22)    