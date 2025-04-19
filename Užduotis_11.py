#11. Rodyklės tipas. Dinaminiai kintamieji. Dinaminiai masyvai


#Kadangi Python nesinaudoja tiesioginėmis rodyklėmis ir dinamine atmintimi taip, kaip, C ar C++, todėl negalime tiesiogiai naudoti 
#rodyklių. Python kalba turi dinamišką atminties valdymą ir valdo atmintį už pati. Nors rodyklių tiesioginis valdymas 
#nėra galimas su Python, žemiau pamėginau simuliuoti rodyklių naudojimą ir atlikti užduotis.


#Sukurkite programą, kuri sukeičia dvi reikšmes vietomis naudojant rodykles.

def sukeisti_vietomis(a, b):
    temp = a
    a = b
    b = temp
    return a, b

#Įveskite dvi skaičių reikšmes
a = int(input("Įveskite pirmą skaičių: "))
b = int(input("Įveskite antrą skaičių: "))

#Sukeičiam vietomis
a, b = sukeisti_vietomis(a, b)

print(f"Sukeistos vietomis reikšmės: a = {a}, b = {b}")

#Įgyvendinkite dinaminį masyvą, kuris kinta kiekvieną kartą, kai vartotojas įveda naują skaičių.

from typing import List

def dinaminis_masyvas() -> None:
    masyvas: List[int] = []  # Pradinis tuščias masyvas
    while True:
        try:
            skaicius = int(input("Įveskite skaičių (0 norint baigti): "))
            if skaicius == 0:
                print("Įvedimas baigtas.")
                break
            masyvas.append(skaicius)  # Pridedame naują skaičių į masyvą
        except ValueError:
            print("Prašome įvesti galiojantį skaičių.")
    
    print(f"Galutinis masyvas: {masyvas}")

dinaminis_masyvas()

#Parašykite programą, kuri saugo tekstą dinaminėje atmintyje ir leidžia jį keisti dinamiškai.

def dinaminis_tekstas() -> None:
    tekstas = ""  # Pradinis tuščias tekstas
    while True:
        naujas_tekstas = input("Įveskite tekstą (spausti ""Enter"" norint baigti): ")
        if naujas_tekstas == "":
            print("Įvedimas baigtas.")
            break
        tekstas += naujas_tekstas + " "  # Pridedame naują tekstą
    print(f"Galutinis tekstas: {tekstas.strip()}")

dinaminis_tekstas()
