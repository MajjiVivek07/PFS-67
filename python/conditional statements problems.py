#conditional statemnts problems
#1) employee performnce evaluation

# name = input("Enter employee name: ")
# projects = int(input("Enter number of projects completed: "))
# rating = int(input("Enter performance rating: "))

# employee = {
#     "name": name,
#     "projects": projects,
#     "rating": rating
# }

# if rating >= 4 and projects >= 5:
#     status = "Excellent"
# elif rating >= 3 and projects >= 3:
#     status = "Good"
# elif rating >= 2:
#     status = "Needs Improvement"
# else:
#     status = "Poor"

# print("Employee Status:", status)

#2) number classification

# num = int(input("Enter an integer: "))

# if num == 0:
#     print("Zero")
# elif num > 0 and num % 2 == 0:
#     print("Positive and even")
# elif num > 0 and num % 2 != 0:
#     print("Positive and odd")
# elif num < 0 and num % 2 == 0:
#     print("Negative and even")
# else:
#     print("Negative and odd")

#3) shopping discount

# price = float(input("Enter product price: "))
# member = input("Customer membership status (yes/no): ")

# if price >= 10000 and member == "yes":
#     discount = 20
# elif price >= 10000 and member == "no":
#     discount = 15
# elif price >= 5000 and member == "yes":
#     discount = 10
# elif price >= 5000 and member == "no":
#     discount = 5
# else:
#     discount = 0

# discount_amount = price * discount / 100
# final_price = price - discount_amount

# print("Discount:", discount, "%")
# print("Final Price:", final_price)

#4) list element validation



#5) atm withdrawal validation

# balance = float(input("Enter account balance: "))
# withdrawal = float(input("Enter withdrawal amount: "))
# card = input("Enter card status (active/inactive): ").lower()
# pin = input("Enter PIN status (correct/incorrect): ").lower()

# if card != "active":
#     print("Withdrawal rejected: Card is inactive")
# elif pin != "correct":
#     print("Withdrawal rejected: PIN is incorrect")
# elif withdrawal <= 0:
#     print("Withdrawal rejected: Amount must be positive")
# elif withdrawal % 100 != 0:
#     print("Withdrawal rejected: Amount must be a multiple of 100")
# elif withdrawal > balance:
#     print("Withdrawal rejected: Insufficient balance")
# else:
#     balance = balance - withdrawal
#     print("Withdrawal successful")
#     print("Remaining balance:", balance)

#6) complex student scholorship

age=int  

       