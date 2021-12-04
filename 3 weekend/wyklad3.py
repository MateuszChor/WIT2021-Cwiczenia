'''
lista=[]
tupla=()  # nie modowalna
slownik={}

lista.sort()
sorted(lista)

del lista[0]
lista.index
lista.append
lista[0]=1
sum(lista)
min(lista)
max(lista)

slownik.get()
slownik.keys()
slownik.items()

for liczba in lista:
    print(liczba+1)

for i in range(len(lista)):
    print(lista[i])

for key,value in slownik.items():
    print(key,value)

for key,value in slownik.items():
    if value =='dwa':
        print(key)
'''

'''
lista_liczb = []

for i in range(5):
    liczba=int(input("Podaj liczba: "))
    lista_liczb.append(liczba)

print(lista_liczb)
'''


'''
users = {
    'Admin':'1234'
}

user_is_authenticated = False 
while not user_is_authenticated:
    login = input('Podaj login: ')
    password = input("Podaj haslo: ")
    if users.get(login):
        if users[login] == password:
            user_is_authenticated = True

'''

historia_operacji = []
users = {}

while True:
    print('1 Stworz uzytkownika')
    print("2 zobacz uzytkownikow")
    print("3 wyjdz z pogramu: ")
    print("4 pokarz logi ")
    option = input("wprowadz opcje ")
    if option == "1":
        login =input("podaj login: ")
        password = input("podaj haslo: ")
        users[login] = password
        historia_operacji.append('new user creaded.')
    elif option =='2':
        for login,password in users.items():
            print(login,password)
            historia_operacji.append("Users were retrived ")
    elif option == '3':
        break
    elif option =='4':
        for log in historia_operacji:
            print(log)