user_is_authenticated = False
while not user_is_authenticated:
    login = input("Podaj login: ")
    password = input("Podaj haslo: ")
    if login == 'Admin' and password == '1234':
        user_is_authenticated = True
print("Authenticated")
