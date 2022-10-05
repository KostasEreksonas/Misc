#!/usr/bin/env python3

def conversion(var1):
    original = var1
    Result = 0

    # Determine how many digits does the binary number have
    count = -1
    while (var1 != 0):
        var1 = int(var1) / 10
        count += 1

    # Create None value arrays of size count to store binary digits and their corresponding decimal values (2^i)
    binaryArray = [None] * count
    decimalArray = [None] * count

    # Append binary number's digits to binaryArray in reverse order and calculate their decimal counterparts
    for i in range(count):
        binaryArray[i] = int(original) % 10
        if (binaryArray[i] >= 2):
            print("Binary numbers has only 0 or 1")
            break
        original = int(original) / 10
        decimalArray[i] = 2 ** i

    # If binary digit is 1, add it's decimal counterpart to the end result
    for j in range(count):
        if binaryArray[j] == 1:
            Result += decimalArray[j]
        elif binaryArray[j] == 0:
            Result += 0
    print(f"Decimal number is: {Result}")

binary = input("Input binary number: ")

conversion(binary)
