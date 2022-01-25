

def kon(napis):
    tab_samogloski=["a",'e',"i","o",'u','y',"ą","ę","ó","A","E","I","O","U","Y","Ą","Ę","Ó"]
    for i in napis:
        if i.islower():
            if i in tab_samogloski:
                wynik = napis.replace(i,i.upper())
                napis=wynik
            else:
                pass
        if i.isupper():
            if i not in tab_samogloski:
                wynik=napis.replace(i,i.lower())
                napis=wynik
            else:
                pass
    return napis

