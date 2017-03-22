"""
remember all function will return numpy array
numpy array is not list, please remember it!!
"""

import numpy as np
import pandas as pd


def Sourec_PickupTime(sourcepath):
    pickup_time = []
    with open(sourcepath, 'r', newline='') as csvreader:
        filereader = pd.read_csv(csvreader,
                                 usecols=['tpep_pickup_datetime'])
        for row in filereader['tpep_pickup_datetime']:
            pickup_time.append(row.split()[1].split(":")[0])
    pickup_time = np.array(pickup_time).astype(np.int)
    return pickup_time


# ptpep_pickup_datetime, ickup_longitude, pickup_latitude
def Sourec_PickupWhere(sourcepath):
    up_time = []
    up_longitude = []
    up_latitude = []
    with open(sourcepath, 'r', newline='') as csvreader:
        filereader = pd.read_csv(csvreader,
                                 usecols=['tpep_pickup_datetime',
                                          'pickup_longitude',
                                          'pickup_latitude'])
        for val in range(len(filereader['tpep_pickup_datetime'])):
            up_time.append(filereader['tpep_pickup_datetime'][val])
            up_longitude.append(filereader['pickup_longitude'][val])
            up_latitude.append(filereader['pickup_latitude'][val])
    print("Open File Complete")
    return up_time, up_longitude, up_latitude


def FormatType(ListT, ListLo, ListLa, fromID, toID, loFr, loTo, laFr, laTo):
    returnListT = []
    returnListLo = []
    returnListLa = []
    for value in range(fromID, toID):
        if ListLo[value] < loTo and ListLo[value] > loFr \
           and ListLa[value] < laTo and ListLa[value] > laFr:
            returnListT.append(ListT[value].split()[1].split(":")[0])
            returnListLo.append(ListLo[value])
            returnListLa.append(ListLa[value])
    return returnListT, returnListLo, returnListLa


def ToNumpType(List, isInt=True):
    if isInt:
        List = np.array(List).astype(np.int)
    else:
        List = np.array(List).astype(np.float)
    return List
