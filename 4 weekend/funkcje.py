

def input_get():
    kapital_poczatkowy = int(input('Podaj kapital poczatkowy'))
    wplywy = int(input('Podaj wpływy miesieczne: '))
    wydatki = int(input("Podaj miesieczne wydatki"))
    return kapital_poczatkowy,wplywy,wydatki # zwraca to w postaci krotki tupli  

def main(kapital_poczatkowy,wplywy,wydatki):
    return kapital_poczatkowy + 12 * (wplywy-wydatki)

def print_menu():
    print("1 oblicz kapitał na koniec roku")
    print("2 wyjdz z programu ") 
    print("3 zarejestruj uzytkownika ") 
    print("4 wyswietl uzytkownikow  ") 
    print("5 zaloguj")
