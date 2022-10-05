#!/usr/bin/env python3

# Get number of words
numofWords = input("Input number of words to count letters of: ")

# Initialize words list to store the number of words specified previously
words = [None] * int(numofWords)

# Input words and put them into words list
for i in range(int(numofWords)):
    word = input(f"Input word {i+1}: ")
    words[i] = word

# Count letters in each word
longest = 0
for x in words:
    length = len(x)
    if length > longest:
        longest = length
        longestWord = x
    print(f"Length of the given word {x} is {length} letters")
print(f"Longest word is {longestWord}, having {longest} letters")
