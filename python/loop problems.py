
#palindrome numbers
#eg: 121, 12321, 1234321
# num = int(input("enter a number:"))
# original = num
# reverse = 0
# while num>0:
#     digit = num%10
#     reverse = reverse * 10 + digit
#     num = num // 10

# if original == reverse:
#     print("the number is a palindrome")
# else:
#     print("the number is not a palindrome")        

#factorial
#5! = 5*4*3*2*1=120
# num= int(input("enter a number:"))
# factorial =1 
# while num>0:
#     factorial*=num
#     num-=1
# print(factorial)

#fibonaci series
#0,1,1,2,3,5,8,13,21,34...
n = 10
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

