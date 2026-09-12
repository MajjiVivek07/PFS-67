#tuple
#tuple is an ordered data structure. it is immutable and collection of objects.
student = ("Vivek", 21, "Bangalore")
print(student)

#1. ordered: proper order is maintained in the tuple.
#2. immutable: we cannot change the values of the tuple. 
#tuples_name[index] = new_value  # This will raise an error

#tuple methods
#count() - returns the number of occurrences of a value in the tuple
my_tuple = (1, 2, 3, 4, 5, 3)
count = my_tuple.count(3)
print(count)

#index() - returns the index of the first occurrence of a value in the tuple
my_tuple = (1, 2, 3, 4, 5)
index = my_tuple.index(3)
print(index)

#concatenation of tuples
tuple1 = (1, 2, 3)
tuple2 = (4,)
result = tuple1 + tuple2
print(result)

#repetition of tuples
tuple1 = (1, 2, 3)
result = tuple1 * 3
print(result)

#built-in functions for tuples
#len() - returns the number of elements in the tuple
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))
#max() - returns the maximum value in the tuple
my_tuple = (1, 2, 3, 4, 5)  
print(max(my_tuple))
#min() - returns the minimum value in the tuple
my_tuple = (1, 2, 3, 4, 5)
print(min(my_tuple))
#sum() - returns the sum of all elements in the tuple
my_tuple = (1, 2, 3, 4, 5)
print(sum(my_tuple))

#methods
#sorted() - returns a new sorted list from the elements of the given tuple
my_tuple = (3, 1, 4, 2, 5)
print(sorted(my_tuple))

#convert tuple to lidt
my_tuple = (10, 20, 30, 40, 50)
my_list = list(my_tuple)
print(my_list)

#now modify it 
my_tuple = (10,60,30,40,50)
my_list=list(my_tuple)
my_list[1]=20
print(my_list)

#append
my_tuple = (10,60,30,40,50)
my_list=list(my_tuple)
my_list.append(60)
print(my_list)

#extend
my_tuple = (10,60,30,40,50)
my_list=list(my_tuple)
my_list.extend([70,80])
print(my_list)
