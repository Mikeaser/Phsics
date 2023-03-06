import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    data = np.loadtxt('作业3/SunSpot.txt', float)
    Data = pd.DataFrame(data)
    Data = Data[Data[4]!= -1.0]
    plt.plot(Data[3], Data[4])
    plt.xlabel('Time(year)')
    plt.ylim([0, 600])
    plt.ylabel('Sun Spot Number')
    plt.title('Sun Spot Number - Time Figure')
    plt.savefig('./作业3/ResultSunSpot.jpg')
    return 0


if __name__ == "__main__":
    main()