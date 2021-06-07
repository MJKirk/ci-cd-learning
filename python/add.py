def myadd(x, y):
    if type(x) is str and type(y) is str:
        raise ValueError("I don't want to add two strings")
    return x + y

