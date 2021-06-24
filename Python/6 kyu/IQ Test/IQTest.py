def iq_test(numbers):
    numarr = [int(i) % 2 for i in numbers.split()]
    x = 0
    if numarr.count(1) > numarr.count(0):
        x = 0
    else:
        x = 1
    return numarr.index(x) + 1