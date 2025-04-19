#8. Rekursija

#Sukurkite rekursyvią funkciją, kuri konvertuoja dešimtainį skaičių į dvejetainį skaičių.

def decimal_to_binary(n):
    if n == 0:
        return ''
    else:
        return decimal_to_binary(n // 2) + str(n % 2)
    
n = int(input("Įveskite dešimtainį skaičių: "))
print (f"Dešimtainis skaičius {n} dvejetainiu formatu: {decimal_to_binary(n)}")

#Sukurti rekursyvią funkciją, kuri apskaičiuotų sumavimą nuo 1 iki N.

def rekursyvus_sumavimas(n):
    if n == 1:
        return 1
    else:
        return n + rekursyvus_sumavimas(n - 1)

n = int(input("Įveskite skaičių N: "))
print(f"Sumavimas nuo 1 iki {n} yra: {rekursyvus_sumavimas(n)}")