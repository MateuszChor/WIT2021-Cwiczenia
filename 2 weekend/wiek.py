wiek=int(input("Podaj swój wiek "))


if wiek >=18:
    print("jesteś pelno letni")
else:
    print("nie jesteś pelno letni")

if wiek >=21:
    print("Mozesz prowadzic samochod oraz glosowac w wyborach")
elif wiek > 17 & wiek < 21:
    print("Mozesz prowadzic samochod")
else:
    print("Nie mozesz glosowac ani prowadzic samochodu")

