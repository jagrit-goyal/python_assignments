
D={1:"One",2:"Two",3:"Three",4:"Four", 5:"Five"}

file_path ="dictionary.txt"

with open(file_path, "w") as file:
    for key , value in D.items():
        file.write(str(key) + ", " + value + "\n")

print("dictionary data is written to :" ,file_path)
file.close()
