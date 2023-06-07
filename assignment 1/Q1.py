L= [11 , 12 , 13 , 14]


# # 1> WAP to add 50 and 60 to L. 
# L.append(50)
# L.append(60)
# print(L)

# # 2> WAP to remove 11 and 13 from L
# L.pop(0)
# L.pop(1)#taking index after removing 11
# print(L)

# # 3> WAP to sort L in ascending order.
# L.sort(reverse = False)
# print(L)

# # 4>WAP to sort L in descending order.
# L.sort(reverse = True)
# print(L)

# # 5> WAP to search for 13 in L.
# print(L.index(13))

# #6>WAP to count the number of elements present in L
# print(len(L))

# #7> WAP to sum all the elements in L.
# s= 0
# for i in range(0,len(L)):
#     s = s+ L[i]
# print("sum of all elemnts is :" , s)

# # 8> WAP to sum all ODD numbers in L.
# s= 0
# for i in range(1,len(L),2):
#     s = s+ L[i]
# print("sum of odd elemnts is :" , s)

# # 9> WAP to sum all EVEN numbers in L
# s= 0
# for i in range(0,len(L),2):
#     s = s+ L[i]
# print("sum of even elemnts is :" , s)

# #10>  WAP to sum all PRIME numbers in L.
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def sum_prime_numbers(lst):
#     sum_primes = 0
#     for num in lst:
#         if is_prime(num):
#             sum_primes += num
#     return sum_primes
# result = sum_prime_numbers(L)
# print(result)

# # 11> WAP to clear all the elements in L.
# L.clear()
# print(L)

# # 12> WAP to delete L.
# del L
