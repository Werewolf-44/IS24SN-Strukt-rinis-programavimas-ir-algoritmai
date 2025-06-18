import json
import hashlib
from zxcvbn import zxcvbn
from abc import ABC, abstractmethod

# Composite Pattern Implementation

# Abstract Base Class (ABC) ir abstract metodai
class PasswordComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        # Privalomas metodas, kurį turi įgyvendinti visos vaikinės klasės. Naudojamas komponento atvaizdavimui konsolėje.
        pass

    @abstractmethod
    def get_security_score(self):
        # Privalomas metodas, grąžinantis saugumo įvertinimą (skalėje 0-10).
        pass

    @abstractmethod
    def to_dict(self):
        # Privalomas metodas, konvertuojantis objektą į žodyną (dict), kad būtų galima išsaugoti į JSON failą.
        pass

# Atskiras slaptažodis
class PasswordEntry(PasswordComponent):
    def __init__(self, username, password, website):
        self.username = username
        self._password = password # Laikinas slaptažodis saugomas atmintyje (nėra saugomas faile)
        self._password_hash = self._hash_password(password)  # Slaptažodis saugomas kaip hash
        self.website = website

    def _hash_password(self, password):
        # Slaptažodžio šifravimas naudojant SHA-256 algoritmą. Hash'as yra vienpusė transformacija - atgal atkurti negalima!
        return hashlib.sha256(password.encode()).hexdigest()

    def display(self, indent=0):
        # Atvaizduojame slaptažodžio įrašą su įtrauktais tarpais (hierarchijos vizualizacija).
        print(f"{' ' * indent}🔒 {self.website} | User: {self.username} | Security: {self.get_security_score()}/10")
    
    def get_security_score(self):
        # Įvertina slaptažodžio stiprumą naudodamas zxcvbn biblioteką.
        if self._password:
            result = zxcvbn(self._password)
            score = result['score']
            return (score + 1) * 2  # Paverčiame į skalę nuo 2 iki 10
        return 0  # Jei slaptažodis nenurodytas, grąžiname 0
    
    def to_dict(self):
        # Konvertuojame slaptažodžio įrašą į žodyną (dict), kad būtų galima išsaugoti į JSON faile.
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
        self.children = []  # Čia saugomi vaikiniai komponentai.

    def add(self, component):
        # Prideda vaikinį komponentą (slaptažodį arba kitą kategoriją).
        self.children.append(component)

    def display(self, indent=0):
        # Atvaizduoja visą kategorijos hierarchiją su įtrauktais tarpais.
        print(f"{' ' * indent}📁 {self.name} (Avg Security: {self.get_security_score()}/10)")
        for child in self.children:
            child.display(indent + 4)  # Kviečia vaikinius display() metodus
    
    def get_security_score(self):
        # Skaičiuoja vidutinį saugumo įvertį visoms kategorijos dalims. Jei kategorija tuščia, grąžina 0.
        if not self.children:
            return 0
        return sum(child.get_security_score() for child in self.children) // len(self.children)
    
    def to_dict(self):
        # Konvertuoja kategoriją ir jos vaikinius įrašus į žodyną, kad būtų galima išsaugoti JSON faile.
        return {
            "type": "category",
            "name": self.name,
            "children": [child.to_dict() for child in self.children] 
        }

# Failų operacijos (JSON)

def save_to_file(db, filename="passwords.json"):
    # Išsaugo slaptažodžių duomenų bazę į JSON failą."""
        with open(filename, 'w') as f:
            json.dump(db.to_dict(), f, indent=4)  # db.to_dict() konvertuoja visą hierarchiją į žodyną

def load_from_file(filename="passwords.json"):
    # Įkelia slaptažodžių duomenų bazę (db) iš JSON failo. Jei failas neegzistuoja, sukuria naują tuščią duomenų bazę.
    try: 
        with open(filename, 'r') as f:
            data = json.load(f)
        return _dict_to_component(data)  # Konvertuoja žodyną atgal į komponentą.
    except FileNotFoundError:
        return PasswordCategory("Kategorijos")  # Sukuria naują šakninę kategoriją
    
def delete_entry_or_category(db):
    print("\n[ŠALINTI SLAPTAŽODĮ ARBA KATEGORIJĄ]")
    if not db.children:
        print("Nėra jokių kategorijų ar slaptažodžių.")
        return
    for idx, child in enumerate(db.children):
        print(f"{idx + 1}. 📁 {child.name}")

    try:
        category_idx = int(input("Pasirinkite kategoriją): ")) - 1
        category = db.children[category_idx]

        print(f'\n{category.name} turinys')
        if not category.children:
            confirm = input("Ši kategorija tuščia. Ar tikrai norite ją ištrinti? (taip/ne): ").strip().lower()
            if confirm == 'taip':
                db.children.pop(category_idx)
                print(f"Kategorija '{category.name}' ištrinta.")
            return
        
        for j, sub in enumerate(category.children):
            if isinstance(sub, PasswordEntry):
                print(f"{j + 1}. 🔒 {sub.website} | User: {sub.username}")
            elif isinstance(sub, PasswordCategory):
                print(f"{j + 1}. 📁 {sub.name}")
                      
        sub_idx = input("Pasirinkite ką trinti (skaičius), arba spauskite Enter, kad trinti visą kategoriją: ").strip()

        if sub_idx == "":
            confirm = input(f"Ar tikrai norite ištrinti visą kategoriją '{category.name}'? (taip/ne): ").strip().lower()
            if confirm == "taip":
                db.children.pop(category_idx)
                print("Kategorija ištrinta.")
            else:
                print("Veiksmas atšauktas.")
        else:
            sub_idx = int(sub_idx) - 1
            removed = category.children.pop(sub_idx)
            if isinstance(removed, PasswordEntry):
                print(f"Slaptažodis '{removed.website}' ištrintas.")
            else:
                print(f"Kategorija '{removed.name}' ištrinta.")

    except (ValueError, IndexError):
        print("Neteisingas pasirinkimas. Bandykite dar kartą.")

        
def _dict_to_component(data):
    # Konvertuoja žodyną iš JSON atgal į PasswordComponent objektus.
    if data["type"] == "entry":
        entry = PasswordEntry(data["username"], "", data["website"])
        entry._password_hash = data["password_hash"]
        entry._password = None
        return entry
    elif data["type"] == "category":
        category = PasswordCategory(data["name"])
        for child_data in data["children"]:
            category.add(_dict_to_component(child_data))
        return category
    
# Meniu
def print_menu():
    # Atspausdina pagrindinį programos meniu.
    print("\n" + "=" * 30)
    print("Slaptažodžių tvarkyklė")
    print("=" * 30)
    print("1. Peržiūrėti turimas paskyras")
    print("2. Pridėti naują kategoriją")
    print("3. Pridėti naują slaptažodį")
    print("4. Ištrinti slaptažodžį arba kategoriją")
    print("5. Išsaugoti ir išeiti")
    print("=" * 30)    
        
# Pagrindinė programos logika (konsolės meniu)

def main():
    db = load_from_file() # Užkrauna esamą DB arba sukuria naują

    while True:
        print_menu() # Rodomas meniu
        choice = input ("Pasirinkite veiksmą: ")

        if choice == "1":
            print ("\n[VISI SLAPTAŽODŽIAI]")
            db.display() # Atvaizduoja visą hierarchiją
        elif choice == "2":
            category_name = input ("Įveskite kategorijos pavadinimą: ")
            new_category = PasswordCategory(category_name)
            db.add(new_category) # Prideda naują kategoriją
        elif choice == "3":
            # Sukuria naują slaptažodį
            new_entry = PasswordEntry(
                input("Vartotojo vardas: "),
                input("Slaptažodis: "),
                input("Svetaine: "),
            )
            # Prideda slaptažodį pasirinktoje kategorijoje
            print("Esamos kategorijos:")
            for idx, child in enumerate(db.children):
                print (f'{idx + 1}, {child.name}')
            category_idx = int(input("Pasirinkite kategoriją į kurią norite įkelti slaptažodį (skaičius): ")) - 1
            db.children[category_idx].add(new_entry)
        elif choice == "4":
            delete_entry_or_category(db)
        elif choice == "5":
            save_to_file(db) # Išsaugo visą DB į failą
            print("Duomenys išsaugoti. Programa baigta")
            break
        else:
            print ("Neteisingas pasirinkimas. Bandykite dar kartą.")
    
if __name__ == "__main__":
    main()