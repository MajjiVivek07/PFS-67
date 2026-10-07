#file handling

#file handling - it provides create files, open files, read files, write files, add files, update files, close files
#types of modes
#modes          #meaning
#r              read
#w              write
#a              append
#x              create
#rb             read binary
#wb             write binary

# file=open("file handling1","r")
# data = file.read()
# print(data)
# file.close()

#readline() - it reads only one line
# file=open("file handling1","r")
# data=file.readline()
# print(data)
# file.close

#readlines - read all lines nd return them as list
# file=open("file handling1","r")
# data=file.readlines()
# print(data)
# file.close

#writing a file
# file=open("python/filehandling1","w")
# file.write("vivek\n")
# file.close()

#real time example: student record
# name = input("enter student name:")
# age=input("enter age")
# course=input("enter course:")
# with open("python/filehandling1","a") as file:
#     file.write(f"name:{name}\n")
#     file.write(f"age:{age}\n")
#     file.write(f"course:{course}\n")
# print("student details saved successfully.")  

#atm machine
balance = 10000

try:
    amount = int(input("Enter withdraw amount: "))

    if amount <= 0:
        raise ValueError("Amount must be positive")

    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount

        with open("transactions.txt", "a") as file:
            file.write(f"Withdrawn: {amount}\n")
            file.write(f"Rem bal: {balance}\n")

        print("Success")
        print("Rem bal:", balance)

except ValueError as e:
    print("Error:", e)



