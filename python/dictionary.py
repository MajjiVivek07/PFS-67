#dictionary
#dictionary is an unordered data structure. it is mutable and collection of key-value pairs. it stores unique keys. it does not allow duplicate keys.
#dictionary_name = {key1: value1, key2: value2, key3: value3}
student ={
    "name": "Vivek",
    "age": 21,
    "city": "Bangalore"
}
print(student)
#print(dictionary_name[key]) - to access the value of a key
#dictionary_name[key] = new_value - to change the value of a key

print(student["name"])
print(student["age"])
print(student["city"])
print(student.get("course"))
#adding a new key
#dict_name["new_key"]=value
student["number"]="1234567"
print(student["number"])
print(student)
#updating value
student["number"]= "8374718284"
print(student)
#I need to print only keys
print(student.keys())
#items()
for key, value in student.items():
    print(key,value)
print(student.items())    

#update()- updates multiple values
student.update({
    "name" :"akash",
    "number" :"8143326568"
})  
#pop
#student.pop("number")
#print(student)
#clear
#student.clear()
#print(student)

#len
print(len(student))
#sorted
print(sorted(student))

#create the dict on your own data(id, name, email, cgpa, college), print all the key value pairs, modify
#email, cgpa, college name in short form, sorted()

student ={
    "id":88,
    "name":"vivek",
    "email":"vivek@gmail.com",
    "cgpa":8.54,
    "college":"gayatri vidya parishad"
}
print(student)
print(student["id"])
print(student["name"])
print(student["email"])
print(student["cgpa"])
print(student["college"])

student

print(student)
print(sorted(student))



