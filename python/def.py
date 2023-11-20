#!/usr/bin/python3

def greet():
    name = input("What is your name? ")

    if len(name) > 0:
        print(f"Hello {name}")
    else:
        print("Please tell me your name")


greet()
