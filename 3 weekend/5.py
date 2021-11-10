lista1=[1,2,3,4,5]
lista2=[1,2,3,4,5]
lista3=[1,2,2,3,3,4,5]

set1=set(lista3)
set2=set(lista1)
set3=set(lista3)



if  set1 & set3 & set2:
    wynik=set1.union(set2,set3)
    print(f"wszystkie listy zawieraja te same elementy sa to {wynik} ")

else:
    print(" jedna z list lub wszystkie listy nie zawieraja ani jednego tego samego elementu")

if len(lista1) != len(set1):
    print("lista 1 zawiera dublikaty")

else:
    print("lista1 nie zawiera duplikatow ")

if len(lista2) != len(set2):
    print("lista 2 zawiera dublikaty")

else:
    print("lista2 nie zawiera duplikatow ")    

if len(lista3) != len(set3):
    print( "lista 3 zawiera dublikaty")

else:
    print("lista3 nie zawiera duplikatow ")



