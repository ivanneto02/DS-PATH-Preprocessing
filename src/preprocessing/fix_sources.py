import sys
sys.path.insert(0, "")
from utils.proceed import proceed
from config import *
import pandas as pd
import time

'''
Currently not working very well. Will have to fix in the future.
- Ivan
'''

def source_specific_fix(source_name, source_url):
    if "health.ri.gov" in source_url:
        return "RIDH"
    elif "medline" in source_url:
        return "Medline"
    elif "www.drugs.com" in source_url:
        return "Drugs.com"
    else:
        return source_name

def fix_sources():
    # do stuff to gather definitions
    print("> Fixing the source column...")
    df = pd.read_csv(DATA_PATH + "/" + FULL_TABLE_IN_FILE, nrows=None)

    # Apply fixes
    df["source_name"] = df.apply(lambda x : source_specific_fix(x["source_name"], x["source_url"]), axis=1)

    # Save
    print("> Saving")
    df.to_csv(DATA_PATH + "/" + FULL_TABLE_OUT_FILE, index=False)
    print("Done.")

if __name__ == "__main__":
    print("""You are running this program without the usage of `main.py`
    in the root directory. * This program will separate the name of the
    drugs from the definitions of the drugs, in the data that has been
    scraped from the internet.\n""")

    if proceed():
        fix_sources()