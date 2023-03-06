import pandas as pd
import matplotlib.pyplot as plt

def main():
    Data = pd.read_csv('./作业3/SeaLevel.csv', skiprows= 5, header=None)  # 前几行不用读取
    for i in range(1,5):
        temp = Data.dropna(subset=[i], axis= 0)
        plt.plot(temp[0], temp[i])
    plt.ylabel("Change in mean sea level [mm]")
    plt.savefig("./作业3/ResultSeaLevel.jpg")
    return 0

if __name__ == '__main__':
    main()

