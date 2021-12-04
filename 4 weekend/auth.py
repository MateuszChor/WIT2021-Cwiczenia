
def register():
    login = input("podaj login: ")
    password = input('podaj haslo: ')
    return login,password

def log(users):
    '''
    Input: users:dict - slownik z infromacjami o obecnie zarejstrowanymi uzytkownikami 

    Output: is_authenticated: bool -informacja czy dane logowania sa poporawne 

    Algorithm
    1 Przyjmuje dane logowanie i zapisuje je do zmiennych login , password
    2 Sprawdza czy w sloniku users znajduje sie klucz podany jako login
    3 jesli sie znajduje sprawdz powiazane z nim haslo i zwroc tak czy nie
    4 jezeli login sie nie znajduje zwroc falsz 
    '''
    login= input("Podaj login: ")
    password = input('Podaj hasło: ')
    if users.get(login):
        return users(login) == password
    return False
