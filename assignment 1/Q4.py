# # 1>WAP to print 100 random strings whose length between 6 and 8.
# import random as r
# import string as s

# print("random strings are: ")
# for i in range (1, 101):
#     print("".join(r.sample(s.ascii_letters,r.randint(6,8))))
    


# # 2> WAP to print all prime numbers between 600 and 800
# def is_prime(n):
#     if n<2:
#         return False
#     for i in range (2 , int(n//2)+1):
#         if n%i ==0:
#             return False
#     return True

# for i in range(600 , 800+1):
#     if is_prime(i):
#         print(i)

# #3> WAP to print all numbers between 100 and 1000 that are divisible by 7 and 9.
# for i in range (100 , 1000+1):
#     if i%7 ==0 and i % 9==0:
#         print(i)
