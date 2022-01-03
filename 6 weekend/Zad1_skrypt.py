def is_numeric(arg):
    if isinstance(arg,(int,float)) == False:
        raise ValueError("All arguments must be numeric !")
    return isinstance(arg,(int,float))

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Can not divide by zero!')

    return x / y
