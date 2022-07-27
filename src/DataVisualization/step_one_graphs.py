import matplotlib.pyplot as plt
from datetime import datetime
import os
from config import *
import pandas as pd

def step_one_graphs(df=None):

    print("> Separating CUIs")
    df["present"] = df["CUI"].apply(lambda x: "MAPPED" if not pd.isnull(x) else "None")

    if not os.path.exists(IMAGES_SAVE_PATH):
        os.makedirs(IMAGES_SAVE_PATH)
    
    # All concepts
    print("> Saving step 1 CUIs pie chart")
    plt.figure()
    df["present"].value_counts().plot(kind="pie", autopct=lambda p: f"{p:.2f}% ({p*len(df)/100:.0f})", label="")
    plt.title("Mapped CUI Distribution for all concepts")
    plt.savefig(IMAGES_SAVE_PATH + "/" + f"cuis_pie_{datetime.now().strftime('%H-%M-%S_%Y-%m-%d')}", bbox_inches='tight', dpi=500)
    plt.close()