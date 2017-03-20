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
