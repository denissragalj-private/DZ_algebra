''' Napiši program koji provjerava je li uneseni niz znakova palindrom.
    Palindrom je niz znakova koji se isto čita s lijeva na desno i s desna na lijevo.
    Primjer palindroma su riječi: ana, aga, ada, ala, bob, civic, radar, rotor, level, madam, racecar
    Primjer palindromskih rečenica    
    (ignoriraj razmake, interpunkcijske znakove i velika/mala slova):
    - Ana voli Milovana

# Unos od korisnika
palindrom = input("Unesi riječ: ")

# Pretvori u mala slova
palindrom = ...  # Dodaj .lower()

# Obrni riječ
obrnuto = palindrom[ ... ]  # Koristi slice da okreneš

# Provjeri s IF
if ... == ...:
    print("Da, ovo je palindrom.")
else:
    print("Ne, ovo nije palindrom.")

'''
import os

# Čišćenje ekrana
os.system('cls' if os.name == 'nt' else 'clear')

print('='*70)
print('Program koji provjerava je li uneseni niz znakova palindrom.')
print('Palindrom je niz znakova koji se isto čita s lijeva na desno i s desna na lijevo.')
print('Primjeri palindroma su riječi: ana, aga, ada, ala, bob, civic, radar, rotor, level, madam, racecar')
print('primjer rečenice:')
print('- Ana voli Milovana')
print('(ignoriraj razmake, interpunkcijske znakove i velika/mala slova):')
print('='*70)

# WHILE petlja za ponovno pokretanje (opcionalno)
while True:
    # Unos od korisnika
    palindrom = input("Unesi riječ ili rečenicu (ili 'exit' za izlaz): ")
    
    if palindrom.lower() == 'exit':
        break
    
    # Pretvori u mala slova i makni razmake
    palindrom = palindrom.lower().strip().replace(" ", "")
    
    # Obrni riječ
    obrnuto = palindrom[::-1]  # Koristimo slice da okrenemo
    
    # Provjeri s IF
    if palindrom == obrnuto:
        print("Da, ovo je palindrom.")
    else:
        print("Ne, ovo nije palindrom.")
    
    print('='*70)

print('Izlaz iz programa, hvala na korištenju!')
