'''
zadatak:
Napisati program koji ispisuje tablicu množenja u tablici za brojeve od 1 do X ovisno o potrebi korisnika.
'''

import os
import sys
import datetime


# ANSI escape kodovi za boje i reset
RESET = "\033[0m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
BLUE = "\033[94m"
ORANGE = "\033[38;5;208m"

# Funkcija za čišćenje terminala
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def generiraj_tablicu_tekst(table_size):
    '''
    Generira tekstualnu tablicu množenja zadane veličine i ispisuje je na ekran
    '''
    # Dinamički izračunava širinu ćelije na temelju najvećeg broja u tablici.
    # Dodaje se +2 za padding (jedan razmak s lijeve i desne strane) radi boljeg poravnanja.
    cell_content_width = len(str(table_size * table_size))
    header_content_width = len(str(table_size))
    
    header_col_width = header_content_width + 2
    cell_col_width = cell_content_width + 2

    # Funkcija za ispis vodoravne linije
    def print_horizontal_line():
        # Prvi dio linije
        print(YELLOW + "|" + "-" * header_col_width + BLUE + "|", end="")
        # Drugi dio linije
        for _ in range(table_size):
            print(YELLOW + "-" * cell_col_width + "|", end="")
        print(RESET)
    
    # Ispis gornjeg okvira
    print_horizontal_line()

    # Zaglavlje stupaca
    print(YELLOW + "|" + RED + f"{'x': ^{header_col_width}}" + BLUE + "|", end="")
    for n_head in range(1, table_size + 1):
        print(CYAN + f"{n_head: ^{cell_col_width}}" + YELLOW + "|", end="")
    print(RESET)

    # Linija ispod zaglavlja
    print(YELLOW + "|" + ORANGE + "=" * header_col_width + BLUE + "|", end="")
    for _ in range(table_size):
        print(ORANGE + "=" * cell_col_width + YELLOW + "|", end="")
    print(RESET)

    # Glavni dio tablice
    for i in range(1, table_size + 1):
        if i > 1:
            print_horizontal_line()

        print(YELLOW + "|" + GREEN + f"{i: ^{header_col_width}}" + BLUE + "|", end="")

        for n in range(1, table_size + 1):
            rezultat = i * n
            print(MAGENTA + f"{rezultat: ^{cell_col_width}}" + YELLOW + "|", end="")
        print(RESET)

    # Ispis donjeg okvira
    print_horizontal_line()

   
def main():
    """Glavna funkcija koja pokreće program."""
    clear_terminal()

    # Petlja za unos veličine tablice
    while True:
        try:
            table_size = int(input(GREEN + "Unesite željenu veličinu tablice (npr. '10' za 10x10): " + RESET))
            if table_size <= 0:
                print(RED + "Veličina mora biti pozitivan broj. Molim unesite ponovo." + RESET)
            else:
                break
        except ValueError:
            print(RED + "Neispravan unos. Molim unesite cijeli broj." + RESET)

    print(GREEN + "Generiram tablicu na ekranu (s bojama)..." + RESET)
    generiraj_tablicu_tekst(table_size,)

    print("\n")

  
    
   

# --- Glavni dio programa (MAIN) ---
if __name__ == "__main__":
    main()
