def count_chars(word):
    dictionary={}
    counter=1
    for i in word:
        if i not in dictionary.keys():
            dictionary[i]=[counter]
        elif i in dictionary.keys():
            counter=counter+1
            dictionary[i]=[counter]
        
    return print(dictionary)
        
            
count_chars("Przykład")