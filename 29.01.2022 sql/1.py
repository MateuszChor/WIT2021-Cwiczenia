from re import X
import sqlite3
import app

class User:
    def __init__(self,login,password,user_type):
        self.login=login
        self.password=password
        self.user_type=user_type


class Meal:
    def __init__(self,name,quantity,price):
        self.name=name
        self.quantity=quantity
        self.price=price



user_is_authenticated = False
while True:
    if user_is_authenticated:
        if user_type=="client":
            more='1'
            zamowienie={}
            total_price=0
            while more=='1':
                try:
                    print("__________MENU___________ ")
                    print(app.Show_DB('meals'))
                    print("------------------------")
                    food=input("co chce zjesc ")
                    quantity=input("ile :")
                    quantity=int(quantity)
                    price,is_good=app.order(quantity,food)
                    total_price=price+total_price
                    if is_good:
                        zamowienie[food]=quantity
                    print(f"Twoje zamówienie to \n {zamowienie}")
                    print(f"Do zapłaty {total_price}")
                    print("Czy chcesz zamoówić coś jeszcze ?")
                    more=input("1 tak 2 nie :")
                except ValueError:
                    print("ilosc musi byc liczba calkowita ")   
            #na koniec operacji
            print("Dziękujemy za wybor naszego sklepu zamowienie złożone do realizacji !")
            print(f"Do zapłaty {total_price}")
            user_is_authenticated = False
        elif user_type=="admin":
            while True:
                print("___ADMIN MEMU____")
                print("Co chcesz zrobić ? ")
                x=input(" 1 Dodaj posiłek do bazy danych \n 2 Usun posiłek z bazy danych \n 3 Dodaj użytkownika \n 4 Usun uzytkownika \n 5 dodaj admina \n 6 Podgląd db users \n 7 Podglad db meals \n 8 exit \n : ")
                if x=="1": # dodaje posilek do db
                    app.Add_meal()
                elif x=="2":  # usun posielek z meals 
                    meal=input("Jaki posilek chcesz usunac z bazy :")
                    app.Del_meal_from_db(meal)
                    print(f"usunięto {meal} ")
                elif x=="3":  # dodaj uzytkonika
                    print("dodaje użytkownika do bazy danych ")
                    print("____________________________________")
                    app.register()
                elif x=="4": #usuwa uzytkownika z bazy danych
                    user=input("Podaj uzytkownika ktorzego chesz usunac :")
                    app.Del_user_from_db(user)
                    print("Usunieto ")
                elif x=="5": # dodaje admina do db
                    app.register_admin()
                    print("dodano admina ") 
                elif x=="6": # pokazuje db users 
                    print(app.Show_DB('users'))
                elif x=="7": # pokazuje db meals
                    print(app.Show_DB('meals'))
                elif x =="8": # wyjscie
                    break

            #na koniec operacji
            user_is_authenticated = False
    else:
        print("_________________________________________________________________________")
        case=input("1 Logowanie , 2 Rejestracja ,Co kolwiek by wyjsc :")
        if case=='1':
            log,user_type=app.login()
            if log:
                user_is_authenticated=True
                print("autentifiaciton")
                print(f"dla  {user_type}")
        elif case=='2':
            app.register()

        else:
            break 

        # zarejestruj / zaloguj. Po pomyslnym zalogowaniu, zmodyfikuj wartość zmiennej `user_is_authenticated`
        