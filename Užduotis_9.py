#9. Failai. Operacijos su jais

#Sukurkite programą, kuri įrašo į failą studentų vardus ir pažymius, taip pat įvestą informaciją nuskaito ir atvaizduoja į ekraną.

def irasyti_i_faila(vardas, pazymys):
    with open('studentai.txt', 'a') as failas:
        failas.write(f'{vardas}, {pazymys}\n')  # 'a' - append, kad nepradėtų iš naujo rašyti failo
    print(f'Studentas {vardas} su pažymiu {pazymys} įrašytas į failą.')

def nuskaityti_is_failo():
    try:
        with open('studentai.txt', 'r') as failas:  # 'r' - read, kad galėtume skaityti failą
            print('Failo turinys:')
            for eilute in failas:
                print(eilute.strip())  # .strip() pašalina naujos eilutės simbolius
    except FileNotFoundError:
        print('Failas nerastas.')

print('Pasirinkite veiksmą:')
print('1. Įrašyti studentą')
print('2. Nuskaityti studentus iš failo')
print('3. Išeiti')
while True:
    pasirinkimas = input('Įveskite pasirinkimą (1/2/3): ')
    if pasirinkimas == '1':
        vardas = input('Įveskite studento vardą: ')
        pazymys = input('Įveskite studento pažymį: ')
        irasyti_i_faila(vardas, pazymys)
    elif pasirinkimas == '2':
        nuskaityti_is_failo()
    elif pasirinkimas == '3':
        print('Išeinama iš programos.')
        break
    else:
        print('Neteisingas pasirinkimas. Bandykite dar kartą.')


#Parašykite programą, kuri nuskaito failą ir suskaičiuoja žodžių skaičių jame.


def skaiciuoti_zodzius_faile(failo_pavadinimas):
    try:
        with open(failo_pavadinimas, 'r') as failas:
            turinys = failas.read() # Nuskaito visą failo turinį
            zodziai = turinys.split()  # Padalina tekstą į žodžius
            zodziu_skaicius = len(zodziai)  # Suskaičiuoja žodžių skaičių
            print(f'Žodžių skaičius faile "{failo_pavadinimas}": {zodziu_skaicius}')
    except FileNotFoundError:
        print('Failas nerastas.')


print('Įrašykite failo pavadinimą, kurį norite nuskaityti (pvz., "studentai.txt"):') #Failas gali būti bet koks tekstinis failas, pavyzdžiui, "studentai.txt". iš pirmos šios užduoties dalies.
failo_pavadinimas = input()
skaiciuoti_zodzius_faile(failo_pavadinimas)
