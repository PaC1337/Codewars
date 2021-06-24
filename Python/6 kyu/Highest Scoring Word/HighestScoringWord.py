def high(x):
    import string
    wynik = []
    mx = 0
    char = string.ascii_lowercase
    x = x.split()
    for n in range(0,len(x)):
        wynik.append(0)
        for i in range(0,len(str(x[n]))):
            for y in range(0,26):
                if(x[n][i] == char[y]):
                    wynik[n] += y + 1
    print(wynik)
    for d in range(0, len(wynik)):
        if(wynik[mx] < wynik[d]):
            mx = d
    return x[mx]
