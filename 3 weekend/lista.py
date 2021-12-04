
lista=[1,2,3,4,5]

#lista.append(True) 
lista.append('element') # dodaje element 
lista.index('element') # ktory inedex w lista ma element
lista.insert(2,"wstawiony element") # pod ktory index jaki element ma wstawic
lista[2]   # ktory elenet z listy 
lista[1:3] # elementy od do 
lista[0:-1:2] # elementy od indexu 0 do indexu - 1 ostatni od konca przeskakujac o  2 elemnty 
lista[::-1] # lista od konca 

lista_liczb =[13,9,27,14,15]
max(lista_liczb) # najwiekszy element
min(lista_liczb) # najmnieszy element
sum(lista_liczb) # suma wszystkich elementow
lista_liczb.sort() # sortuje (tablice) liste
lista_str=['c','b','d','a']
del lista_str[0] # usuwa element z listy

'''
for i in lista_str: # petla iteruje sie przez karzdy element z listy 
    print(i)
'''

for i in range(len(lista_str)):  # len(lista) zwraca liczbe elementow (int) petla wykonuje sie przez int razy w kazdej iteracji pokazuje po 1 elemencie z listy
    print(lista_str[i])


