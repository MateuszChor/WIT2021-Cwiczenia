dane_logowania ={"Admin":"1234"}

not_authenticated = True

while not_authenticated:
    login = input("Podaj logi ")
    Password = input("Podaj haslo ")     
    if Password==dane_logowania.get(login):
        print("Dane poprawne")
        not_authenticated=False
    else:
        print("bład sproboj ponownie ")  





