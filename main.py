
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from multiprocessing import Pool
from multiprocessing import freeze_support

from Functions.commandfun import getpointnum
from Functions.statistics import list_time_statistics


def OpenSourceCSV(sourcepath):
    pickup_time = []
    with open(sourcepath, 'r', newline='') as csvreader:
        filereader = pd.read_csv(csvreader,
                                 # nrows=200,
                                 usecols=['tpep_pickup_datetime'])
        for row in filereader['tpep_pickup_datetime']:
            pickup_time.append(row.split()[1].split(":")[0])
    return pickup_time


def addlists(ONElist, TWOlist):
    returnlist = [0]*len(ONElist)
    if len(ONElist) is not len(TWOlist):
        return returnlist
    for val in range(0, len(ONElist)):
        returnlist[val] = ONElist[val] + TWOlist[val]
    return returnlist


def makepolt(x, y):
    plt.bar(x, y, width=1)
    plt.show()


if __name__ == '__main__':
    # on windows plantform
    freeze_support()

    sourcepath = os.path.join(os.getcwd(), 'DATA',
                              'yellow_tripdata_2016-01.csv')
    pickup_time = []
    pickup_time_statistics = [0]*24
    pickup_time_x = list(range(0, 24))

    pickup_time = OpenSourceCSV(sourcepath)
    pickup_time = np.array(pickup_time)
    pickup_time = pickup_time.astype(np.int)

    list_point = getpointnum(pickup_time.size)

    with Pool(processes=4) as pool:
        results = [pool.apply_async(list_time_statistics, (pickup_time,
                                                           list_point[i],
                                                           list_point[i+1]))
                   for i in range(4)]
        for res in results:
            pickup_time_statistics = addlists(pickup_time_statistics,
                                              res.get(timeout=100))

    makepolt(pickup_time_x, pickup_time_statistics)
