from utils.proceed import proceed

def main():
    # do stuff to gather definitions
    print("- gathering definitions...")
    pass

if __name__ == "__main__":
    print("""You are running this program without the usage of `main.py`
    in the root directory. * This program will separate the name of the
    drugs from the definitions of the drugs, in the data that has been
    scraped from the internet.\n""")

    if proceed():
        main()

