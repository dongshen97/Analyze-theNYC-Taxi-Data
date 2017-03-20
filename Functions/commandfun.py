def getpointnum(datalen):
    pointlen = datalen // 4
    returnlist = [0, pointlen, pointlen * 2, pointlen * 3, datalen]
    return returnlist


def addlists(ONElist, TWOlist):
    returnlist = [0]*len(ONElist)
    if len(ONElist) is not len(TWOlist):
        return returnlist
    for val in range(0, len(ONElist)):
        returnlist[val] = ONElist[val] + TWOlist[val]
    return returnlist
