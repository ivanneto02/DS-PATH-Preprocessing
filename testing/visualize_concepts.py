import pandas as pd
from config import *
import matplotlib.pyplot as plt

def visualize_concepts():
    df = pd.read_csv(DATA_PATH + "/" + OUT_FILE, nrows=10)

    df["concept_type"].value_counts().plot(kind="pie")
    plt.show()

if __name__ == "__main__":
    visualize_concepts()