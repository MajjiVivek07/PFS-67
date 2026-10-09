#regular expession
#regular expression - search looks for a pattern anywhere inside

#string
# import re
# text = "I am learning python"
# result = re.search("python", text)
# print(result)

# #we need to use search when we want to know as "doies this pattern occur somewhere in text"
# #re.match() - it checks the pattern only at the beginning.
# import re
# text = "From Python the day one, I'm focusing on and it is esay"
# result = re.match("Python", text)
# print(result)

# #re.fullmatch() - it requires entire string to match the pattern
# import re
# text = "I love Python"
# result = re.fullmatch("Python", text)
# print(result)

# #re.findall() - it finds all occurances of a pattern and returns then as a list
# import re
# text = "I have 10 apples and 20 oranges"
# result = re.findall(r"\d+", text)
# print(result)
# #\d - digits (digits from 0 to 9)
# #\d+ - combination of one or more digits
# import re
# text = "I have 10 apples and 20 oranges"
# result2 = re.findall(r"\d", text)
# print(result2)

# #\w - word character - letters, digits, underscore
# import re
# text = "Python_123"
# result = re.findall(r"\w", text)
# print(result)

# #^ - start of string
# #the pattern must start at beginning
# import re
# pattern = r"^Python"
# print(re.search(pattern, "is easy Python"))

# #$ - pattern must end at the end of string
# import re
# pattern =r"Python$"
# print(re.search(pattern, "is easy Python"))

#r"^\d{4}$"

#quantifiers - It tells regex how many times something can occur
# *, +, ?, {}
#* - zero or more
#r"ab*" - a, ab, abb, abbbb, abbbbbb......
#because b can occur zero or more times

#+ - one or more
#r"ab+" - ab, abb, abbb, abbbb, abbbbb
# a is not valid here, because atleast 1 be needs to there

# ? - zero or more
#r"colour?r" - color, colour

#{} - exact number
#r"^\d{4}$" - means exactly 4 digits
#1234(correct) , 123(wrong), 12345(wrong)
# r"^\d{4, 6}$" - menas 4 to 6 digits are valid

#digits validation

# import re
# value = input()
# pattern = r"^\d+$"
# if re.fullmatch(pattern, value):
#     print("only digits")
# else:
#     print("invalid")


#phone number validation
# import re
# phone = input("Enter number:")
# pattern = r"^[6-9]\d{9}$"
# if re.fullmatch(pattern, phone):
#     print("Valid")
# else:
#     print("Invalid")


#Email Validation
#username@damain.com
# r"^[\w.-]+@[\w.-]+\.\w+$"
#[\w.-]+ -> username
#[\w.-]+ -> domain

# import re
# email = input("Enter email:")
# pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
# if re.fullmatch(pattern, email):
#     print("Valid")
# else:
#     print("Invalid")


import re
name = input("Enter name:")
password = input("Enter password:")
#name
if re.fullmatch(r"[A-Za-z]+",name):
    print("Valid")
else:
    print("Invalid")
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
if re.fullmatch(pattern, password):
    print("Valid")
else:
    print("Invalid")
