import math
import numpy as np

from scipy.stats import mode


def list_time_statistics(List, fromID, toID):
    pickup_time_statistics = [0]*24
    for value in List[fromID:toID]:
        pickup_time_statistics[value] += 1
    return pickup_time_statistics


def LongShort_path(Tlist, Dlist):
    middle = np.median(Dlist)
    BT = []
    ST = []
    for value in range(len(Tlist)):
        if Dlist[value] > middle:
            BT.append(Tlist[value])
        else:
            ST.append(Tlist[value])
    return mode(BT), mode(ST)


def LoLaDefindbyPathTime(Tlist, LoList, LaList, TIME, loFr, loTo, laFr, laTo):
    reLo = []
    reLa = []
    for value in range(len(Tlist)):
        if Tlist[value] == TIME:
            if LoList[value] < loTo and LoList[value] > loFr \
               and LaList[value] < laTo and LaList[value] > laFr:
                reLo.append(LoList[value])
                reLa.append(LaList[value])
    return reLo, reLa


def LoLabyLPathAndTime(Tlist, LoList, LaList, Dlist, TIME,
                       loFr, loTo, laFr, laTo):
    middle = np.median(Dlist)
    reLo = []
    reLa = []
    for value in range(len(Tlist)):
        if Tlist[value] == TIME and Dlist[value] > middle:
            if LoList[value] < loTo and LoList[value] > loFr \
               and LaList[value] < laTo and LaList[value] > laFr:
                reLo.append(LoList[value])
                reLa.append(LaList[value])
    return reLo, reLa


def LoLabySPathAndTime(Tlist, LoList, LaList, Dlist, TIME,
                       loFr, loTo, laFr, laTo):
    middle = np.median(Dlist)
    reLo = []
    reLa = []
    for value in range(len(Tlist)):
        if Tlist[value] == TIME and Dlist[value] < middle:
            if LoList[value] < loTo and LoList[value] > loFr \
               and LaList[value] < laTo and LaList[value] > laFr:
                reLo.append(LoList[value])
                reLa.append(LaList[value])
    return reLo, reLa


def Get_BiggestLowest(nparray):
    maxnum = math.floor(np.amax(nparray) * 10) / 10
    minnum = math.ceil(np.amin(nparray) * 10) / 10
    return maxnum, minnum
