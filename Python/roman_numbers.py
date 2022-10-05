#!/usr/bin/env python3

letters = ["I", "V", "X", "L", "C", "D", "M"]
numbers = [1, 5, 10, 50, 100, 500, 1000]

roman = input("Enter roman number: ")
list = []
number = 0
    if (letter == letters[0]):
        number += numbers[0]
    elif (letter == letters[1]):
        number += numbers[1]
    elif (letter == letters[2]):
        number += numbers[2]
    elif (letter == letters[3]):
        number += numbers[3]
    elif (letter == letters[4]):
        number += numbers[4]
    elif (letter == letters[5]):
        number += numbers[5]
    elif (letter == letters[6]):
        number += numbers[6]

print(number)
print(list)
