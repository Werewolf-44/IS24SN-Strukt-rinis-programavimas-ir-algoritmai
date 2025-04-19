#7. Funkcijos

#Parašykite funkciją, kuri apskaičiuoja dviejų skaičių didžiausią bendrą daliklį (DBD).

def didziausias_bendras_daliklis(a, b):
    while b:
        a, b = b, a % b
    return a

skait1 = int(input("Įveskite pirmą skaičių: "))
skait2 = int(input("Įveskite antrą skaičių: "))
print(f"Didžiausias bendras daliklis: {didziausias_bendras_daliklis(skait1, skait2)}")

#Parašykite funkciją, kuri sugeneruoja n-tojo Fibonačio skaičiaus reikšmę.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    

n = int(input("Įveskite n: "))
print(f"Fibonacci skaičius: {fibonacci(n)}")

#Sukurkite funkciją, kuri paverčia temperatūrą iš Celsijaus į Farenheitą ir atvirkščiai.

def temperaturos_konvertavimas(temperatura, skalė):
    if skalė == 'C':
        return (temperatura * 9/5) + 32
    elif skalė == 'F':
        return (temperatura - 32) * 5/9
    else:
        raise ValueError("Neteisinga skalė. Naudokite 'C' arba 'F'.")
    
temperatura = float(input("Įveskite temperatūrą: "))
skalė = input("Įveskite pateiktos temperatūros skalę (C/F): ").upper()

print(f"Temperatūra: {temperaturos_konvertavimas(temperatura, skalė)}")