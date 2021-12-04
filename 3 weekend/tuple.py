krotka=(1,True,2.0,"string",[])

# krotka.append('element')  nie mozna modfikowac krotki dodawac usuwac zmieniac elementow

len(krotka)

krotka.index('string') 
# krotka.insert(2, 'Wstawiony element') nie mozna modfikowac krotki dodawac usuwac zmieniac elementow

krotka[2]
krotka[1:3]
krotka[0:-1: 2]
krotka[::-1]

krotka_liczb = (13,9,27,14,15)

max(krotka_liczb)
min(krotka_liczb)
sum(krotka_liczb)

# krotka_liczb.sort() nie mozna modfikowac krotki dodawac usuwac zmieniac elementow
print(sorted(krotka_liczb)) # ten zapis dziala poniewaz funkcja sorted nie modifikuje zmiennej tylko tworzy posortowana kopie zmiennej sama zmienna jest nie rozna 

krotka_stringow=("c","b","a","d")

# del krotka_stringow[0] # nie mozna modfikowac krotki dodawac usuwac zmieniac elementow

for i in krotka_stringow:
    print(i)

for i in range(len(krotka_stringow)):
    print(krotka_stringow[i])

