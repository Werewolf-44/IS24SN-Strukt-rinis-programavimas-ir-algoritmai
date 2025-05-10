import json
import hashlib
from abc import ABC, abstractmethod

# Composite Pattern Implementation


# Abstract Base Class (ABC) ir abstract metodai
class PasswordComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        """Privalomas metodas, kurį turi įgyvendinti visos vaikinės klasės.
        Naudojamas komponento atvaizdavimui konsolėje.
        """
        pass

    @abstractmethod
    def get_security_score(self):
        """Privalomas metodas, grąžinantis saugumo įvertinimą (skalėje 0-10).
        Turi būti implementuotas ir 'lapuose' (PasswordEntry), ir 'kompozituose' (PasswordCategory).
        """
        pass

    @abstractmethod
    def to_dict(self):
        """Privalomas metodas, konvertuojantis objektą į žodyną (dict),
        kad būtų galima išsaugoti į JSON failą.
        """
        pass

# Atskiras slaptažodis
class PasswordEntry(PasswordComponent):
    def __init__(self, username, password, website):
        self.username = username
        self._password_hash = self._hash_password(password)  # Slaptažodis saugomas kaip hash
        self.website = website

    def _hash_password(self, password):
        """Slaptažodžio šifravimas naudojant SHA-256 algoritmą.
        Hash'as yra vienpusė transformacija - atgal atkurti negalima!
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def display(self, indent=0):
        """Atvaizduojame slaptažodžio įrašą su įtrauktais tarpais (hierarchijos vizualizacija)."""
        print(f"{' ' * indent}🔒 {self.website} | User: {self.username} | Security: {self.get_security_score()}/10")
    
    def get_security_score(self):
        """Įvertina slaptažodžio stiprumą (čia supaprastinta logika).
        Realiai galima naudoti biblioteką 'zxcvbn' arba panašias.
        """
        length = len(self._password_hash)  # Hash ilgis != tikras slaptažodžio ilgis (čia tik pavyzdys)
        return min(10, max(1, length // 6))  # Imituojamas saugumo įvertis 1-10
    
    def to_dict(self):
        """Konvertuojame slaptažodžio įrašą į žodyną (dict), kad būtų galima išsaugoti į JSON faile."""
        return {
            "type": "entry",
            "username": self.username,
            "password_hash": self._password_hash,
            "website": self.website
        }

# Slaptažodžių grupė
    
class PasswordCategory(PasswordComponent):
    def __init__(self, name):
        self.name = name
        self.children = []  # Čia saugomi vaikiniai komponentai (PasswordEntry arba PasswordCategory)

    def add(self, component):
        """Prideda vaikinį komponentą (slaptažodį arba kitą kategoriją)."""
        self.children.append(component)

    def display(self, indent=0):
        """Atvaizduoja visą kategorijos hierarchiją su įtrauktais tarpais."""
        print(f"{' ' * indent}📁 {self.name} (Avg Security: {self.get_security_score()}/10)")
        for child in self.children:
            child.display(indent + 4)  # Rekursyviai kviečia vaikų display() metodus
    
    def get_security_score(self):
        """Skaičiuoja vidutinį saugumo įvertį visoms kategorijos dalims.
        Jei kategorija tuščia, grąžina 0.
        """
        if not self.children:
            return 0
        return sum(child.get_security_score() for child in self.children) // len(self.children)
    
    def to_dict(self):
        """Konvertuoja kategoriją ir jos vaikus į žodyną, kad būtų galima išsaugoti JSON faile."""
        return {
            "type": "category",
            "name": self.name,
            "children": [child.to_dict() for child in self.children]  # Rekursyviai kviečia vaikų to_dict()
        }

    
    # Failų operacijos (JSON)

def save_to_file(db, filename="passwords.json"):
    #Išsaugo slaptažodžių duomenų bazę į JSON failą."""
        with open(filename, 'w') as f:
            json.dump(db.to_dict(), f, indent=4)  # db.to_dict() rekursyviai konvertuoja visą hierarchiją į žodyną

def load_from_file(filename="passwords.json"):
    """Įkelia slaptažodžių duomenų bazę (db) iš JSON failo.
    Jei failas neegzistuoja, sukuria naują tuščią duomenų bazę.
    """
    try: 
        with open(filename, 'r') as f:
            data = json.load(f)
        return _dict_to_component(data)  # Konvertuoja žodyną atgal į komponentą (rekursyviai)
    except FileNotFoundError:
        return PasswordCategory("Kategorijos")  # Sukuria naują šakninę kategoriją
        
def _dict_to_component(data):
    """Rekursyviai konvertuoja žodyną iš JSON atgal į PasswordComponent objektus"""
    if data["type"] == "entry":
        entry = PasswordEntry(data["username"], "", data["website"])  # Slaptažodis nenurodytas (hash'as jau yra)
        entry._password_hash = data["password_hash"]  # Atstatomas hash'as
        return entry
    elif data["type"] == "category":
        category = PasswordCategory(data["name"])
        for child_data in data["children"]:
            category.add(_dict_to_component(child_data))  # Rekursyviai prideda vaikus
        return category
    
#Meniu
def print_menu():
    """Atspausdina pagrindinę programos meniu."""
    print("\n" + "=" * 30)
    print("Slaptažodžių tvarkyklė")
    print("=" * 30)
    print("1. Peržiūrėti visus slaptažodžius")
    print("2. Pridėti naują kategoriją")
    print("3. Pridėti naują slaptažodį")
    print("4. Išsaugoti ir išeiti")
    print("=" * 30)    
        
#Pagrindinė programos logika (konsolės meniu)

def main():
    db = load_from_file() # Užkrauna esamą DB arba sukuria naują

    while True:
        print_menu() # Rodomas meniu
        choice = input ("Pasirinkite veiksmą: ")

        if choice == "1":
            print ("\n[VISI SLAPTAŽODŽIAI]")
            db.display() # Rekursyviai atvaizduoja visą hierarchiją
        elif choice == "2":
            category_name = input ("Įveskite kategorijos pavadinimą: ")
            new_category = PasswordCategory(category_name)
            db.add(new_category) # Prideda naują kategoriją
        elif choice == "3":
            #Sukuria naują slaptažodį
            new_entry = PasswordEntry(
                input("Svetainė: "),
                input("Vartotojo vardas: "),
                input("Slaptažodis: "),
            )
            # Prideda jį pasirinktoje kategorijoje
            print("Esamos kategorijos:")
            for idx, child in enumerate(db.children):
                print (f'{idx + 1}, {child.name}')
            category_idx = int(input("Pasirinkite kategoriją (skaičius): ")) - 1
            db.children[category_idx].add(new_entry)
        elif choice == "4":
            save_to_file(db) # Išsaugo visą DB į failą
            print("Duomenys išsaugoti. Programa baigta")
            break
        else:
            print ("Neteisingas pasirinkimas. Bandykite dar kartą.")
    
if __name__ == "__main__":
    main()