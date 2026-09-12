#strings
name="Vivek"
print(name)
print(name[2])
print(name[-2])
print(name[0:4])

# f-strings and .format() method
#f-strings
age = 22
name = "Vivek"
print(f"My name is {name} and my age is {age}")  #f-string
# .format()
print("My name is {} and my age is {}".format(name, age))
# indexing
lang="Python"
print(lang)
print(lang[0])
print(lang[1])
print(lang[2])
print(lang[3])
print(lang[4])
print(lang[5])
#reverse indexing
print(lang[-1])
print(lang[-2]) 
print(lang[-3])
print(lang[-4])
print(lang[-5])
print(lang[-6])

#string slicing
#variable[start:stop]
word="Python"
print(word[0:4])
print(word[:5])
print(word[3:])

#variable[start:stop:step]
word="Python"
print(word[0:6:2]) 
print(word[0:6:3])
print(word[0:6:4])

#reversing
print(word[::-1])

#replacing
word="Python"
reult=word.replace("h","")
print(reult)
print(word)
# second way for replacing
text="python"
for char in text:
    if char=="h":
        continue
    print(char, end="")

#concatenation
#concatenation is the process of joining two or more strings together
first_name="\nVivek"
last_name="Majji"
name=first_name+" "+last_name
print(name)

#repetition
#repetition is the process of repeating a string multiple times
word="Python"
print(word * 3)
#for spacing between the words
print((word + " ") * 3)

#membership - in()
message="Python is a programming language"
print("java" in message)

#methods 
#upper() - converts all characters in a string to uppercase
word="python"
print(word.upper())
#isupper() - checks if all characters in a string are uppercase
word="PYTHON"
print(word.isupper())
#lower() - converts all characters in a string to lowercase
word="PYTHON"
print(word.lower())
#islower() - checks if all characters in a string are lowercase
word="python"
print(word.islower())
#title() - converts the first character of each word in a string to uppercase
word="python programming"
print(word.title())
#capitalize() - converts the first character of a string to uppercase
word="python is a programming language"
print(word.capitalize())
#strip() - removes whitespace from the beginning and end of a string
word="   python is a programming language   "
print(word.strip())
#lstrip() - removes whitespace from the beginning of a string
word="   python   "
print(word.lstrip())
#rstrip() - removes whitespace from the end of a string
word="  python   "
print(word.rstrip())
#replace() - replaces a specified substring with another substring
word="python is a programming language"
print(word.replace("python", "Java"))
#count() - counts the number of occurrences of a specified substring in a string
word="python is a programming language"
print(word.count("a"))
#startswith() - checks if a string starts with a specified substring
word="python is a programming language"
print(word.startswith("is"))
#endswith() - checks if a string ends with a specified substring
word="python is a programming language"
print(word.endswith("language"))
#split() - splits a string into a list of substrings based on a specified delimiter
word="python, java, sql"
print(word.split())
#join() - joins a list of strings into a single string using a specified delimiter
words=["python", "java", "sql"]
print(", ".join(words))

#isalpha() - checks if all characters in a string are alphabetic
word="python"
print(word.isalpha())
#isdigit() - checks if all characters in a string are digits
word="12345"
print(word.isdigit())
#isalnum() - checks if all characters in a string are alphanumeric
word="python123"
print(word.isalnum())





