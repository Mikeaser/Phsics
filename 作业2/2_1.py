import numpy as np
import math
import matplotlib.pyplot as plt


def j_0(x):
    '''
    0th order Bessel function
    '''
    if x == 0:
        y = 1
    else:
        y = math.sin(x)/x
    return y


def j_1(x):
    '''
    1st order Bessel function
    '''
    if x == 0:
        y = 0
    else:
        y1 = math.sin(x)/x**2
        y2 = math.cos(x)/x
        y = y1-y2
    return y


def j_0_star(x):
    '''
    Reciprocal 0th order Bessel function for backpropagation
    '''
    y = 1
    return y


def j_1_star(x):
    '''
    Reciprocal first order Bessel function
    '''
    y = 1
    return y


def BesselUpward(x_list, l_max):
    '''
    The specific calculation of the Bessel function using upward method
    Args:
        x_list (list[float]): The x array to be calculated
        l_max (int): The highest order of the Bessel function to be computed
    Returns:
        DataSet: A two-dimensional array, each outer element represents the corresponding point value of the l-th order Bessel function
    '''
    DataSet = []  # A two-dimensional data set for storing curves
    for l in range(l_max+1):
        y_l = []
        n = 0
        for x in x_list:
            if l == 0:
                y = j_0(x)
            if l == 1:
                y = j_1(x)
            if l >= 2:
                # Solve using recurrence relation
                y = (2*l-1)*DataSet[l-1][n]/x - DataSet[l-2][n]
                n += 1
            y_l.append(y)
        DataSet.append(y_l)
    return DataSet


def BesselDownward(x_list, l_max):
    '''
    The specific calculation of the Bessel function using downward method
    Normalization by the 0th order Bessel function using relative value invariance
    Args:
        x_list (list[float]): The x array to be calculated
        l_max (int): The highest order of the Bessel function to be computed
    Returns:
        DataSet: A two-dimensional array, each outer element represents the corresponding point value of the l-th order Bessel function
    '''
    DataSet = []  # A two-dimensional data set for storing curves
    for k in range(l_max+1):
        y_k = []
        n = 0
        for x in x_list:
            if k == 0:
                y = j_0_star(x)
            if k == 1:
                y = j_1_star(x)
            if k >= 2:
                # Solve using recurrence relation
                y = (2*(l_max-k)+3)*DataSet[k-1][n]/x - DataSet[k-2][n]
                n += 1
            y_k.append(y)
        DataSet.append(y_k)
    # Normalized
    for k in range(l_max+1):
        n = 0
        for Bessel_y_k in DataSet[k]:
            DataSet[k][n] = Bessel_y_k * j_0(x_list[n])/DataSet[l_max][n]
            n += 1
    
    return DataSet


if __name__ == "__main__":
    modes = ['upward', 'downward']
    for mode in modes:
        if mode == 'upward':
            x_min = 1e-5
            x_max = 20.0
            l_max = 30
            step = 0.001

            x_list = np.arange(x_min, x_max, step).tolist()
            BesselDataset = BesselUpward(x_list, l_max)

            # Use matplotlib to draw pictures
            DrawNum = [2, 5, 10]
            for l_draw in DrawNum:
                plt.plot(x_list, BesselDataset[l_draw],
                         label="l = " + str(l_draw))
            plt.title('Bessel function -- upward iteration method')
            plt.xlim([0, x_max])
            plt.ylim([-0.2, 0.35])
            plt.xlabel("x")
            plt.ylabel("j(x)")
            plt.legend()
            plt.savefig('./作业2/ResultUpward.jpg')
            plt.close()
            # plt.show()
        if mode == 'downward':
            x_min = 0.001
            x_max = 20.0
            l_max = 30
            step = 0.001

            x_list = np.arange(x_min, x_max, step).tolist()
            BesselDataset = BesselDownward(x_list, l_max)

            # Use matplotlib to draw pictures
            DrawNum = [2, 5, 10]
            # DrawNum = [0, 1, 2]
            for l_draw in DrawNum:
                k_draw = l_max - l_draw
                plt.plot(x_list, BesselDataset[k_draw],
                         label="l = " + str(l_draw))
            plt.title('Bessel function -- downward iteration method')
            plt.xlim([0, x_max])
            plt.ylim([-0.2, 0.35])
            plt.xlabel("x")
            plt.ylabel("j(x)")
            plt.legend()
            plt.savefig('./作业2/ResultDownward.jpg')
            plt.close()
