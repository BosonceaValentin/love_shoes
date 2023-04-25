import datetime

def inregistrare_cumparare(adidasi, pret):
    with open('adidasi.txt', 'a') as f:
        data = datetime.date.today().strftime('%d/%m/%Y')
        f.write(f'{adidasi}, {pret} RON, {data}\n')

def afisare_istoric_cumparari():
    try:
        with open('adidasi.txt', 'r') as f:
            istoric = f.read()
        print(istoric)
    except FileNotFoundError:
        print('Nu s-a gasit istoricul de cumparari.')

def main():
    print('Introduceti datele pentru perechea de adidasi cumparata:')
    adidasi = input('Numele adidasilor: ')
    pret = input('Pretul adidasilor (in RON): ')
    inregistrare_cumparare(adidasi, pret)
    afisare_istoric_cumparari()

if __name__ == '__main__':
    main()