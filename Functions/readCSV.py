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
    pickup_time = []
    pickup_longitude = []
    pickup_latitude = []
    with open(sourcepath, 'r', newline='') as csvreader:
        filereader = pd.read_csv(csvreader,
                                 usecols=['tpep_pickup_datetime',
                                          'pickup_longitude',
                                          'pickup_latitude'])
        for val in range(len(filereader['tpep_pickup_datetime'])):
            if filereader['pickup_longitude'][val] is '0.0' or \
               filereader['pickup_latitude'][val] is '0.0':
                pass
            else:
                pickup_time.append(filereader['tpep_pickup_datetime'][val])
                pickup_longitude.append(filereader['pickup_longitude'][val])
                pickup_latitude.append(filereader['pickup_latitude'][val])
    return pickup_time, pickup_longitude, pickup_latitude
