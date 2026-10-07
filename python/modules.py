#module
# A module is a python file containing python code such as variables, functions, classes and statements and can be used in another python program
#python file ending with "".py"
#why do we need modules:
#code organization
#avoid rewriting
#reducing error
#code reusability
#team development

#types of modules
#1) built in/standard library modules
#these comes with python
#eg: math, random, sys, os, datetime, statistics
# import math
# print(math.sqrt(25))

# import calculator 
# print(calculator.add(10,20))
#if we want specific function we use
# from calculator import add,sub
#if we want every function we use
# from calculator import *

#user defined- modules created bt yourself

#third party modules:
#requests, django, flask, pandas, numpy
#these are developed outside python's standard library and are normally installed seperately

#Sys module:
#import sys
#print(sys.version)

#sys.argv - contain command line arguments
# import sys
# name= sys.argv[1]
# print("Hello",name)
# age =15
# if age<18:
#     print("not eligible")
#     sys.exit()
# print("eligible")  


#platform module:
#it is used to get info about computer operating system release, version, machine, processor, python version, architecture
# import platform
#platform.system() - return os Name
# print(platform.system())
# #platform.release() - os release
# # print(platform.release())
# # print(platform.version())
# # print(platform.machine()) #return machine architecture
# # print(platform.processor())
# # print(platform.python_version())
# # print(platform.python_implementation())

# import platform
# if platform.system()=="windows":
#     print("running on windows")
# elif platform.system()=="linux":
#     print("running on linux")
# else:
#     print("nothing")  


#collection module:
# specialized data structures
#eg: list, tuple, set, dictionary
#import of collections
#default dict
#counter
#deque
#namedtuple

#counter: counter is used to count how many times item occurs
#from collections impoet counter{}

# from collections import Counter
# nums=[1,1,2,2,2,3,3,3,3,4,4]
# count=Counter(nums)
# print(count)

# text="banana"
# count=Counter(text)
# print(count)

#default dictionary
#it allows us to provide dafault value

# from collections import defaultdict
# students = defaultdict(int)
# print(students["python"])

#grouping students based on their batch
# from collections import defaultdict
# students=defaultdict(list)
# students["CSE"].append("vivek")
# students["CSE"].append("sky")
# students["ECE"].append("yatish")
# print(students)

#deque: double ended queue
# from collections import deque
# nums= deque([10,20,30])
# nums.append(40)
# print(nums)
#add at beginning
# nums.appendleft(5)
# print(nums)
#delete from last
# nums.pop()
# print(nums)
#deleting from beginning
# nums.popleft()
# print(nums)

#namedtuple: A namedtuple is like a tuple whose values can also be accessed by usinh names
# from collections import namedtuple
# student=namedtuple("students", ["name","age","branch"])
# student = student("rahul",20,"CSE")
# print(student.name)
# print(student.age)
# print(student.branch)

#itertools: it provides tools to work with itertors
#import itertools
#used for combinations, permutations. cartesian products, grouping

# import itertools
# numbers = itertools.count(1)
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

#cycle() : repeats elements again and again
# colors = itertools.cycle(["red","green","blue"])
# print(next(colors))
# print(next(colors))
# print(next(colors))
# print(next(colors))
# print(next(colors))

#permutations() : it represents different arrangements/orders
# from itertools import permutations
# nums=[1,2,3]
# result=permutations(nums)
# for item in result:
#     print(item)

#combinations() : it select items where order doesn't matter    

# from itertools import combinations
# nums=[1,2,3,4,5,6,7,8]
# result=combinations(nums,2)
# for item in result:
#     print(item)

#chain(): combines multiple iterables into one sequence

# from itertools import chain
# a=[1,2,3]
# b=[4,5,6]
# result=chain(a,b)
# for x in result:
#     print(x)   

#datetime module: date,time, date+time, time difference, formatting
# from datetime import date
# today = date.today()
# print(today)
# print(today.year)
# print(today.month)

# from datetime import datetime
# now=datetime.now()
# print(now)

#creating specific date
# from datetime import date
# birthday=date(2004,8,11)
# print(birthday)

#creating specific date and time
# from datetime import datetime
# dt=datetime(2026,9,24,15,30)
# print(dt)

#timedelta : represents difference between dates/times
# from datetime import date, timedelta
# today=date.today()
# future=today+timedelta(days=10)
# print(today)
# print(future)

#date difference 
# from datetime import date
# date1=date(2002,5,9)
# date2=date(2026,9,26)
# diff=date2-date1
# print(diff)
# print(diff.days)

#formatting date - strftime()
# from datetime import datetime
# now = datetime.now()
# formatted=now.strftime("%d-%m-%y")
# print(formatted)

# date_string="26-09-2026"
# date_object=datetime.strptime(date_string,"%d-%m-%Y")
# print(date_object)


#random password generator:

# import random
# characters="@$#!%&*()-+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# password=""
# for i in range(10):
#     password+=random.choice(characters)
# print("password:",password) 


#password generator using string

# import random
# import string
# characters="@$#!%&*()-+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# characters=string.ascii_letters+string.digits+string.punctuation
# password=""
# for i in range(8):
#     password+=random.choice(characters)
# print("password:",password) 

#ATM example:
#if,elif,else,variables,input,arthemetic operations, logical operations

#check pin
# correct_pin=1234
# pin =int(input("enter pin:"))
# if pin==correct_pin:
#     print("access granted")
# else:
#     print("invalid pin")  
# #add balance
# balance=10000
# deposit=5000
# pin=int(input("enter pin:"))
# if pin==1234:
#     print("access granted")
#     balance+=deposit
#     print(balance)
# else:
#     print("invalid pin") 
# #withdraw money
# balance=10000
# pin=int(input("enter pin:"))
# if pin==1234:
#     amount=int(input("enter withdraw amount:"))
#     if amount<=balance:
#         balance-=amount
#         print("withdraw successful")
#         print("remaining balance",balance)
#     else:
#         print("insufficient balance") 
# else:
#     print("invalid pin") 

#complete ATM example
balance=10000
pin=int(input("enter pin:"))
if pin==1234:
    print("\n1. check balance")
    print("2. withdraw")
    print("3. deposit")
    choice=int(input("enter your choice:"))
    if choice==1:
        print("balance:",balance)
    elif choice==2:
        amount=int(input("enter withdraw amount:")) 
        if amount<=balance:
            balance-=amount
            print("withdraw successful")
            print("remaining balance:",balance)
        else:
            print("insufficient balance")
    elif choice==3:
        amount=int(input("enter amount:"))
        balance+=amount
        print("deposit success")
        print("updated balance:",balance)
    else:
        print("invalid choice")
else:
    print("pin incorrect")                                   

   






