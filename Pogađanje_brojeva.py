'''
Igra pogađanja brojeva. od 1-100
'''
import random
import time
import os

# Čišćenje ekrana
os.system('cls' if os.name == 'nt' else 'clear')
print('='*70)
print('Igra pogađanja brojeva od 1 do 100.')
print('Računalo nasumično bira broj, a ti pogađaš koji je to broj.')
print('Nakon svakog unosa, računalo će ti reći je li tvoj broj manji ili veći od traženog broja.')
print('='*70) 

# Generiranje nasumičnog broja između 1 i 100
tajni_broj = random.randint(1, 100)

# Broj pokušaja
pokusaji = 0

# WHILE petlja za ponovno pokretanje 
while True:
    # Unos od korisnika
    unos = input("Unesi svoj broj (ili 'exit' za izlaz): ")
    
    if unos.lower() == 'exit':
        break
    
    else:
        unos = int(unos)
        pokusaji += 1 # Povećavamo broj pokušaja
        
        if unos == tajni_broj:
            print(f"Čestitamo! Pogodio si broj {tajni_broj} u {pokusaji} pokušaja.")
            print('='*70)   
        elif unos < tajni_broj:
            print("Tvoj broj je manji od traženog.")
        else:
            print("Tvoj broj je veći od traženog.")
            
# pitanje i  Pauza prije ponovnog pokretanja
    print('='*70)
    time.sleep(1)
    odgovor = input('dali želite nastaviti? (da/ne): ')
    if odgovor.lower() != 'da':
        break 

print('Izlaz iz programa, hvala na korištenju!')