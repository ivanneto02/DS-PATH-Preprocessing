import sys
sys.path.insert(0, "")
from utils.proceed import proceed
from config import *
import pandas as pd
import time

def fix_sources():
    # do stuff to gather definitions
    print("> Fixing the source column...")

    df = pd.read_csv(DATA_PATH + "/data.csv", nrows=None)
    df.head(10)

    print("Done.")

if __name__ == "__main__":
    print("""You are running this program without the usage of `main.py`
    in the root directory. * This program will separate the name of the
    drugs from the definitions of the drugs, in the data that has been
    scraped from the internet.\n""")

    if proceed():
        fix_sources()