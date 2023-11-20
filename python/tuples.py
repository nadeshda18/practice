#!/usr/bin/python3

# tuples are immutable, once created can not be changed
# duplicate values are allowed

tuple1 = (10, 1, -10, 15, 20)
tuple2 = ("Hello", "world", "how", "are")
tuple3 = ("hello", 10, -5, "world")
tuple4 = (tuple1, tuple2, tuple3)

print(tuple1)
print(tuple2)
print(tuple3)
print()  # print a new line
print(len(tuple1))  # counts the number of indexes
print(len(tuple2))
print(len(tuple3))
print(tuple1[0])  # prints the value from index 0
print(tuple2[1])
print(tuple3[2])
print()
print(tuple1[:2])  # print from index 0 until 2 but not including 2
print(tuple2[2:3])  # print index 2-3 not including 3
print(tuple3[1:2])
print()
print(tuple4)
print(len(tuple4))
print()
print(min(tuple1))
print(max(tuple1))
