#!/usr/bin/python3
# how many days, month, years until your 90

age = input("What is your age? ")

days = (90 * 365) - (365 * int(age))
week = (90 * 52) - (52 * int(age))
month = (90 * 12) - (12 * int(age))

print(
    f"You have {days} Days, and {week} Weeks and {month} Month until your 90 years old")
