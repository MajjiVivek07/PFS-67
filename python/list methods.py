#list methods

#append() - adds an element to the end of the list
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

#insert() - (index, value)
#insert() - adds an element at a specific index in the list
numbers.insert(4, 5)
print(numbers)

#extend() - adds multiple elements to the end of the list
numbers.extend([6, 7, 8])
print(numbers)

#remove() - removes the first occurrence of a value from the list
numbers.remove(8)
print(numbers)

#pop() - removes and returns the last element of the list
numbers.pop()
print(numbers)

#clear() - removes all elements from the list
numbers.clear()
print(numbers)

#index() - returns the index of the first occurrence of a value in the list
numbers = [1, 2, 3, 4, 5, 6]
index= numbers.index(3)
print(index)

#count() - returns the number of occurrences of a value in the list
numbers = [1, 2, 3, 4, 5, 6, 3]
count = numbers.count(3)
print(count)

#sort() - sorts the elements of the list in ascending order
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)

#sorted() - returns a new sorted list from the elements of the given list
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

#reverse() - reverses the order of the elements in the list
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)