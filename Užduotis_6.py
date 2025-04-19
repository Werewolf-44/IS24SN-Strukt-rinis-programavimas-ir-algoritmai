#6. Masyvai. Dvimačiai masyvai

#Sukurkite programą, kuri generuoja atsitiktinį skaičių masyvą ir suranda vidurkį.

import random

dydis = random.randint(1, 100)
masyvas = [random.randint(1, 100) for _ in range(dydis)]
print(f"Sugeneruotas masyvas:, {masyvas}")

vidurkis = sum(masyvas) / len(masyvas)
print(f"Masyvo vidurkis:, {vidurkis}")

#Sukurkite programą, kuri randa didžiausią ir mažiausią skaičių masyve.

didziausias = max(masyvas)
maziausias = min(masyvas)

print(f"Didžiausias skaičius masyve: {didziausias}")
print(f"Mažiausias skaičius masyve: {maziausias}")

#Parašykite programą, kuri randa daugiausiai pasikartojantį skaičių masyve.

from collections import Counter

dažniausias = Counter(masyvas).most_common(1)[0][0]
print(f"Daugiausiai pasikartojantis skaičius masyve: {dažniausias}")

#Sukurkite programą, kuri apskaičiuoja matricos determinanto reikšmę (2x2 arba 3x3).

def skaiciuoti_determinanta_3x3(matrica):
    a = matrica[0][0]
    b = matrica[0][1]
    c = matrica[0][2]
    d = matrica[1][0]
    e = matrica[1][1]
    f = matrica[1][2]
    g = matrica[2][0]
    h = matrica[2][1]
    i = matrica[2][2]

    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

def skaiciuoti_determinanta_2x2(matrica):
    a = matrica[0][0]
    b = matrica[0][1]
    c = matrica[1][0]
    d = matrica[1][1]

    return a * d - b * c

print("Pasirinkite matricos dydį (2x2 arba 3x3):")
dydis = int(input("Įveskite 2 arba 3: "))

if dydis == 2:
    print("Įveskite 2x2 matricos elementus:")
    matrica = [[int(input(f"Elementas [{i}][{j}]: ")) for j in range(2)] for i in range(2)]
    determinantas = skaiciuoti_determinanta_2x2(matrica)
    print(f"2x2 matricos determinantas: {determinantas}")
elif dydis == 3:
    print("Įveskite 3x3 matricos elementus:")
    matrica = [[int(input(f"Elementas [{i}][{j}]: ")) for j in range(3)] for i in range(3)]
    determinantas = skaiciuoti_determinanta_3x3(matrica)
    print(f"3x3 matricos determinantas: {determinantas}")
