#!/usr/bin/env python3

def palindrome(var1):
    org = var1
    org2 = var1
    count = -1
    reverse = 0
    while (var1 != 0):
        var1 = int(var1) / 10
        count += 1
    numberArray = [None] * count
    for i in range(count):
        numberArray[i] = int(org) % 10
        org = int(org) / 10
        print(f"Number {i} is {numberArray[i]}")
    for j in range(count):
        if (j == count-1):
            reverse = (reverse + numberArray[j])
        else:
            reverse = (reverse + numberArray[j])*10
    print(f"Original number: {org2}; Reverse number: {reverse}")
    if (reverse == int(org2)):
        print(f"Number {org2} is a palindrome")
    else:
        print(f"Number {org2} is not a palindrome")

number = input("Input number: ")
palindrome(number)
