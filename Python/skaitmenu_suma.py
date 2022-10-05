#!/usr/bin/env python3

def Suma(var1):
    suma = 0
    skaitmenys = []
    while (var1 != 0):
        skaitmuo = int(var1) % 10
        skaitmenys.append(skaitmuo)
        var1 = int(var1) / 10
    #kiekis = len(skaitmenys)
    for x in skaitmenys:
        suma += skaitmenys[x]
    print(f"Skaiciaus skaitmenu suma yra {suma}")

skaicius = input("Iveskite skaiciu: ")
print(f"Skaicius yra {skaicius}")

Suma(skaicius)
