
import os
import matplotlib.pyplot as plt

from multiprocessing import Pool
from multiprocessing import freeze_support

from Functions.readCSV import Sourec_PickupWhere
from Functions.readCSV import FormatType
from Functions.commandfun import getpointnum


def makepolt(x, y):
    plt.hist2d(x, y, bins=200, norm=LogNorm())
    plt.show()


if __name__ == '__main__':
    # on windows plantform
    freeze_support()

    sourcepath = os.path.join(os.getcwd(), 'DATA',
                              'yellow_tripdata_2016-01.csv')
    reTime = []
    reLo = []
    reLa = []
    time, longitude, latitude = Sourec_PickupWhere(sourcepath)

    list_point = getpointnum(len(time))
    with Pool(processes=4) as pool:
        results = [pool.apply_async(FormatType, (time,
                                                 longitude,
                                                 latitude,
                                                 list_point[i],
                                                 list_point[i+1],
                                                 -74.05, -73.75, 40.6, 40.85))
                   for i in range(4)]
        print("Data Format Complete")
        for val in results:
            value = val.get()
            reTime = reTime + value[0]
            reLo = reLo + value[1]
            reLa = reLa + value[2]
        print("Data Merge Complete")

    makepolt(reLo, reLa)
