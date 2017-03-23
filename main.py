
import os
import matplotlib.pyplot as plt

from numpy import mean, median
from Functions.readCSV import Sourec_Search
from Functions.statistics import LongShort_path


def makepolt(x):
    n, bins, patches = plt.hist(x, 100, normed=1, facecolor='g')
    plt.show()


if __name__ == '__main__':
    sourcepath = os.path.join(os.getcwd(), 'DATA',
                              'yellow_tripdata_2016-01.csv')

    List = Sourec_Search(sourcepath, 'tpep_pickup_datetime', 'trip_distance')

    A, B = LongShort_path(List[0], List[1])
    print(A)
    print(B)
