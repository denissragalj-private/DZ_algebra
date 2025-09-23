import os
import time 

# ANSI kodovi za boje
RESET = '\033[0m'
BOLD = '\033[1m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'

# Čišćenje ekrana
os.system('cls' if os.name == 'nt' else 'clear')

print(BOLD + BLUE + '=' * 75 + RESET)
print(BOLD + BLUE + '\t\tProgram za upravljanje vozilima' + RESET)
print(BOLD + BLUE + '=' * 75 + RESET)

# Prazna lista za pohranu podataka o vozilima
lista_vozila = []

# Dodavanje nekoliko primjera vozila
lista_vozila.append({
    'tip': 'Automobil',
    'proizvodjac': 'VW',
    'registracija': 'ZG1234AB',
    'godina': 2018,
    'cijena': 15000.00
})

lista_vozila.append({
    'tip': 'Kamion',
    'proizvodjac': 'Volvo',
    'registracija': 'PU5678CD',
    'godina': 2015,
    'cijena': 45000.00
})

lista_vozila.append({
    'tip': 'Motocikl',
    'proizvodjac': 'Honda',
    'registracija': 'ST9012EF',
    'godina': 2021,
    'cijena': 9500.00
})

# Ispis svih vozila u tabličnom formatu
print(BOLD + YELLOW + 'Ispis vozila:' + RESET)
print(BOLD + YELLOW + '=' * 75 + RESET)
print(BOLD + CYAN + f"{'ID':<5}\t{'Tip':<15}{'Proizvodjac':<15}{'Registracija':<15}{'Godina':^10}{'Cijena':>11}" + RESET)
print(CYAN + '-' * 75 + RESET)

# Ispis svakog vozila iz liste s ID-om
for i, vozilo in enumerate(lista_vozila, start=1): 
    # ID vozila  tj redni broj u listi koja počinje od 1  (enumerate sa start=1 , koristio sam GEMINI-a za ovo)
    print(GREEN +
        f"{i:<5}\t"   
        f"{vozilo['tip']:<15}"
        f"{vozilo['proizvodjac']:<15}"
        f"{vozilo['registracija']:<15}"
        f"{vozilo['godina']:^10}"
        f"{vozilo['cijena']:>10.2f} €"
    )
print(RESET) # vraćanje na zadanu boju (defaultnu) nakon for petlje.

print(CYAN + '-' * 75 + RESET)
print()
print(BOLD + BLUE + '=' * 75 + RESET)

while True:
    choice = input('Želite li unijeti novo vozilo? (da/ne): ').lower()
    if choice == 'da':
        # Unos novog vozila
        tip = input(f'{RESET}Unesite tip vozila: {GREEN}')
        proizvodjac = input(f'{RESET}Unesite proizvodjaca: {GREEN}')
        registracija = input(f'{RESET}Unesite registraciju: {GREEN}')
        godina = int(input(f'{RESET}Unesite godinu proizvodnje: {GREEN}'))
        cijena = float(input(f'{RESET}Unesite cijenu: {GREEN}'))

        # Kreiranje rječnika za novo vozilo
        novo_vozilo = {
            'tip': tip,
            'proizvodjac': proizvodjac,
            'registracija': registracija,
            'godina': godina,
            'cijena': cijena
        }
        
        # Dodavanje novog vozila u listu
        lista_vozila.append(novo_vozilo)
        print(BOLD + GREEN + 'Novo vozilo je uspješno dodano!' + RESET)
        
    else:
        print(RED + '\nHvala na korištenju programa za upravljanje vozilima!' + RESET)
        print(RED + '-' * 75 + RESET)
        break


# Prikaz jednostavnog progress bara
print(YELLOW + 'Učitavanje liste...' + RESET)

# Faze "progress bara"
# print(RED + '[#.....]' + RESET, end='\r')
# time.sleep(0.1)
# print(RED + '[##....]' + RESET, end='\r')
# time.sleep(0.1)
# print(RED + '[###...]' + RESET, end='\r')
# time.sleep(0.1)
# print(RED + '[####..]' + RESET, end='\r')
# time.sleep(0.1)
# print(RED + '[#####.]' + RESET, end='\r')
# time.sleep(0.1)
# print(RED + '[######]' + RESET) # U posljednjem ispisu nema \r
# time.sleep(1.5)

for i in range(1, 10): # Brojevi od 0 do 9 (ukupno 10 znakova)
    progress = '#' * i + '.' * (9 - i)
    print(RED + f'[{progress}]' + RESET, end='\r')
    time.sleep(0.2)

print('\n') # Prijelaz u novi red nakon završetka
time.sleep(0.5)


print(GREEN + 'Završeno!' + RESET)

# Čišćenje ekrana prije ispisa ažurirane liste
os.system('cls' if os.name == 'nt' else 'clear')
print(GREEN + 'Slijedi ažurirana lista vozila:' + RESET)
input(YELLOW + 'Pritisnite Enter za nastavak...' + RESET)
print(BOLD + BLUE + '=' * 75 + RESET)
print(BOLD + BLUE + '\t\tProgram za upravljanje vozilima' + RESET)
print(BOLD + BLUE + '=' * 75 + RESET)
print(BOLD + YELLOW + 'Ažurirana lista vozila:' + RESET)
print(BOLD + YELLOW + '=' * 75 + RESET)

# Ispis ažurirane liste vozila
print(BOLD + CYAN + f"{'ID':<5}\t{'Tip':<15}{'Proizvodjac':<15}{'Registracija':<15}{'Godina':^10}{'Cijena':>11}" + RESET)
print(CYAN + '-' * 75 + RESET)
for i, vozilo in enumerate(lista_vozila, start=1):
    print(GREEN +
        f"{i:<5}\t"
        f"{vozilo['tip']:<15}"
        f"{vozilo['proizvodjac']:<15}"
        f"{vozilo['registracija']:<15}"
        f"{vozilo['godina']:^10}"
        f"{vozilo['cijena']:>10.2f} €"
    )

print(RESET) # vraćanje na zadanu boju (defaultnu) nakon for petlje.

print(CYAN + '-' * 75 + RESET)

print()
print(BOLD + BLUE + '=' * 75 + RESET)