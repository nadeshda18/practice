#!/usr/bin/python3
n1 = input("enter first number: ")
n2 = input("enter second number: ")
print("first number is: ", n1)
print("second number is: ", n2)

temp = n1
n1 = n2
n2 = temp

print("swapped numbers are: ", n1, n2)
