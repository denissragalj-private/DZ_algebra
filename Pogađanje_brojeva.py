import random
import os

while True:
    # Čišćenje ekrana
    os.system('cls' if os.name == 'nt' else 'clear')
    print('='*70)
    print('Igra pogađanja brojeva od 1 do 100.')
    print('Računalo nasumično bira broj, a ti pogađaš koji je to broj.')
    print('Nakon svakog unosa, računalo će ti reći je li tvoj broj manji ili \nveći od traženog broja.')
    print('='*70)

    # Generiranje nasumičnog broja između 1 i 100
    tajni_broj = random.randint(1, 100)
    pokusaji = 0
    unos_string = ''

    igra_zavrsena = False
    while not igra_zavrsena:
        # Unos od korisnika
        unos_string = input("Unesi svoj broj (ili 'exit' za izlaz): ")
        print('='*70)
        if unos_string.lower() == 'exit':
            igra_zavrsena = True
            break
        else:
             unos_int = int(unos_string)
             pokusaji += 1

        if unos_int == tajni_broj:
            print(f"Čestitamo! Pogodio si broj {tajni_broj} u {pokusaji} pokušaja.")
            print('='*70)
            igra_zavrsena = True
        elif unos_int < tajni_broj:
            print("Tvoj broj je manji od traženog.")
        else:
            print("Tvoj broj je veći od traženog.")

    # Pitanje za nastavak igre nakon što je pogađanje završeno
    if unos_string.lower() != 'exit':
        odgovor = input('Želite li igrati ponovno? (da/ne): ')
        if odgovor.lower() != 'da':
            print('Izlaz iz programa, hvala na korištenju!')
            break
    else:
        # Ako je korisnik unio 'exit' odma izlazi iz programa
        print('Izlaz iz programa, hvala na korištenju!')
        break
    