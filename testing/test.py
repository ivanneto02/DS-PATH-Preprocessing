import pandas as pd
from utils.information import *

def print_fewlines():
    df = pd.read_csv(DATA_PATH + "/" + OUT_FILE, nrows=10)
    print(df.head(10))

if __name__ == "__main__":
    print_fewlines()