
#conditional statements - excutes or works based on condition
#if, elif, else

#1. if statement - if means execute the code only when condition is true

#age = 22
#if age>=18:
 #   print("eligible")

#else
'''age= int(input())
if age >=21:
    print("alcohol permitted")
else:
    print("alcohol not permitted")   

 #nested- if condition
age=25
has_id=True
if age>=21:'''
#   print("age satisfied")
#if has_id:
# print("you can enter")

 #1) real time example -atm
 # is this card valid?
 # is this pin correct?
 # is there enough balance?
 # #withdraw

 #2) online shopping
 # is the product available?
 # login with account
 # is payment done?

 #1)atm
card = int(input("Enter card number: "))
if card != 8374718284:
    print("Invalid card number")
else:
    pin = int(input("Enter PIN: "))
    if pin != 12345:
        print("PIN is not correct")
    else:
        balance = 10000
        withdraw = int(input("Enter withdrawal amount: "))
        if withdraw >= balance:
            print("Insufficient amount")
        else:
            print("Withdrawal successful")



#2) online shopping

    


       
