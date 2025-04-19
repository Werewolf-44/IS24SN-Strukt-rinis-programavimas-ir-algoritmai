#5. Paprastieji duomenų tipai. Operacijos su jais

#Sukurkite programą, kuri konvertuoja valandas į minutes ir sekundes.

valandos = float(input("Įveskite valandas: "))
minutes = valandos * 60
sekundes = valandos * 3600
print(f"{valandos} valandos yra {minutes} minutės ir {sekundes} sekundės.")

#Parašykite programą, kuri apskaičiuoja kiek įvestas žodis arba sakinys turi balsių ir priebalsių bei išvesti į ekraną atsakymą.

zodis = input("Įveskite žodį: ")
balsiai = "aąeęėiįouųū"
balsiai_kiekis = 0
priebalsiai_kiekis = 0
for raide in zodis:
    if raide.isalpha():
        if raide in balsiai:
            balsiai_kiekis += 1
        else:
            priebalsiai_kiekis += 1
print(f"Žodyje '{zodis}' yra {balsiai_kiekis} balsių ir {priebalsiai_kiekis} priebalsių.")