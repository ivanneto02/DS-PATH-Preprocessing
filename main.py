import preprocessing.init
import scraping#.here include the file for data scraping

def main():
    # data scraping
    #here run the file for scraping all of the data

    # preprocess the data
    preprocessing.init.main() # Run the main program inside preprocessing

    # rest of the program will be run here

if __name__ == "__main__":
    main()