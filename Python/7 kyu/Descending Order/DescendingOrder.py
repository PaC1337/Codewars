def Descending_Order(num):
    numlist = [int(x) for x in str(num)]
    numlist.sort(reverse = True)
    s = [str(i) for i in numlist]
    res = int("".join(s))
    return res