#list comphersion

# numbers=[]
# for i in range(1,6):
#     numbers.append(i)
# print(numbers)

# numbers= [i for i in range(1,6)]
# print(numbers)

#one line representation of loop
#syntax: [expression for variable in iterable]
#[x for x in range(1,5)]

# squares=[i*i for i in range(1,6)]
# print(squares)

# names=["sam", "ram","jim"]
# result=[name.upper() for name in names]
# print(result)

#list comprehension with if

# numbers =[]
# for i in range(1,11):
#     if i%2==0:
#         numbers.append(i)
# print(numbers) 

# numbers = [i for i in range(1,11) if i%2==0]
# print(numbers)

#filtering values
# nums=[10,15,20,25,30,35,40]
# result = [i for i in nums if i>20]
# print(result)

#nested list comprehension
#it means having more than one for loop inside list comprehension

# result=[]
# for i in range(1,4):
#     for j in range(1,4):
#         result.append((i,j))
# print(result) 

# result=[(i,j) for i in range(1,4) for j in range(1,4)]
# print(result) 

# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# result=[x for row in matrix for x in row]
# print(result)