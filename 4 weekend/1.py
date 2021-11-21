def convert_string_to_number(x):
    if type(x) == int:
        print("to już jest liczba")
    elif type(x) != int:
        x=int(x)
        print(type(x),x)
    

convert_string_to_number('5')