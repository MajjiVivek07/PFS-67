#operators
#arithmetic operators
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)  #3.33
print("Floor Division:", a // b) #3
print("Modulus:", a % b) #1
print("Exponentiation:", a ** b)

#assignment operators
#addition assignment
x = 5
x += 3  # x = x + 3
print("Addition Assignment:", x)

#subtraction assignment
x = 5
x -= 3 # x = x - 3
print("Subtraction Assignment:", x)

#multiplication assignment
x = 5
x *= 3 # x = x * 3
print("Multiplication Assignment:", x)

#division assignment
x = 5
x /= 3 # x = x / 3
print("Division Assignment:", x)

#modulus assignment
x = 5
x %= 3 # x = x % 3  
print("Modulus Assignment:", x)

#exponentiation assignment
x = 5
x **= 3 # x = x ** 3
print("Exponentiation Assignment:", x)

#comparison operators
a = 5
b = 5
print("Equal to:", a == b)
print("Not equal to:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)

#logical operators
age =25
salary = 50000
print(age > 18 and salary > 30000) #True
print("Logical AND:", age > 18 and salary > 30000)
print("Logical OR:", age > 18 or salary > 30000)
print("Logical NOT:", not (age > 18))

#identity operators
a = [10, 20, 30]
b = [10, 20, 30]
print(a==b)  # True
print(a is b)  # False
print(a is not b)  # True
# is refers to check whether two names are belong to the same object.

#membership operators
#in, not in
#it check whther the value exists within a condition or sequence
numbers=[10, 20, 30, 40,]
print(20 in numbers)  # True
print(20 not in numbers)  # False

#bitwise operators
#bitwise operators are used to perform bit-level operations on binary numbers. They operate on the individual bits of the operands.
a = 10 
b = 5
print("Bitwise AND:", a & b)  
print("Bitwise OR:", a | b)   
print("Bitwise XOR:", a ^ b)   
print("Bitwise NOT:", ~a)    
print("Left Shift:", a << 1)  
print("Right Shift:", a >> 1) 

#precedence of operators
#1. Parentheses ()
#2. Exponentiation (**)
#3. Multiplication (*), Division (/), Floor Division (//), Modulus (%)
#4. Addition (+), Subtraction (-)
result = (10 + 5)*2
print( result)  #30

#small example program
#shopping (if we can buy 3000 rupees more than bill we have 10 percent discount if we buy less 3000 rupees bill we do not have 10 percent discount will not be given)
price = 3000
quantity = 3
total_cost = price * quantity
if total_cost > 3000:
    discount = total_cost * 0.10
else:
    discount = 0
final_cost = total_cost - discount
print("final cost:", final_cost)




