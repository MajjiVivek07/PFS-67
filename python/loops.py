
#loops- Doing the same task for the repetition of times
#1)for loop
#2)while loop

#for loop- when we know the number of iterations needs to perform
#eg: cooking food for family
#while loop- when we dont know the number of iterations needs to perform
#eg: cooking food in restaurant

#for loop 
#1)by using index 
# for i in range(1,11): #(only 1 to 10 prints)
#     print(i)

#iteration 1
# i=1, i=2 

# nums=[10,20,30,40,50]
# for i in range(0,5):
#     print(nums[i])

#2) by using value
# nums=[10,20,30,40,50]
# for num in nums:
    # print(num)  

#while loop
#while loop syntax
# i=1
# while i<=5:
#     print(i)
#     i+=1

#1st iter =1 <=5
# 2nd => i=2 => 2<=5
# 3rd => i=3 => 3<=5
# 4th => i=4 => 4<=5
# 5th => i=5 => 5<=5

#print even numbers from 1 to 10
#using while loop
# i=1
# while i<=10:
#     if(i%2==0):
#         print(i)
#     i+=1
# #using for loop
# for i in range(2,11):
#     if i%2==0:
#         print(i)

#in reverse
#for loop
# for i in range(10,0,-1):
#     print(i)

#while loop
# i=10
# while i>=1:
#     print(i)
#     i-=1

#sum of numbers from 1 to n
# total=0
# for i in range(1,11):
#     total+=i
# print(total)

#multiplication table

# num=int(input("enter number:"))
# for i in range(1,11):
#     print(num*i)

#finding largest number in array without max()

nums = [10,20,30,40,50]
largest=nums[0]
for num in nums:
    if num > largest:
        largest=num
print(largest)          

        

           