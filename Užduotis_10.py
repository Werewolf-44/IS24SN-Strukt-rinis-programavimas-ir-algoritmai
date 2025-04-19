#10. Struktūros. Struktūrų masyvas ir operacijos

#Sukurkite struktūrą Automobilis, kuri turi markę, modelį, metus ir kainą. Leiskite vartotojui įvesti 5 automobilius ir rikiuokite pagal kainą.

from dataclasses import dataclass

@dataclass
class Automobilis:
    marke: str
    modelis: str
    metai: int
    kaina: float

print("Įveskite 5 automobilius:")
automobiliai = []
for i in range(5):
    marke = input(f"Automobilio {i+1} markė: ")
    modelis = input(f"Automobilio {i+1} modelis: ")
    metai = int(input(f"Automobilio {i+1} metai: "))
    kaina = float(input(f"Automobilio {i+1} kaina: "))
    automobiliai.append(Automobilis(marke, modelis, metai, kaina))
    print()

automobiliai.sort(key=lambda x: x.kaina) #Rikiuojame automobilius pagal kainą
print("Automobiliai rikiuoti pagal kainą:")
for automobilis in automobiliai:
    print(f"Markė: {automobilis.marke}, Modelis: {automobilis.modelis}, Metai: {automobilis.metai}, Kaina: {automobilis.kaina}")

#Parašykite programą, kuri saugo darbuotojų informaciją ir randa didžiausią atlyginimą turintį darbuotoją.

@dataclass
class Darbuotojas:
    vardas: str
    pavarde: str
    amzius: int
    atlyginimas: float

print("Kiek darbuotojų norite įvesti?:")
darbuotojai = []
kiekis = int(input())
for i in range(kiekis):
    vardas = input(f"Darbuotojo {i+1} vardas: ")
    pavarde = input(f"Darbuotojo {i+1} pavardė: ")
    amzius = int(input(f"Darbuotojo {i+1} amžius: "))
    atlyginimas = float(input(f"Darbuotojo {i+1} atlyginimas: "))
    darbuotojai.append(Darbuotojas(vardas, pavarde, amzius, atlyginimas))
    print()

darbuotojas_max_atlyginimas = max(darbuotojai, key=lambda x: x.atlyginimas) #Rasti darbuotoją su didžiausiu atlyginimu
print(f"Didžiausią atlyginimą turintis darbuotojas: {darbuotojas_max_atlyginimas.vardas} {darbuotojas_max_atlyginimas.pavarde}, Atlyginimas: {darbuotojas_max_atlyginimas.atlyginimas}")



