#set
#set is an unordered data structure. it is mutable and collection of objects. it stores unique elements. it does not allow duplicate values.
my_set = {1, 2, 3, 4, 5, 2, 3}
print(my_set)

nums ={}
print(type(nums))

nums=set()
print(type(nums))

#append
nums={10,20,30}
nums.add(40)
print(nums)

#set operations
#union, intesection, difference, symmetric difference 
#union(|)- combine all the elements from both sets, without allowing duplicates

#union
a={10,20,30}
b={30,40,50}
print(a|b)
#union using method()
print(a.union(b))

#intersection
a={10,20,30}
b={30,40,50}
print(a&b)
#intersection using method()
print(a.intersection(b))

#difference
#difference - elements that exists in the first set but not in the second 
#A-B
a={10,20,30}
b={30,40,50}
print(a-b)
#difference using method()
print(a.difference(b))

#B-A
a={10,20,30}
b={30,40,50}
print(b-a)
#differnce using method()
print(b.difference(a))

#symmetric differnce - elements that are in either set but not in both
a={10,20,30}
b={30,40,50}
print(a^b)

#set main methods(BUILD IN FUNCTIONS)
#len
nums={10,20,30,40}
print(len(nums))
#max
nums={10,20,30,40}
print(max(nums))
#min
nums={10,20,30,40}
print(min(nums))
#sum
nums={10,20,30,40}
print(sum(nums))
#add
nums={10,20,30,40}
nums.add(50)
print(nums)
#update
nums={10,20,30,40,50}
nums.update([60,70,80])
print(nums)
#remove
nums={10,20,30,40,50,60,70,80}
nums.remove(80)
print(nums)
#pop
nums={10,20,30,40,50,60,70}
nums.pop()
print(nums)
#clear
nums={10,20,30,40,50,60}
nums.clear()
print(nums)

