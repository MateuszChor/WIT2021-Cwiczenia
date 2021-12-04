lista1=[1,2,2,2,3] # zbiory liczb uwzgendniaja powtarzajacych sie liczb 
lista2=[2,3,4,4,5]
set1=set(lista1)
set2=set(lista2)


set1 | set2 # laczy zbiory 
set1.union(set2) # zwraca porownunanie zbiow  np 1=(1,2,3) 2=(2,3,4) union= 12324

set1 & set2  # tylko te elementy ktore sie powtarzaja 
set1.intersection(set2) # tylko te elementy ktore sie powtarzaja

set1-set2   # elementy z zbioru 1 kotre sie nie powtarzaja w 2 zbiorze 
set2-set1  # elemty zbioru 2 ktore sie nie powtarzaja w 1 zbiorze 
len(set1) # dlugosc elementow zbioru bez duplikatow
set1.add(4) # dodaje element do zbioru
#set1.pop()
set1.remove(4) # usuwa 4 
set1.update(set2) # rozszerza zbior o elenty z zbioru 2
set2.clear() # czyscic zbior
print(set2)

4 in lista1 

