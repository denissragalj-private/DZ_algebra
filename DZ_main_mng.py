import os
import getpass

#region COLORS
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ENDC = '\033[0m'
#endregion

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
            # DZ - dodati informaciju o tome tko koristi vozilo (HINT: used_by)
            'used_by': 'Ivo',  # None ako vozilo nije u upotrebi
            #'is_operational': True
        },
        {
            'id': 2,
            'type': 'Kamion',
            'manufacturer': 'MAN',
            'licence_plate': 'ZP1999MAN',
            'year_of_licence': 1919,
            'price': 300_000.00,
            # DZ - dodati informaciju o tome tko koristi vozilo (HINT: used_by)
            'used_by': None,  # None ako vozilo nije u upotrebi
            #'is_operational': None

        },
        {
            'id': 3,
            'type': 'Kamion',
            'manufacturer': 'MAN',
            'licence_plate': 'ZP2000MAN',
            'year_of_licence': 1919,
            'price': 300_000.00,
            # DZ - dodati informaciju o tome tko koristi vozilo (HINT: used_by)
            'used_by': 'Pero',  # None ako vozilo nije u upotrebi
            #'is_operational': True
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
        },
        {
            'id': 3,
            'first_name': 'Jaran',
            'last_name': 'Jaranic'
        }
    ],
    # Novi rjecnik za pohranu lozinki
    'logins': {
        'Pero': '123456',
        'Ivo': '123456',
        # Dodati nove korisnike programa koji nisu nužno zaposlenici, i njihove lozinke
        'Marko': '123456',
        'Ana': '123456',
        'Jure': '123456',
        'Denis': '123456'
    }
}

#endregion

def ocisti_terminal():
    # Očisti terminal (Windows: 'cls', ostalo: 'clear')
    os.system('cls' if os.name == 'nt' else 'clear  ')

def login_user():
    print('Prijava korisnika')
    print()
    # DZ - simulirati prijavu korisnika u sustav HINT: nekako, negdje cuvati password svakog korisnika
    username = input('Upišite korisnicko ime: ')
    password = getpass.getpass('Upišite lozinku: ')
    # password = input('Upišite lozinku: ')
    #provjera korisnika
    if username not in company['logins']:
        print('Korisnik ne postoji u sustavu!')
        input('Za nastavak ptritsnite tipku ENTER')
        ocisti_terminal()
        return login_user()
    if company['logins'][username] != password:
        print('Pogresna lozinka!')
        input('Za nastavak ptritsnite tipku ENTER')
        ocisti_terminal()
        return login_user()
    
    print(f'Pozdrav {username}, dobro dosli u sustav!')
    input('Za nastavak ptritsnite tipku ENTER')
    ocisti_terminal()
    return username, password 


# glavni dio programa

ocisti_terminal()

username, password = login_user()

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
    # Trebam provjeriti dali je korisnik employee
    # DZ
    is_employee = False
    for employee in company['employees']:
        if employee['first_name'] == username:
            is_employee = True
            break
    if is_employee:
        print(f'Prijavljeni ste kao {username}. Imate pune ovlasti u sustavu.')
    else:
        print(f'Prijavljeni ste kao {username}. \n Niste zaposlenik firme {company["name"]}. \n Imate ogranicene ovlasti u sustavu.')
    print()
    # Prikaz punog imena korisnika - HINT: full_name prijavljenog korisnika
    # DZ
    full_name = ''
    for employee in company['employees']:
        if employee['first_name'] == username:
            full_name = f"{employee['first_name']} {employee['last_name']}"
            break
        
    print(f'Korisnik: {full_name}')
    print()
    print(f'{BLUE}1. Ispis svih vozila{ENDC}')
    print(f'{GREEN}2. Unos novog vozila{ENDC}')
    # DZ
    print(f'{BLUE}3. Ispis svih djelatnika{ENDC}')
    print(f'{GREEN}4. Unos novog djelatnika{ENDC}')
    print(f'{GREEN}5. Unos novog korisnika sustava{ENDC}') # HINT: novi korisnik nije nužno djelatnik
    print(f'{BLUE}6. Ispis svih korisnika sustava{ENDC}') # HINT: ispisati sve korisnike iz rječnika 'logins'
    print(f'{YELLOW}7. Brisanje vozila po ID-u{ENDC}') # HINT: obrisati vozilo iz liste 'vehicles' prema unesenom ID-u
    print(f'{YELLOW}8. Brisanje djelatnika po ID-u{ENDC}') # HINT: obrisati djelatnika iz liste 'employees' prema unesenom ID-u
    print(f'{GREEN}9. Promjena korisnika vozila{ENDC}') # HINT: promijeniti vrijednost 'used_by' za odabrano vozilo
    print(f'{GREEN}10. Promjena lozinke korisnika{ENDC}') # HINT: promijeniti vrijednost 'password' za odabranog korisnika
    print(f'{GREEN}11. Odjava korisnika{ENDC}') # HINT: odjaviti korisnika i vratiti se na početak programa (prijava korisnika)
    print(f'{YELLOW}12. Brisanje korisnika sustava{ENDC}') # HINT: obrisati korisnika iz rječnika 'logins'
    print('0. Izlaz')
    print()


    menu_item = int(input('Izberite jednu opciju iz izbornika: '))
    print()
    if menu_item == 0:
        break
    elif menu_item == 1:
        #region DISPLAY ALL VEHICLES
        print(f"|{'ID':<4}|", end='')
        print(f"{'Tip':<15}|", end='')
        print(f"{'Proizvodac':<25}|", end='')
        print(f"{'Reg. oznaka':<20}|", end='')
        print(f"{'Godina reg.':<20}|", end='')
        print(f"{'Korisnik':<12}|", end='')
        print(f"{'Cijena (EUR)':>22}|")
        print('-'*126)

        for vehicle in company['vehicles']:
            print(f"|{vehicle['id']:<4}|", end='')
            print(f"{vehicle['type']:<15}|", end='')
            print(f"{vehicle['manufacturer']:<25}|", end='')
            print(f"{vehicle['licence_plate']:<20}|", end='')
            print(f"{vehicle['year_of_licence']:<20}|", end='')
            if vehicle['used_by'] is not None:
                print(f"{vehicle['used_by']:<12}|", end='')
            else:
                print(f"{'Nema korisnika':<12}|", end='')
            print(f"{vehicle['price']:>20.3f} €|")
        
        print('-'*126)
        print()
        # Privremeno zaustavi izvrsavanje programa dok god korisnike ne pritisne tipku ENTER
        # Moze biti proivoljno vrijeme cekanja, dok time.spleep(sec=) zahtijeva fiksni broj sekundi
        input('Za nastavak ptritsnite tipku ENTER')
        #endregion
    elif menu_item == 2:
        #region ADD NEW VEHICLE
        if username not in company['logins']:
            print('Samo zaposlenici firme mogu unositi nova vozila u sustav!')
            input('Za nastavak ptritsnite tipku ENTER')
            continue
        else:
            ocisti_terminal()
           
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
                # is_operational = input('Upisite moze li se vozilo koristiti? (Da/Ne): ')
                # if is_operational.lower() == 'da':
                #     vehicle['is_operational'] = True
                # else:
                #     vehicle['is_operational'] = False
                vehicle['used_by'] = input('Upisite ime korisnika vozila (ostaviti prazno ako vozilo nema korisnika): ')
                if vehicle['used_by'] == '':
                    vehicle['used_by'] = None # vozilo nema korisnika
            

                company['vehicles'].append(vehicle)

                next_entry = input('Novi unos? (Da/Ne): ')
                if next_entry.lower() != 'da':
                    break
            #endregion
    elif menu_item == 3:
        #region DISPLAY ALL EMPLOYEES
        print(f"|{'ID':<5}|", end='')
        print(f"{'Ime':<20}|", end='') 
        print(f"{'Prezime':<20}|", end='')
        print(f"{'Vozilo':<30}|") # Dodan novi stupac
        print('-'*80)

        for employee in company['employees']:
            assigned_vehicle = 'Nema dodijeljeno vozilo'
            for vehicle in company['vehicles']:
                if vehicle['used_by'] == employee['first_name']:
                    assigned_vehicle = f"{vehicle['type']} ({vehicle['licence_plate']})"
                    break # Prekidamo unutarnju petlju jer smo našli vozilo

            print(f"|{employee['id']:<5}|", end='')
            print(f"{employee['first_name']:<20}|", end='')
            print(f"{employee['last_name']:<20}|", end='')
            print(f"{assigned_vehicle:<30}|")
        
        print('-'*80)
        print()
        input('Za nastavak pritisnite tipku ENTER')
        #endregion
    elif menu_item == 4:
        #region ADD NEW EMPLOYEE
        if username not in company['logins']:
            print('Samo zaposlenici firme mogu unositi nova vozila u sustav!')
            input('Za nastavak ptritsnite tipku ENTER')
            continue
        else:
            while True:
                employee = {}
                employee['id'] = company['employees'][-1]['id'] + 1
                first_name = input('Upisite ime djelatnika: ')
                last_name = input('Upisite prezime djelatnika: ')
                employee['first_name'] = first_name
                employee['last_name'] = last_name
                # Unos lozinke
                password = getpass.getpass('Upisite lozinku djelatnika: ') # koristiti getpass.getpass() za skriveni unos
                employee['password'] = password

                company['employees'].append(employee)
                # Dodavanje novog korisnika i njegove lozinke u rjecnik 'logins'
                company['logins'][first_name] = password

                next_entry = input('Novi unos? (Da/Ne): ')
                if next_entry.lower() != 'da':
                    break
        #endregion
    elif menu_item == 5:
        #region ADD NEW USER
        while True:
            username = input('Upisite korisnicko ime: ')
            if username in company['logins']:
                print('Korisnicko ime vec postoji! Pokusajte ponovno.')
                continue
            password = getpass.getpass('Upisite lozinku: ')
            company['logins'][username] = password
            next_entry = input('Novi unos? (Da/Ne): ')
            if next_entry.lower() != 'da':
                break
        #endregion
    elif menu_item == 6:
        print(f"|{'Korisnicko ime':<20}|", end='')
        print(f"{'Lozinka':<20}|", end='')
        print(f"{'Zaposlenik':<12}|")
        print('-'*54)

        for user, pwd in company['logins'].items():
            is_user_employee = False
            for employee in company['employees']:
                if employee['first_name'] == user:
                    is_user_employee = True
                    break
            
            print(f"|{user:<20}|", end='')
            print(f"{pwd:<20}|", end='')
            print(f"{'Da' if is_user_employee else 'Ne':<12}|")
        
        print('-'*54)
        print()
        input('Za nastavak pritisnite tipku ENTER')
        #endregion
    elif menu_item == 7:
      #region DELETE VEHICLE
      if not is_employee:
          print('Samo zaposlenici firme mogu brisati vozila iz sustava!')
          input('Za nastavak pritisnite tipku ENTER')
          continue
      else:
          while True:
              vehicle_id_delete = input('Upišite ID vozila koje želite obrisati: ')
              if vehicle_id_delete.isdigit():
                  vehicle_id = int(vehicle_id_delete)
                  vehicle_found = False
                  for i, vehicle in enumerate(company['vehicles']):
                      if vehicle['id'] == vehicle_id:
                          vehicle_found = True
                          del company['vehicles'][i]
                          print(f'Vozilo s ID-om {vehicle_id} je obrisano.')
                          break
                  if not vehicle_found:
                      print(f'Vozilo s ID-om {vehicle_id} nije pronađeno.')
              else:
                  print('Pogrešan unos! Molimo unesite ispravan ID (broj).')
              
              next_entry = input('Brisanje drugog vozila? (Da/Ne): ')
              if next_entry.lower() != 'da':
                  break
      #endregion
    elif menu_item == 8:
        #region DELETE EMPLOYEE
        if not is_employee:
            print('Samo zaposlenici firme mogu brisati djelatnike iz sustava!')
            input('Za nastavak pritisnite tipku ENTER')
            continue
        else:
            while True:
                employee_id_delete = input('Upišite ID djelatnika koje želite obrisati: ')
                if employee_id_delete.isdigit():
                    employee_id = int(employee_id_delete) 
                    employee_found = False
                    for i, employee in enumerate(company['employees']):
                        if employee['id'] == employee_id:
                            employee_found = True
                            del company['employees'][i]
                            print(f'Djelatnik s ID-om {employee_id} je obrisan.')
                            break
                    if not employee_found:
                        print(f'Djelatnik s ID-om {employee_id} nije pronađen.')  
                else:
                    print('Pogrešan unos! Molimo unesite ispravan ID (broj).')  
                    continue
                next_entry = input('Brisanje drugog djelatnika? (Da/Ne): ')
                if next_entry.lower() != 'da':
                    break
        #endregion
    elif menu_item == 9:
        #region CHANGE VEHICLE USER
        if not is_employee:
            print('Samo zaposlenici firme mogu mijenjati korisnike vozila u sustavu!')
            input('Za nastavak pritisnite tipku ENTER')
            continue
        else:
            while True:
                vehicle_id_change = input('Upišite ID vozila kojem želite promijeniti korisnika: ')
                if vehicle_id_change.isdigit():
                    vehicle_id = int(vehicle_id_change)
                    vehicle_found = False
                    for vehicle in company['vehicles']:
                        if vehicle['id'] == vehicle_id:
                            vehicle_found = True
                            new_user = input('Upišite ime novog korisnika (ostavite prazno ako vozilo nema korisnika): ')
                            if new_user == '':
                                vehicle['used_by'] = None
                            else:
                                vehicle['used_by'] = new_user
                            print(f'Korisnik vozila s ID-om {vehicle_id} je promijenjen.')
                            break
                    if not vehicle_found:
                        print(f'Vozilo s ID-om {vehicle_id} nije pronađeno.')
                else:
                    print('Pogrešan unos! Molimo unesite ispravan ID (broj).')
                
                next_entry = input('Promjena korisnika drugog vozila? (Da/Ne): ')
                if next_entry.lower() != 'da':
                    break
        #endregion
    elif menu_item == 10:
        #region CHANGE USER PASSWORD
        while True:
            user_to_change = input('Upišite korisnicko ime kojem želite promijeniti lozinku: ')
            if user_to_change in company['logins']:
                new_password = getpass.getpass('Upišite novu lozinku: ')
                company['logins'][user_to_change] = new_password
                print(f'Lozinka za korisnika {user_to_change} je promijenjena.')
            else:
                print('Korisnik ne postoji u sustavu!')
            
            next_entry = input('Promjena lozinke drugog korisnika? (Da/Ne): ')
            if next_entry.lower() != 'da':
                break
        #endregion
    elif menu_item == 11:
        #region LOGOUT USER
        print(f'Korisnik {username} je odjavljen.')
        input('Za nastavak pritisnite tipku ENTER')
        ocisti_terminal()
        username, password = login_user()
        #endregion
    elif menu_item == 12:
        #region DELETE USER
        if not is_employee:
            print('Samo zaposlenici firme mogu brisati korisnike iz sustava!')
            input('Za nastavak pritisnite tipku ENTER')
            continue
        else:
            while True:
                user_to_delete = input('Upišite korisnicko ime kojeg želite obrisati: ')
                if user_to_delete in company['logins']:
                    del company['logins'][user_to_delete]
                    print(f'Korisnik {user_to_delete} je obrisan iz sustava.')
                else:
                    print('Korisnik ne postoji u sustavu!')
                
                next_entry = input('Brisanje drugog korisnika? (Da/Ne): ')
                if next_entry.lower() != 'da':
                    break
        #endregion  
    else:
        print('Pogresan unos! Molimo izaberite jednu od ponudenih opcija.')
        input('Za nastavak pritisnite tipku ENTER') 
        continue

# Zavrsetak izvrsavanja programa
print()
print('Pozdrav!')
print('Hvala što ste koristili naš sustav.')