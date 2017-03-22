import math
import numpy as np


def list_time_statistics(List, fromID, toID):
    pickup_time_statistics = [0]*24
    for value in List[fromID:toID]:
        pickup_time_statistics[value] += 1
    return pickup_time_statistics


def Get_BiggestLowest(nparray):
    maxnum = math.floor(np.amax(nparray) * 10) / 10
    minnum = math.ceil(np.amin(nparray) * 10) / 10
    return maxnum, minnum
