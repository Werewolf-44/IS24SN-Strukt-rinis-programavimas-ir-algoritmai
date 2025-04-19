#3. Sąlygos ir ciklo sakiniai

#Parašykite programą, kuri patikrina, ar skaičius yra lyginis ar nelyginis.

skaicius = int(input("Įveskite skaičių: "))
if skaicius % 2 == 0:
    print(f"{skaicius} yra lyginis skaičius.")
else:
    print(f"{skaicius} yra nelyginis skaičius.")

#Sukurkite programą, kuri spausdina daugybos lentelę nuo 1 iki N.

N = int(input("Įveskite N: "))
for i in range(1, N + 1):
    print(f"Daugybos lentelė {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

#Raskite visus pirminius skaičius nuo 1 iki N.

N = int(input("Įveskite N: "))
print(f"Pirminiai skaičiai nuo 1 iki {N}:")
for num in range (2, N + 1):
    pirminis = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            pirminis = False
            break
    if pirminis:
        print(num)