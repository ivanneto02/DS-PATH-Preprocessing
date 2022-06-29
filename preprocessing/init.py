from preprocessing import compile_csv
from preprocessing import gather_definitions

from utils import proceed

def main():
    # compile csv
    compile_csv.main()

    # gather definitions
    gather_definitions.main()

if __name__ == "__main__":
    print("You are running the main program that will preprocess the raw data.")

    if proceed():
        main()