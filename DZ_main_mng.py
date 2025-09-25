import os
import getpass

#region INIT

company = {
    'id': 1,
    'name': 'Pajdo und Jaranen GmbH',
    'tax_id': '01234567891',
    'vehicles': [
        {
            'id': 1,
            'type': 'Kamion',
            'manufacturer': 'MAN',
            'licence_plate': 'ZP1998MAN',
            'year_of_licence': 1919,
            'price': 300_000.00,
            'is_operational': True
        },
        {
            'id': 2,
            'type': 'Kamion',
            'manufacturer': 'MAN',
            'licence_plate': 'ZP1999MAN',
            'year_of_licence': 1919,
            'price': 300_000.00,
            'is_operational': False
        },
        {
            'id': 3,
            'type': 'Kamion',
            'manufacturer': 'MAN',
            'licence_plate': 'ZP2000MAN',
            'year_of_licence': 1919,
            'price': 300_000.00,
            'is_operational': True
        }
    ],
    'employees': [
        {
            'id': 1,
            'first_name': 'Pero',
            'last_name': 'Peric'
        },
        {
            'id': 2,
            'first_name': 'Ivo',
            'last_name': 'Ivic'
        }
    ]
}

#endregion

def ocisti_terminal():
    # Očisti terminal (Windows: 'cls', ostalo: 'clear')
    os.system('cls' if os.name == 'nt' else 'clear  ')

def login_user():
    print('Prijava korisnika')
    print()
    # DZ - simulirati prijavu korisnika u sustav HINT: nekako, negdje cuvati password svakog korisnika
    username = input('Upisite korisnicko ime: ')
    if username.strip() == '':
       pass
    elif username.lower() == 'admin':
        print('Dobrodosli admin korisnice!')
        password = input('Upisite lozinku: ')
        if password != 'admin123':
            print('Pogresna lozinka! Prijava kao guest korisnik')
            username = 'guest'
    else:
        if username not in [emp['first_name'].lower() for emp in company['employees']]:
            print('Korisnik ne postoji! Prijava kao guest korisnik')
            username = 'guest'
        else:
            print(f'Dobrodosli {username}!')  
            password = input('Upisite lozinku: ')
            # Ovdje bi se mogla dodati provjera lozinke ako bi se lozinke spremale
            # Za sada samo prihvatimo bilo koju lozinku 
            print('Uspjesno ste prijavljeni!')
            

    password = input('Upisite lozinku: ')
    print(f'Pozdrav {username}, dobro dosli u sustav!')
    input('Za nastavak ptritsnite tipku ENTER')
    ocisti_terminal()
    return username


# glavni dio programa

ocisti_terminal()

login_user()

while True:
    # DZ - simulirati prijavu korisnika u sustav HINT: nekako, negdje cuvati password svakog korisnika
    # DZ - promijeniti podatke o vozilu tako da umjesto is_operational imate used_by i povezati s korisnikom
    #       HINT: Osmislite prikaz punog imena korisnika -> full_name
    #login_user()
    ocisti_terminal()
    # MAIN MENU
    print()
    print('\tPy Fleet Management')
    print()
    print(f'Firma: {company['name']}')
    if login_user() == 'guest':
        print('Niste prijavljeni u sustav. Prijavite se da bi koristili sve funkcionalnosti.')
        # onemoguci unos novih vozila i djelatnika  
        company['vehicles'] = []
        company['employees'] = []
        pass
    elif username.lower() == 'admin':
        print('Prijavljeni ste kao admin korisnik. Imate sve ovlasti u sustavu.')
    elif username in [emp['first_name'].lower() for emp in company['employees']]:
        print(f'Prijavljeni ste kao {username}. Imate ogranicene ovlasti u sustavu.') 
    else:
        print('Niste prijavljeni u sustav. Prijavite se da bi koristili sve funkcionalnosti.')
        # onemoguci unos novih vozila i djelatnika  
        company['vehicles'] = []
        company['employees'] = []
        pass
    print()

    print(f'Korisnik: {company["employees"][0]["last_name"]}, {company["employees"][0]["first_name"]}')
    print()
    print('1. Ispis svih vozila')
    print('2. Unos novog vozila')
    # DZ
    print('3. Ispis svih djelatnika')
    print('4. Unos novog djelatnika')

    print('0. Izlaz')
    print()

    menu_item = int(input('Izberite jednu opciju iz izbornika: '))

    if menu_item == 0:
        break
    elif menu_item == 1:
        #region DISPLAY ALL VEHICLES
        print(f"|{'ID':<4}|", end='')
        print(f"{'Tip':<15}|", end='')
        print(f"{'Proizvodac':<25}|", end='')
        print(f"{'Reg. oznaka':<20}|", end='')
        print(f"{'Godina reg.':<20}|", end='')
        print(f"{'U primjeni':<12}|", end='')
        print(f"{'Cijena (EUR)':>22}|")
        print('-'*126)

        for vehicle in company['vehicles']:
            print(f"|{vehicle['id']:<4}|", end='')
            print(f"{vehicle['type']:<15}|", end='')
            print(f"{vehicle['manufacturer']:<25}|", end='')
            print(f"{vehicle['licence_plate']:<20}|", end='')
            print(f"{vehicle['year_of_licence']:<20}|", end='')
            if vehicle['is_operational']:
                print(f"{'Da':<12}|", end='')
            else:
                print(f"{'Ne':<12}|", end='')
            print(f"{vehicle['price']:>20.3f} €|")
        
        print('-'*126)
        print()
        # Privremeno zaustavi izvrsavanje programa dok god korisnike ne pritisne tipku ENTER
        # Moze biti proivoljno vrijeme cekanja, dok time.spleep(sec=) zahtijeva fiksni broj sekundi
        input('Za nastavak ptritsnite tipku ENTER')
        #endregion
    elif menu_item == 2:
        #region ADD NEW VEHICLE
        while True:
            #region OPIS
            # vehicles = company['vehicles']
            # next_vehicle_id = len(vehicles) + 1
            # next_vehicle_id = len(company['vehicles']) + 1
            
            # company['vehicles'][1]['id'] opis:
            # iz rjecnika company pod kljucem 'vehicles' dohvati mi tu vrijednost -> lista
            # iz tako dobivene liste uzmem element pod indexom 1 -> dobit cu opet rjecnik
            # is ovog novog rjecnika dohvati vrijednost pod kljucem 'id' -> int (2)
            # next_vehicle_id = company['vehicles'][1]['id'] + 1
            # pokriva sve slucajeve jer dohvaca ZADNJI element liste
            #endregion
            vehicle = {}

            # next_vehicle_id = company['vehicles'][-1]['id'] + 1
            # vehicle['id'] = next_vehicle_id
            # ili
            vehicle['id'] = company['vehicles'][-1]['id'] + 1
            vehicle['type'] = input('Upisite tip vozila: ')
            vehicle['manufacturer'] = input('Upisite proizvodaca vozila: ')
            vehicle['licence_plate'] = input('Upisite reg. oznaku vozila: ')
            vehicle['year_of_licence'] = input('Upisite godinu 1. registracije vozila: ')
            vehicle['price'] = float(input('Upisite cijenu vozila u EUR: '))
            # vehicle['is_operational'] = input('Upisite moze li se vozilo koristiti? (Da/Ne): ')
            is_operational = input('Upisite moze li se vozilo koristiti? (Da/Ne): ')
            if is_operational.lower() == 'da':
                vehicle['is_operational'] = True
            else:
                vehicle['is_operational'] = False

            company['vehicles'].append(vehicle)

            next_entry = input('Novi unos? (Da/Ne): ')
            if next_entry.lower() != 'da':
                break
        #endregion
    elif menu_item == 3:
        #region DISPLAY ALL EMPLOYEES
        print(f"|{'ID':<4}|", end='')
        print(f"{'Ime':<20}|", end='')    
        print(f"{'Prezime':<20}|")
        print('-'*50)

        for employee in company['employees']:
            print(f"|{employee['id']:<4}|", end='')
            print(f"{employee['first_name']:<20}|", end='')
            print(f"{employee['last_name']:<20}|")
        
        print('-'*50)
        print()
        input('Za nastavak ptritsnite tipku ENTER')
        #endregion  
    elif menu_item == 4:
        #region ADD NEW EMPLOYEE
        while True:
            employee = {}
            employee['id'] = company['employees'][-1]['id'] + 1
            employee['first_name'] = input('Upisite ime djelatnika: ')
            employee['last_name'] = input('Upisite prezime djelatnika: ')

            company['employees'].append(employee)

            next_entry = input('Novi unos? (Da/Ne): ')
            if next_entry.lower() != 'da':
                break
        #endregion

# Zavrsetak izvrsavanja programa
print()
print('Pozdrav!')
print()