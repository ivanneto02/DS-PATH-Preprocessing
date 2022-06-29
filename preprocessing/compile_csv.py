from utils.proceed import proceed

from information import *

import os

def main():
    # do stuff to compile csv
    print("- compiling csv...")

    # Get all the letter folders
    source_folders = next(os.walk(DATA_PATH))[1]

    total_paths = []
    # Iterate through all of the sources
    for source in source_folders:
        # Get all the letter folders
        letter_folders = next(os.walk(DATA_PATH + "/" + source))[1]
        # Iterate through all of the letters
        for letter in letter_folders:
            # get all the files
            files = next(os.walk(DATA_PATH + "/" + source + "/" + letter))[2]
            for fil in files:
                print(f"Getting {DATA_PATH}/{source}/{letter}/{fil}...")
                total_paths.append(DATA_PATH + "/" + source + "/" + letter + "/" + fil)

if __name__ == "__main__":
    print("""You are running this program without the usage of `main.py`
    in the root directory. * This program will create a csv file
    that has been processed from the raw data that has been 
    scraped from the internet.\n""")

    if proceed():
        main()

