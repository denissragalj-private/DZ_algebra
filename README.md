# Generator Akorda

## Opis
Aplikacija koja omogućuje korisniku da unese početni ton akorda za koji mu treba vratiti tri tona od kojih se sastoji durski i molski akord prema njemačkoj notaciji.



### Tonovi u oktavi
```
Indeks: 0, 1,  2, 3,  4, 5, 6,  7, 8,  9, 10, 11
Ton:    C, C#, D, D#, E, F, F#, G, G#, A, A#, H
```

### Struktura akorda
- **Durski akord**: osnovni ton + 4 polutona + 7 polutona (0, 4, 7)
- **Molski akord**: osnovni ton + 3 polutona + 7 polutona (0, 3, 7)

### Primjeri
```
D dur (D): D, F#, A
D mol (d): D, F, A

H dur (H): H, D#, F#
H mol (h): H, D, F#
```

## Korištenje
1. Aplikacija će prikazati dostupne tonove
2. Unesi početni ton akorda (npr. C, D#, G)
3. Aplikacija će prikazati durski i molski akord
4. Možeš nastaviti s novim akordima ili izaći iz aplikacije

## Značajke
- Čišćenje terminala između unosa
- Provjera unosa
- Mogućnost višestrukih generiranja

## Tehnički detalji
- Automatsko čišćenje terminala (podržava Windows i Unix/Linux/macOS)
- Provjera unosa prema dostupnim tonovima
