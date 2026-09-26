#nested loops
# for i in range(0,2): #1-0
#     for j in range(0,10): #j=0, j=1
#         print(i,j)

#star patterns
# 1) increasing triangle
# *
# **
# ***
# ****
# *****    

# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ") 
#     print() 

#2) decreasing triangle
# *****
# ****
# ***
# **
# *

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print() 

#square pattern
# *****
# *****
# *****
# *****
# *****

# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()  

#rectangle pattern
# ********
# ********
# ********
# ********
# rows=4
# cols=8 
# for i in range(rows):
#     for j in range(cols):
#         print("*",end=" ")
#     print() 

#space pattern
#      *
#     **
#    ***
#   ****
#  *****      

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     print()

#pyramid pattern
#        *
#       ***
#      *****
#     *******
#    *********
# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2 * i-1):
#         print("*",end="")    
#     print() 

#number pattern
# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print() 

#5
# 54
# 543
# 5432
# 54321

# for i in range(1,6):
#     num=5
#     for j in range(i):
#         print(num,end="")
#         num-=1
#     print()

#1
#2 3
#4 5 6
#7 8 9 10

# num=1
# for i in range(1,5):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()

#54321
#54321
#54321
#54321
#54321

# for i in range(5):
#     num=5
#     for j in range(5,0,-1):
#          print(j,end="")
#          num-=1
#     print()

#54321
#5432
#543
#54
#5

# for i in range(5,0,-1):
#     num=5
#     for j in range(i):
#         print(num,end=" ")
#         num-=1
#     print()

#1
#21
#321
#4321
#54321

# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

#         1
#        123
#       12345
#      1234567
#     123456789

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1, 2*i):
#         print(j,end="")
#     print()

#name pattern
# C
# CO
# COD
# CODE

# name="CODE"
# for i in range(1,len(name)+1):
#     for j in range(i):
#         print(name[j],end="")
#     print() 


#          *
#         * *
#        *   *
#       *     *
#      *********

n=5
for i in range(1,n+1):
    #spaces before the pyramid
    for j in range(n-i):
        print(" ",end="")
    #spaces between the stars
    for j in range(1,2*i):
        if i==n:
            print("*",end="")
        elif j==1 or j==2*i-1:
            print("*",end="")
        else:
            print(" ",end="")  
    print()             