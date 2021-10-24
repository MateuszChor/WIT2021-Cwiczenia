kapital_poczatkowy=int(input("Podaj kapital poczatkowy :"))
wplywy_miesieczne=int(input("Podaj wplywy :"))
okres_inwestowania=int(input("Podaj okres inwestowania w miesiacach :"))
koncowa_wartosc=int(input("Jaka jest twoja pozdana koncowa wartosc :"))


wynik = (kapital_poczatkowy+(wplywy_miesieczne*okres_inwestowania))



for x in range(okres_inwestowania):
    miesiac=wplywy_miesieczne * 1.02
    kapital_poczatkowy=kapital_poczatkowy+miesiac
    print(miesiac)
    print(kapital_poczatkowy)



if kapital_poczatkowy>koncowa_wartosc:
    print("Twoj kapital bedzie wiekszy niz zakladales")
elif kapital_poczatkowy<koncowa_wartosc:
    print("Twoj kapital bedzie mniejszy niz zakladales")   
elif kapital_poczatkowy==koncowa_wartosc:
    print("Twoj kapital bedzie dokladnie taki jak zakladales") 
    
