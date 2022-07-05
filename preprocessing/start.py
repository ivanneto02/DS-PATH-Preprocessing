from venv import create
from .compile_csv import compile_csv
from .fix_sources import fix_sources
from .gather_definitions import gather_definitions
from .unweighted_tfidf import create_unweighted_tfidf
from .weighted_tfidf import create_weighted_tfidf

from utils import proceed

def start():
    # compile csv
    compile_csv()

    # gather definitions
    gather_definitions()

    # create unweighted TFIDF scores
    create_weighted_tfidf()

    # # create weighted TFIDF scores
    # create_unweighted_tfidf()

if __name__ == "__main__":
    print("You are running the main program that will preprocess the raw data.")

    if proceed():
        start()