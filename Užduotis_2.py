#2. Kintamieji. Pagrindinės programinės konstrukcijos. Priskyrimo sakinys. Sudėtinis sakinys

#Parašykite programą, kuri konvertuoja centimetrus į metrus ir atvirkščiai.

print("Pasirinkite konvertavimą:")
print("1. Centimetrai į metrus")
print("2. Metrai į centimetrus")

pasirinkimas = input("Įveskite pasirinkimą (1 arba 2): ")
if pasirinkimas == "1":
    centimetras = float(input("Įveskite centimetrus: "))
    metras = centimetras / 100
    print(f"{centimetras} cm yra {metras} m")
elif pasirinkimas == "2":
    metras = float(input("Įveskite metrus: "))
    centimetras = metras * 100
    print(f"{metras} m yra {centimetras} cm")
else:
    print("Neteisingas pasirinkimas. Pasirinkite 1 arba 2.")

#Sukurkite skaičiuotuvą, kuris leidžia atlikti sudėtį, atimtį, daugybą ir dalybą.

print("Pasirinkite aritmetinį veiksmą:")
print("1. Sudėtis")
print("2. Atimtis")
print("3. Daugyba")
print("4. Dalyba")

veiksmas = input("Įveskite pasirinkimą (1, 2, 3 arba 4): ")
skaičius1 = float(input("Įveskite pirmą skaičių: "))
skaičius2 = float(input("Įveskite antrą skaičių: "))
if veiksmas == "1":
    rezultatas = skaičius1 + skaičius2
    print(f"{skaičius1} + {skaičius2} = {rezultatas}")
elif veiksmas == "2":
    rezultatas = skaičius1 - skaičius2
    print(f"{skaičius1} - {skaičius2} = {rezultatas}")
elif veiksmas == "3":
    rezultatas = skaičius1 * skaičius2
    print(f"{skaičius1} * {skaičius2} = {rezultatas}")
elif veiksmas == "4":
    if skaičius2 != 0:
        rezultatas = skaičius1 / skaičius2
        print(f"{skaičius1} / {skaičius2} = {rezultatas}")
    else:
        print("Dalyba iš nulio negalima.")
else:
    print("Neteisingas pasirinkimas. Pasirinkite 1, 2, 3 arba 4.")