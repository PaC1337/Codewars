def triple_double(num1, num2):
    one = str(num1)
    two = str(num2)
    onebool = False
    twobool = False
    for i in range(0, len(one)):
        if(one[i]*3 == one[i:i+3]):
            onebool = True
            for n in range(0, len(two)):
                if(one[i]*2 == two[n:n+2]):
                    twobool = True

    if(bool(onebool & twobool) == True):
        return 1
    else:
        return 0