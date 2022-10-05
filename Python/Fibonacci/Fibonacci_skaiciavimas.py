#!/usr/bin/env python3

# Importuojamos naudojamos bibliotekos
import time
from matplotlib import pyplot as plt
import os
from functools import cache

# Fibonačio skaičiaus gavimas rekursiniu būdu
# Šaltinis - https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
def rekursinis(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return(rekursinis(x-1) + rekursinis(x-2))

# Fibonačio skaičiaus gavimas linijiniu būdu
# Šaltinis - https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
def dinaminis(x):
    a = 0 # Pirmas Fibonačio skaičius
    b = 1 # Antras Fibonačio skaičius
    if x == 0: # Spausdinamas pirmas Fibonačio skaičius
        return a
    elif x == 1: # Spausdinamas antras Fibonačio skaičius
        return b
    else:
        for i in range(2,x+1):
            c = a + b # Fibonačio skaičiui gauti atliekamas 2-jų prieš jį buvusių skaičių sumavimas
            a = b # Du sumuojami fibonačio skaičiai perstumiami į priekį per 1 poziciją
            b = c # Du sumuojami fibonačio skaičiai perstumiami į priekį per 1 poziciją
        return b

# Fibonačio skaičiaus gavimas matriciniu būdu
# Šaltinis - https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
def matricinis(x):
    # Fibonačio skaičių matrica
    F = [[1, 1],
         [1, 0]]
    if (x == 0):
        return 0
    # Fibonačio skaičių matrica yra perduodama į laipsnio kėlimo funkciją
    # Fibonačio skaičių matrica F yra dauginama pati iš savęs x kartų
    power(F, x)
    # Ieškomas Fibonačio skaičius yra F matricos pirmoje eilutėje bei pirmame stulpelyje
    return F[0][0]

# Atliekama matricų F ir M daugyba
# Kiekvienoje matricos F pozicijoje gaunamas tolimesnis Fibonačio skaičius
def multiply(F, M):
    # 1-a F matricos eilutė X 1-as M matricos stulpelis
    F11 = (F[0][0] * M[0][0] +
           F[0][1] * M[1][0])
    # 1-a F matricos eilutė X 2-as M matricos stulpelis
    F12 = (F[0][0] * M[0][1] +
           F[0][1] * M[1][1])
    # 2-a F matricos eilutė X 1-as M matricos stulpelis
    F21 = (F[1][0] * M[0][0] +
           F[1][1] * M[1][0])
    # 2-a F matricos eilutė X 2-as M matricos stulpelis
    F22 = (F[1][0] * M[0][1] +
           F[1][1] * M[1][1])
    # Gauti tolimesni Fibonačio skaičiai įtraukiami į F matricą
    F[0][0] = F11 # 1-a eilutė, 1-as stulpelis
    F[0][1] = F12 # 1-a eilutė, 2-as stulpelis
    F[1][0] = F21 # 2-a eilutė, 1-as stulpelis
    F[1][1] = F22 # 2-a eilutė, 2-as stulpelis

def power(F, x):
    # Pradinė Fibonačio skaičių matrica (Fibonačio skaičių eilės numeriai yra 2,1,1,0)
    M = [[1, 1],
         [1, 0]]
    # Fibonačio matrica F dauginama iš savęs x kartų
    # x - ieškomas Fibonačio skaičius
    for i in range(2, x):
        multiply(F, M)

# Fibonačio skaičiaus gavimas rekursiniu būdu
def Rekursinis(x):
    # Sąrašai (lists), skirti grafikui gauti
    # Gauti Fibonačio skaičiai
    Eile = [] # Gautų Fibonačio skaičių eilės numeriai
    Laikai = [] # Sąrašas laikų, per kuriuos gautas kiekvienas Fibonačio skaičius
    laikas = 0 # Laikas, per kurį randamas duotasis Fibonačio skaičius
    # Ciklas Fibonačio skaičiams gauti
    for i in range(0,x+1):
        """Fibonačio skaičiaus apskaičiavimas bei laiko jam gauti išmatavimas"""
        start = time.perf_counter()     # Pradedamas matuoti Fibonačio skaičiaus gavimo laikas
        print(i, "Fibonačio skaičius, gautas rekursiniu būdu, yra: ", rekursinis(i)) # Fibonačio skaičiaus skaičiavimas
        end = time.perf_counter()     # Baigiamas matuoti Fibonačio skaičiaus gavimo laikas
        laikas += (end-start) # Kiekvieno Fibonačio sikaičiaus radimo laikas
        Laikai.append(laikas) # Šis laikas pridedamas į laikų sąrašą
        print("Užtruko laiko:", laikas, "s") # Bendra suma išvedama į ekraną
        Eile.append(i)    # Gauto Fibonačio skaičiaus eilės numeris pridedamas į bendrą sąrašą
    """Grafiko su gautais duomenimis sudarymas"""
    plt.plot(Eile,Laikai)
    plt.xlabel("Fibonačio skaičiaus eilės numeris")
    plt.ylabel("Laikas, s")
    if (laikas < 60):
        print("Programos veikimo laikas: %.2f" % laikas+" s")
    if (laikas > 60):
        minutes = laikas / 60
        sekundes = laikas - int(minutes) * 60
        print("Programos veikimo laikas: %.0f" % minutes+" min. ir %.2f" % sekundes+" s")

# Fibonačio skaičiaus gavimas linijiniu būdu
def Dinaminis(x):
    Eile = []
    Laikai = []
    laikas = 0
    """Algoritmo implementacija"""
    for i in range(0,x+1):
        start = time.perf_counter()
        print(i, "Fibonačio skaičius, gautas linijiniu būdu, yra: ", dinaminis(i))
        end = time.perf_counter()
        laikas += (end-start)
        Laikai.append(laikas)
        print("Užtruko laiko:",laikas,"s")
        Eile.append(i)
    """Galutinis laikas"""
    if (laikas < 60):
        print("Programos veikimo laikas: %.2f" % laikas+" s")
    if (laikas > 60):
        minutes = laikas / 60
        sekundes = laikas - int(minutes) * 60
        print("Programos veikimo laikas: %.0f" % minutes+" min. ir %.2f" % sekundes+" s")
    """Grafiko su gautais duomenimis sudarymas"""
    plt.plot(Eile,Laikai)
    plt.xlabel("Fibonačio skaičiaus eilės numeris")
    plt.ylabel("Laikas, s")

# Fibonačio skaičiaus gavimas matriciniu būdu
def Matricinis(x):
    Eile = []
    Laikai = []
    laikas = 0
    for i in range(0,x+1):
        start = time.perf_counter()
        print(i, "Fibonačio skaičius, gautas matriciniu būdu, yra: ", matricinis(i))
        end = time.perf_counter()
        laikas += (end-start)
        Laikai.append(laikas)
        print("Užtruko laiko:", laikas)
    if (laikas < 60):
        print("Programos veikimo laikas: %.2f" % laikas+" s")
    if (laikas > 60):
        minutes = laikas / 60
        sekundes = laikas - int(minutes) * 60
        print("Programos veikimo laikas: %.0f" % minutes+" min. ir %.2f" % sekundes+" s")
        Eile.append(i)
    """Grafiko su gautais duomenimis sudarymas"""
    plt.plot(Eile,Laikai)
    plt.xlabel("Fibonačio skaičiaus eilės numeris")
    plt.ylabel("Laikas, s")

# Pagrindinė programa
if __name__ == "__main__":
    # Įvedamas norimo rasti Fibonačio skaičiaus eilės numeris bei įvestis konvertuojama į int tipą
    F = int(input("Kelintą Fibonačio skaičių norima rasti? "))
    metodas = input("Koks Fibonačio skaičiaus gavimo metodas bus naudojamas? ")

    if metodas == "Rekursinis":
        Rekursinis(F)
        plt.title("Fibonačio skaičiaus gavimas rekursiniu būdu")
        plt.legend(['Rekursinis'])
        plt.savefig(os.getcwd()+"/Grafikai/Rekursinis.png")

    if metodas == "Dinaminis":
        Dinaminis(F)
        plt.title("Fibonačio skaičiaus gavimas dinaminiu būdu")
        plt.legend(['Dinaminis'])
        plt.savefig(os.getcwd()+"/Grafikai/Dinaminis.png")

    if metodas == "Matricinis":
        Matricinis(F)
        plt.title("Fibonačio skaičiaus gavimas matriciniu būdu")
        plt.legend(['Matricinis'])
        plt.savefig(os.getcwd()+"/Grafikai/Matricinis.png")

    if metodas == "Dinaminis_Matricinis":
        Dinaminis(F)
        Matricinis(F)
        plt.title("Fibonačio skaičiaus gavimas dinaminiu ir matriciniu būdais")
        plt.legend(['Dinaminis', 'Matricinis'])
        plt.savefig(os.getcwd()+"/Grafikai/Dinaminis_ir_Matricinis.png")

    if metodas == "Rekursinis_Dinaminis_Matricinis":
        Rekursinis(F)
        Dinaminis(F)
        Matricinis(F)
        plt.title("Fibonačio skaičiaus gavimas rekursiniu, dinaminiu ir matriciniu būdais")
        plt.legend(['Rekursinis', 'Dinaminis', 'Matricinis'])
        plt.savefig(os.getcwd()+"/Grafikai/Rekursinis_Dinaminis_ir_Matricinis.png")

    # Grafiko atvaizdavimas naudojant tkinter GUI backend'ą
    plt.show()
