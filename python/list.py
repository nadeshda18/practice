#!/usr/bin/python3

# list are mutable, they can be changed
# duplicate values are allowed

list1 = [1, "Nadja", "Volvo", 1954]
print(list1[1])
print(list1[2])
print(len(list1))
print(len(list1[2]))

list1.append(2)  # add at the end
print(list1)

list1.insert(1, "Schnuppe")  # insert at index number
print(list1)

list1.remove("Nadja")  # remove name
print(list1)

list1.remove(list1[3])  # remove at index number
print(list1)
