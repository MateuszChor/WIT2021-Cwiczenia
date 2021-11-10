lista=[1,2,3,4,5]
lista_max=[]

while len(lista_max) != 2:
    lista_max.append(max(lista))
    del lista[-1]
    
print('lista max = {}'.format(lista_max))