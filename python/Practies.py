l1 = [12,23,34,45,56,78,4,56,20000,45,96]
# # print(max(l1))
# # print(min(l1))
# highest=l1
# lowest=l1
# for num in l1:
#     if num>l1:
#         highest=num
#         print(highest)
#     if num<l1:
#         lowest=num
#         print(lowest)

lowest = l1[0]
highest = l1[0]
for i in l1:
    if i > highest :
        highest = i
print(highest)
for i in l1:
    if i<lowest:
        lowest=i
print(lowest)        