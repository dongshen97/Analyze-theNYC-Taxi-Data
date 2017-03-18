def getpointnum(datalen):
    pointlen = datalen // 4
    returnlist = [0, pointlen, pointlen * 2, pointlen * 3, datalen]
    return returnlist
