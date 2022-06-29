from .compile_csv import compile_csv
from .fix_sources import fix_sources
from .gather_definitions import gather_definitions

from utils import proceed

def start():
    # compile csv
    compile_csv()

    # gather definitions
    gather_definitions()

if __name__ == "__main__":
    print("You are running the main program that will preprocess the raw data.")

    if proceed():
        start()