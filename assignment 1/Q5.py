import random as r

list1 = []
list2= []
for i in range(10):
    random_number1 = r.randint(10,30)
    list1.append(random_number1)

    random_number2 = r.randint(10,30)
    list2.append(random_number2)
print("list 1 is :",list1)
print("list 2 is :",list2)

# # 1>Common numbers in the two lists
# print(list(set(list1)&set(list2)))

# # 2> Unique numbers in both the list
# print(list(set(list1)|set(list2)))

# #3> Minimum in both the list
# print( min(list1))
# print(min(list2))

# # 4> Maximum in both the list
# print(max(list1))
# print(max(list2))

# # 5>Sum of both the lists
# sum_list = []
# for list1 , list2 in zip(list1 , list2):
#     sum_list.append(list1 +list2)

# print("sum list:" , sum_list)



