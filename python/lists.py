#list
#list is a ordered data structure. it is a mutable and collection of objects.
my_list = [1, 2, 3, 4, 5]
print(my_list)
# 1. ordered: proper order is maintained in the list.
# 2. mutable: we can change the values of the list.
# lists_name[index] = new_value
my_list[0] = 10
print(my_list)
# list can contain different data types
my_list = [1, "hello", 3.14, True]
print(my_list)
#adding elements to the list
# append() - adds an element to the end of the list
my_list.append(6)
print(my_list)
#extend() - adds multiple elements to the end of the list
a=[7, 8, 9]
b=[10, 11, 12]
a.extend(b)
print(a)
#if we delete last element of the list, we can use pop() method
a.pop()
print(a)
#remove() - removes the first occurrence of the specified value
a.remove(8)
print(a)

#concatination of lists
list1 = [1, 2, 3]   
list2 = [4, 5, 6]
result = list1 + list2
print(result)

#repeatition of lists
list1 = [1, 2, 3]
result = list1 * 3
print(result)

#built-in functions for lists
#len() - returns the number of elements in the list
a = [1, 2, 3, 4, 5]
print(len(a))
#max() - returns the maximum value in the list
a = [1, 2, 3, 4, 5]
print(max(a))
#min() - returns the minimum value in the list
a = [1, 2, 3, 4, 5]
print(min(a))
#sum() - returns the sum of all elements in the list
a = [1, 2, 3, 4, 5]
print(sum(a))
#sorted() - returns a new sorted list from the elements of the given list
a = [3, 1, 4, 2, 5]
print(sorted(a))  
#reversed() - returns a new reversed list from the elements of the given list
a = [1, 2, 3, 4, 5] 
print(list(reversed(a)))
