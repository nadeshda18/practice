#!/usr/bin/python3

# sets are unordered
# sets do not allow duplicates
# sets do not use indexes
# sets are mutable and can be changed

set1 = {10, True, 'Nadja'}
set2 = {5, False, 'Schnuppe'}
set3 = set()  # will create an empty set
set4 = {}  # !!Will create a dict and not an empty set

print(set1)  # will print True, 10, Nadja
print(set2)  # will print False, 5, Schnuppe
print(type(set3))
print(type(set4))
print()

set1.add(20)  # add at the end
set2.add('Father')
print(set1)
print(set2)

set1.remove(True)
print(set1)
