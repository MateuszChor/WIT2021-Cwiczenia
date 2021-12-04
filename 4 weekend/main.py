from funkcje import print_menu,main,input_get
from auth import register,log

users = {
    # slownik ktory przechowuje informacje na temat uzytkownikow pod postancia
    # login : haslo
    

}

user_is_authenticated = False


while True:
    print_menu()
    option = input("wybierz jedna z opcji: ")
    if option == '1':
        if user_is_authenticated:
            kapital_poczatkowy,wplywy,wydatki = input_get()  # z krotki ktora zwraca funckja pakujemy wartosci pokolei do zmiennych
            print(main(kapital_poczatkowy,wplywy,wydatki))
    elif option == '2':
        break
    elif option == '3':
        login,password = register()
        users[login] = password
    elif option == '4':
        if user_is_authenticated:
            print(users)
        else:
            print("Musisz byc zalogowany ")
    elif option == '5':
        user_is_authenticated = log(users)