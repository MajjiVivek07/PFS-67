# import calculator
# print(calculator.add(10,20))
# print(calculator.sub(10,20))
# print(calculator.mul(10,20))
# print(calculator.div(10,20))

# import calculator 
# print(calculator.name)
# print(calculator.age)
# print(calculator.company)

# import math
# print(math.sqrt(25))
# print(math.pow(2,3))
# print(math.ceil(4.2)) #rounds upward
# print(math.floor(4.8)) #rounds downward
# print(math.factorial(5))
# print(math.pi)
# radius=5
# area=math.pi*radius*radius
# print(area)

import random
# num = random.randint(1,10)
# print(num)
# names=["s","v","k","a"]
# name=random.choice(names)
# print(name)
# nums=[1,2,3,4,5]
# random.shuffle(nums)
# print(nums)

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
import platform
#platform.system() - return os Name
print(platform.system())
#platform.release() - os release
# print(platform.release())
# print(platform.version())
# print(platform.machine()) #return machine architecture
# print(platform.processor())
# print(platform.python_version())
# print(platform.python_implementation())

import platform
if platform.system()=="windows":
    print("running on windows")
elif platform.system()=="linux":
    print("running on linux")
else:
    print("nothing")    