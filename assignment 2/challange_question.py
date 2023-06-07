#taking a sample list
L = ["Ram", 1, "Shyam", 2, "Aman", 3]

for i in range (0,len(L)):#converting every element into string
    L[i] = str(L[i])
print(L)
L.sort()
print(L)
