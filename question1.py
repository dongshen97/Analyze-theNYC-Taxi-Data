import os
import matplotlib.pyplot as plt

from matplotlib.colors import LogNorm

from Functions.readCSV import Sourec_PickupWhere
from Functions.readCSV import FormatType


def makepolt(x, y):
    plt.hist2d(x, y, bins=200, norm=LogNorm())
    plt.show()


if __name__ == '__main__':
    sourcepath = os.path.join(os.getcwd(), 'DATA',
                              'yellow_tripdata_2016-01.csv')
    reTime = []
    reLo = []
    reLa = []
    time, longitude, latitude = Sourec_PickupWhere(sourcepath)

    reTime, reLo, reLa = FormatType(time, longitude, latitude, 0, len(time),
                                    -74.05, -73.75, 40.6, 40.85)
    print("Data Format Complete")

    makepolt(reLo, reLa)
