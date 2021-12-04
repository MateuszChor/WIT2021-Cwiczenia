dane_logowania = {'Admin':'1234','User1':'12345'}

dane_logowania['Admin'] # pokazuje wartosc klucza (admin)

dane_logowania.get('Admin')

## dane_logowania['User2'] nie znajduje dangeo klucza KeyError
## dane_logowania.get('User2') nie znalazl klucza user2 zwraca wartosc None

# help(dict.get)

dane_logowania.get('User2',-1) ## jak nie ma danego klucza ani wartosci dodaje klucz i wartosc 
dane_logowania.get("User2",'wartosc') ## jak jest zamienia wartosc klucza 

dane_logowania['User2']='przykladowe_haslo' # zamienia wartosc klucza user2

dane_logowania.keys()  #zwraca liste kluczy w slowniku 
dane_logowania.values() # zwraca liste wartosci w slowniku
dane_logowania.items() # zwraca liste elementow skladajacych sie z klucza i wartosci (elemty w postaci krotki)

'''
for item in dane_logowania.items(): 
    print(item)   # zwraca w kazdej iterracji element skladajacy sie z klucza i wartosci w postaci krotki 

'''
'''
for key,value in dane_logowania.items():
    print(key,value)   # zwraca w karzedj iteracji element odziellnie sam klucz i sama wartosc 
'''


# dane_logowania.pop('User2') # wyciaga wartosc pod kluczem user2 wraz z kluczem ze slownika

'''
if dane_logowania.get("User1"):
    print("znaleziono uzytkownika")
'''

dane_uzytkownikow = {"User1":{'name':'gall','surname':'Anonim'}}
print(dane_uzytkownikow.get('User1').get('name'))
print(dane_uzytkownikow['User1']["surname"])



