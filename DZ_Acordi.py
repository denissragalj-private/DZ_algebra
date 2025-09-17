"""
Generator Akorda
================
Aplikacija za generiranje durskih i molskih akorda na osnovu unešenog početnog tona.

Korisnik unosi početni ton akorda, a aplikacija vraća tri tona od kojih se sastoje
durski i molski akord na osnovu njemačke notacije.

Oktava: C, C#, D, D#, E, F, F#, G, G#, A, A#, H (0-11)
- Durski akord: osnovni ton + 4 polutona + 7 polutona (0, 4, 7)
- Molski akord: osnovni ton + 3 polutona + 7 polutona (0, 3, 7)
"""

import os

def main():
    """Glavna funkcija aplikacije."""
    tonovi = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]
    
    def ocisti_terminal():
        """Očisti terminal ovisno o operativnom sustavu."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def generiraj_akord(pocetni_ton, tonovi):
        """
        Generiraj durski i molski akord za zadati početni ton.
        
        Args:
            pocetni_ton (str): Početni ton akorda
            tonovi (list): Lista svih tonova u oktavi
            
        Returns:
            tuple: (dur_akord, mol_akord) kao liste tonova
        """
        indeks = tonovi.index(pocetni_ton)
        
        # Durski akord: osnovni + 4 polutona + 7 polutona
        dur_akord = [
            tonovi[indeks],
            tonovi[(indeks + 4) % 12],
            tonovi[(indeks + 7) % 12]
        ]
        
        # Molski akord: osnovni + 3 polutona + 7 polutona  
        mol_akord = [
            tonovi[indeks],
            tonovi[(indeks + 3) % 12],
            tonovi[(indeks + 7) % 12]
        ]
        
        return dur_akord, mol_akord
    
    def prikazi_tonove(tonovi):
        """Prikaži dostupne tonove korisniku."""
        print('\nMogući tonovi su:')
        print()
        for ton in tonovi:
            print(ton, end="  ")
        print("\n")
    
    # Glavna petlja aplikacije
    while True:
        ocisti_terminal()
        prikazi_tonove(tonovi)
        
        pocetni_ton = input("Unesi početni ton za akord (primjer: C, D#, G, ...): ").strip()
        print()
        
        if pocetni_ton not in tonovi:
            print("Unio si nepoznat ton! Pokušaj ponovno i unesi ton točno kako piše gore.\n")
        else:
            print(f'Unio si ton: {pocetni_ton}\n')
            
            # Generiraj akorde
            dur_akord, mol_akord = generiraj_akord(pocetni_ton, tonovi)
            
            # Prikaži rezultate
            print("Rezultat:\n")
            print(f'   DUR akord ({pocetni_ton} dur): {", ".join(dur_akord)}')
            print(f'   MOL akord ({pocetni_ton} mol): {", ".join(mol_akord)}')
            print()
        
        # Pitaj korisnika želi li nastaviti
        izbor = input("Želiš li još jedan generator akorda? (upiši da / ne): ").strip().lower()
        
        if izbor != "da":
            print("\nHvala na korištenju generatora akorda! Do viđenja :)\n")
            break

if __name__ == "__main__":
    main()