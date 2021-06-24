def openOrSenior(data):
    result = list()
    for x in range(len(data)):
        if data[x][0] > 54 and data[x][1] > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result