from utils.proceed import proceed

def main():
    # do stuff to gather sources
    print("- mismatching sources...")
    pass

if __name__ == "__main__":
    print("""You are running this program without the usage of `main.py`
    in the root directory. * This program will ensure that all of the sources of
    the drugs match the true sources from the links. If this is not the case, a
    source mismatch will be marked in the source mismatch table.\n""")
 
    if proceed():
        main()

