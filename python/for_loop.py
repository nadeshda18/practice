#!/usr/bin/python3

# for loop will iterate over a sequence

for i in range(1, 11):
    print(i)
    if i == 5:
        break  # will stop after 5

print("Done")

for x in range(4, 40):
    if x % 4 == 0:
        print(x)
    else:
        continue  # will skip all numbers that are not divisible by 4

for y in range(5, 10):
    if y == 8:
        continue  # will print from 5 - 10 and skipping 8
    else:
        print(y)
