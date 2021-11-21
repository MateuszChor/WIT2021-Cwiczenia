def print_dict(dict):
    for key in dict:
        get = dict.get(key)
        print(key,get)

przyklad={"a":1,"b":2}
print_dict(przyklad)