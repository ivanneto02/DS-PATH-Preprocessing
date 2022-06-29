from utils.proceed import proceed

def main():
    # do stuff to compile csv
    print("- compiling csv...")
    pass

if __name__ == "__main__":
    print("""You are running this program without the usage of `main.py`
    in the root directory. * This program will create a csv file
    that has been processed from the raw data that has been 
    scraped from the internet.\n""")

    if proceed():
        main()

