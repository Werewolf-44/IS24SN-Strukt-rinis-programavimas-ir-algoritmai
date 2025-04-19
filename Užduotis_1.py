#Algoritmai. Jų paskirtis ir funkcijos

#Parašykite algoritmą, kuris suskaičiuoja kiek yra skaičių, dalinamų iš 7 nuo 1 iki N.

skaičius = int(input("Įveskite skaičių: "))
kiekis = 0	
for i in range (1, skaičius + 1):
    if i % 7 == 0:
        kiekis += 1
print("Skaičių, dalinamų iš 7, kiekis nuo 1 iki", skaičius, "yra:", kiekis)

# Parašykite algoritmą, kuris suranda didžiausią ir mažiausią skaičių iš trijų įvestų skaičių iš klaviatūros.

skaičius1 = int(input("Įveskite pirmą skaičių: "))
skaičius2 = int(input("Įveskite antrą skaičių: "))
skaičius3 = int(input("Įveskite trečią skaičių: "))

Didžiausias = max (skaičius1, skaičius2, skaičius3)
Mažiausias = min (skaičius1, skaičius2, skaičius3)

print("Didžiausias skaičius:", Didžiausias)
print("Mažiausias skaičius:", Mažiausias)