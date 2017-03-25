
import os
import matplotlib.pyplot as plt

from matplotlib.colors import LogNorm

from Functions.readCSV import Sourec_Search
from Functions.statistics import LongShort_path
from Functions.statistics import LoLabyLPathAndTime, LoLabySPathAndTime


def makepolt(xL, yL, xS, yS):
    plt.subplot(121)
    plt.hist2d(xL, yL, bins=200, norm=LogNorm())
    plt.grid()
    plt.subplot(122)
    plt.hist2d(xS, yS, bins=200, norm=LogNorm())
    plt.grid()
    plt.show()


if __name__ == '__main__':
    sourcepath = os.path.join(os.getcwd(), 'DATA',
                              'yellow_tripdata_2016-01.csv')

    List = Sourec_Search(sourcepath,
                         'tpep_pickup_datetime',
                         'pickup_longitude',
                         'pickup_latitude',
                         'trip_distance')

    LpathTime, SpathTime = LongShort_path(List[0], List[3])
    xL, yL = LoLabyLPathAndTime(List[0], List[1], List[2], List[3],
                                LpathTime[0][0], -74.05, -73.75, 40.6, 40.85)
    xS, yS = LoLabySPathAndTime(List[0], List[1], List[2], List[3],
                                LpathTime[0][0], -74.05, -73.75, 40.6, 40.85)
    makepolt(xL, yL, xS, yS)
