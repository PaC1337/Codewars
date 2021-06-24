def goodVsEvil(good, evil):
    goodtab = list(good.split(" "))
    goodtab.append(0)
    eviltab = list(evil.split(" "))
    goodvalues = [1,2,3,3,4,10,0]
    evilvalues = [1,2,2,2,3,5,10]
    goodscore = 0
    evilscore = 0
    for i in range(0,7):
        goodscore += int(goodtab[i])*goodvalues[i]
        evilscore += int(eviltab[i])*evilvalues[i]
    if(goodscore > evilscore):
        return "Battle Result: Good triumphs over Evil"
    elif(evilscore > goodscore):
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"