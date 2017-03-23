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


def Sourec_Search(sourcepath, *args):
    search = []
    returnList = []
    for value in args:
        search.append(value)
    with open(sourcepath, 'r', newline='') as csvreader:
        filereader = pd.read_csv(csvreader,
                                 usecols=search)
    for value in args:
        if value is 'tpep_pickup_datetime':
            up_time = []
            for val in filereader['tpep_pickup_datetime']:
                up_time.append(val.split()[1].split(":")[0])
            returnList.append(np.array(up_time).astype(np.int))
        else:
            returnList.append(filereader[value].values.astype(np.float))
    return returnList


def FormatType(ListT, ListLo, ListLa, fromID, toID, loFr, loTo, laFr, laTo):
    returnListT = []
    returnListLo = []
    returnListLa = []
    for value in range(fromID, toID):
        if ListLo[value] < loTo and ListLo[value] > loFr \
           and ListLa[value] < laTo and ListLa[value] > laFr:
            returnListT.append(int(ListT[value].split()[1].split(":")[0]))
            returnListLo.append(float(ListLo[value]))
            returnListLa.append(float(ListLa[value]))
    returnListT = np.array(returnListT).astype(np.int)
    returnListLo = np.array(returnListLo).astype(np.float)
    returnListLa = np.array(returnListLa).astype(np.float)
    return returnListT, returnListLo, returnListLa
