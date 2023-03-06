import pandas as pd

def main():
    data = pd.read_table('作业3/SunSpot.txt', sep='\t', header=None)
    print(data)




    return 0


if __name__ == "__main__":
    main()