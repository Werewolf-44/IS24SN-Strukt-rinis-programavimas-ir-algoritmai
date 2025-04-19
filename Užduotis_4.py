#4. Dinaminio meniu kūrimas

#Sukurti konsolinę programą, kurioje sukurtumėte meniu su pasirenkamais punktais bei atitinkamai iškviečiama tam tikra funkcija pagal pasirinktą meniu punktą.

def pasisveikinti():
    print("Sveiki atvykę į mūsų programą!")

def parodyti_laika():
    from datetime import datetime
    dabar = datetime.now()
    print("Dabartinis laikas:", dabar.strftime("%Y-%m-%d %H:%M:%S"))

def atsisveikint():
    print("Ačiū, kad naudojotės mūsų programa!")
    exit()

while True:
    print("\nPasirinkite meniu punktą:")
    print("1. Pasisveikinti")
    print("2. Parodyti dabartinį laiką")
    print("3. Atsisveikinti")

    pasirinkimas = input("Įveskite savo pasirinkimą (1-3): ")

    if pasirinkimas == '1':
        pasisveikinti()
    elif pasirinkimas == '2':
        parodyti_laika()
    elif pasirinkimas == '3':
        atsisveikint()
    else:
        print("Neteisingas pasirinkimas, bandykite dar kartą.")