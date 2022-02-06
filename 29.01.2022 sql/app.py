import sqlite3
import pandas as pd 

class UserDTO:
    def __init__(self,db_name):
        self.connection=sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def commit_and_close_connection(self):
        self.connection.commit()
        self.connection.close()

def connect_with_base():
    connection = sqlite3.connect('foodapp.db')
    cursor=connection.cursor()
    return connection,cursor

def register_admin():
    connection,cursor=connect_with_base()
    username=input("Podaj login admina:")
    password=input("Podaj haslo admina:")
    cursor.execute('CREATE TABLE IF NOT EXISTS users(login,password,user_type)')
    cursor.execute('INSERT INTO users VALUES (?,?,?)',(username,password,"admin"))
    connection.commit()
    connection.close() 
    print(f"Dodano {username} admina !")

def check(params,typeB,column):
    connection,cursor=connect_with_base()
    queryset=cursor.execute(f'SELECT * FROM {typeB} WHERE {column}= (?)',(params,))   
    try: 
        user = queryset.fetchall()[0] 
        if login in user:
            return False
    except IndexError:
        return True

def Add_meal():
    connection,cursor=connect_with_base()
    name=input("jaki posilek chcesz dodac do bazy :")
    chec=check(name,"meals","name")
    if chec:
        quantity=input(f"ile mamy sztuk produktu {name} : ")
        price=input(f"Jaka cena za 1 sztk produktu {name} :")
        cursor.execute('CREATE TABLE IF NOT EXISTS meals (name,quantity,price)')
        cursor.execute('INSERT INTO meals VALUES (?,?,?)',(name,quantity,price))
        connection.commit()
        connection.close()
        print(f"Dodano posilek {name} !")
    else:
        print("taki posielek juz jest w liscie ")
        pass

def register():
    username = input("Podaj nazwe użytkownika: ")
    password = input("Podaj haslo uzytkownika: ")
    user_dto = UserDTO('foodapp.db')
    chec=check(username,"users","login")
    if chec:
        user_dto.cursor.execute(f'CREATE TABLE IF NOT EXISTS users (username,password,user_type)')
        user_dto.cursor.execute(f'INSERT INTO users  VALUES (?,?,?)',(username,password,'client'))
        #TOdo zabezpieczenie przed istenijacym loginem
        user_dto.commit_and_close_connection()
    else:
        print("taki uzytkownik juz isnieje !")

def Del_user_from_db(username):
    connection,cursor=connect_with_base()
    cursor.execute('DELETE FROM users WHERE login= (?)',(username,))
    connection.commit()
    connection.close()

def Del_meal_from_db(name):
    connection,cursor=connect_with_base()
    cursor.execute('DELETE FROM meals WHERE name= (?)',(name,))
    connection.commit()
    connection.close()

def Show_DB(type):
    connection,cursos=connect_with_base()
    data= pd.read_sql_query(f'Select * from {type};',connection)
    return data

def order(quantity,food):
    price_in_total=0
    is_good=True
    try:
        connection,cursos=connect_with_base()
        chose=cursos.execute('SELECT * FROM meals WHERE name= (?)',(food,))
        our_chose=chose.fetchall()[0]
        food_from_base=our_chose[0]
        quantity_in_base=our_chose[1]
        price_in_base=our_chose[2]
        price_in_base=int(price_in_base)
        quantity_in_base=int(quantity_in_base)
        quantity_in_base=quantity_in_base-quantity
        if quantity_in_base<1:
            is_good=False
            raise Exception
        price_in_total=price_in_base*quantity 
        cursos.execute(f'UPDATE meals SET quantity = {quantity_in_base} WHERE name=(?)',(food,))
        connection.commit()
        connection.close()
    except IndexError:
        print("brak takiego dania w menu ")
        is_good=False
    except Exception:
        print(f"Brak {food} w sklepie !!!!!!")

    return price_in_total,is_good

def login():
    try:    
        username= input('Podaj nazwe uzytkownika: ')
        password= input("Podaj haslo uzytkownika: ")
        user_dto = UserDTO('foodapp.db')
        queryset=user_dto.cursor.execute('SELECT * FROM users WHERE login= (?)',(username,))
        #TODO #user_type=user_dto.cursor.execute('SELECT * FROM users WHERE user_type = ?',(user_typee,))
        user = queryset.fetchall()[0] 
        login=user[0]
        passwrd=user[1]
        type_of_user=user[2]
        
        if login == username:
            if passwrd == password:
                print("zalogowano")
                return True,type_of_user
            if passwrd != password:
                print("złe haslo ")

        return False,False
    except IndexError:
        print("nie ma uzytkownika o takim loginie !")
        return False,False
    
    except TypeError:
        print("złe haslo !")
        return False,False
    
    