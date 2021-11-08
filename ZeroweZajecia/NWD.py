def nwd(a, b):
    x = a % b
    if x == 0:
        return b
    else:
        return nwd(b, x)
