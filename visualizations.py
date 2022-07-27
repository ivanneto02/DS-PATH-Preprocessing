import src.UMLSConnector as connector
from config import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime
from src.DataVisualization import source_graphs
import os

def run_visualizations():
    print("> Starting the visualization process")
    # connect to database, return connection
    print("> Reading dataset")
    df = pd.read_csv(DATA_PATH + "/" + BARE_TABLE_IN_FILE, nrows=None)

    print("> Creating source graphs")
    source_graphs(df=df)

    print("> Creating UMLS CUI connection")
    # Will do in a second

if __name__ == "__main__":
    run_visualizations()