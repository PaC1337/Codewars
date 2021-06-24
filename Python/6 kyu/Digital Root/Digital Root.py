def digital_root(n):
    x = sum(int(i) for i in str(n))
    if x < 10:
        return x
    else:
        return digital_root(x)