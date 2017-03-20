
import os
import matplotlib.pyplot as plt

from multiprocessing import Pool
from multiprocessing import freeze_support

from Functions.readCSV import Sourec_PickupWhere
from Functions.commandfun import addlists
from Functions.commandfun import getpointnum
from Functions.statistics import list_time_statistics


def makepolt(x, y):
    plt.bar(x, y, width=1, linewidth=1)
    plt.show()


if __name__ == '__main__':
    # on windows plantform
    freeze_support()

    sourcepath = os.path.join(os.getcwd(), 'DATA',
                              'demo_tripdata_2016-01.csv')
    time = []
    longitude = []
    latitude = []
    pickup_time_statistics = [0]*24
    pickup_time_x = list(range(0, 24))

    time, longitude, latitude = Sourec_PickupWhere(sourcepath)

    print(time)
    print(longitude)
    print(latitude)
