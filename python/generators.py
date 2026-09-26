#generators
#generators produces value one at a time when required

# def numbers2():
#     for i in range(1,6):
#         yield i
# result = numbers2()
# print(next(result)) 
# print(next(result)) 
# print(next(result)) 
# print(next(result)) 
# print(next(result)) 

#yield passes the function and remembers it's current state

# def numbers():
#     yield 1
#     yield 2
#     yield 3
# result2=numbers()
# print(next(result2))
# print(next(result2)) 
# print(next(result2)) 

#yield vs return
# def demo():
#     return 10
#     return 20
# print(demo())
# print(demo())

# def demo():
#     yield 10
#     yield 20
#     yield 30
# result = demo()
# print(next(result))  
# print(next(result))  
# print(next(result))

#understanding generators execution

# def demo():
#     print("start")
#     yield 10
#     print("middle")
#     yield 20
#     print("end")
#     yield 30
# result = demo()
# print(next(result))  
# print(next(result))  
# print(next(result))

#generator using with for loop
# def numbers():
#     for i in range(1,6):
#         yield i
# for x in numbers():
#     print(x)

#generator expression

#list comp=[]
#genetator exp =()

# nums = (x*x for x in range(1,6))
# print(next(nums))    
# print(next(nums))  
# print(next(nums))  
# print(next(nums))  
# print(next(nums))

#we need to use generators when we want to generate values at a time

#medium level problem
# create a generator that produces even no.s from 1 to 20

def even():
    for i in range(1,21):
        if i%2==0:
            yield i
            