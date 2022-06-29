import pandas as pd
from utils.information import *

def test():
    df = pd.read_csv(DATA_PATH + "/data.csv", nrows=10)
    print(df.head(10))

if __name__ == "__main__":
    test()