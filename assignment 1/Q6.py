# import random as r

# L=[]
# for i in range(100):
#     L.append(r.randint(100,900))

# print(L)

# #1> all odd numbers
# count =0

# for i in range (100):
#     if L[i]%2!=0:
#         count = count+1
# print("\n")
# print("number of odd numbers are: ",count)

# 2> all even numbers
# count =0

# for i in range (100):
#     if L[i]%2==0:
#         count = count+1
# print("\n")
# print("number of even numbers are: ",count)

# 3> all prime numbers
def is_Prime(n):
    if n<2:
        return False
    
    for i in range (2 , int(n**0.5)+1):
        if n%i ==0:
            return False
    return True
    

import random as r

L=[]
prime =[]
for i in range(100):
    random = r.randint(100,900)
    L.append(random)
    if is_Prime(random):
        prime.append(random)


print(L , "\n") 
print("\n so prime numbers are" , prime)
 
