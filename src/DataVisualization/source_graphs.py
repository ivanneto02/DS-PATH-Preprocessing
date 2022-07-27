import matplotlib.pyplot as plt
from datetime import datetime
import os
from config import *

def source_graphs(df=None):

    plt.style.use('seaborn')

    print("> Separating drugs and diseases")
    dis_df = df[df["concept_type"] == "disease"]
    dru_df = df[df["concept_type"] == "drug"]

    if not os.path.exists(IMAGES_SAVE_PATH):
        os.makedirs(IMAGES_SAVE_PATH)

    # All concepts
    print("> Saving all concepts sources count graphs")
    plt.figure()
    df["source_name"].value_counts().plot(kind="pie", autopct=lambda p: f"{p:.2f}% ({p*len(df)/100:.0f})", label="")
    plt.title("Source distribution for all concepts")
    plt.savefig(IMAGES_SAVE_PATH + "/" + f"source_graph_all_concepts_pie_{datetime.now().strftime('%H-%M-%S_%Y-%m-%d')}", bbox_inches='tight', dpi=500)
    plt.close()
    plt.figure()
    df["source_name"].value_counts().plot(kind="bar")
    plt.title("Source distribution for all concepts")
    plt.xticks(rotation=45)
    plt.xlabel("source")
    plt.ylabel("count")
    plt.savefig(IMAGES_SAVE_PATH + "/" + f"source_graph_all_concepts_bar_{datetime.now().strftime('%H-%M-%S_%Y-%m-%d')}", bbox_inches='tight', dpi=500)
    plt.close()

    # Disease concepts
    print("> Saving disease sources count graphs")
    plt.figure()
    dis_df["source_name"].value_counts().plot(kind="pie", autopct=lambda p: f"{p:.2f}% ({p*len(df)/100:.0f})", label="")
    plt.title("Source distribution for diseases")
    plt.savefig(IMAGES_SAVE_PATH + "/" + f"source_graph_disease_pie_{datetime.now().strftime('%H-%M-%S_%Y-%m-%d')}", bbox_inches='tight', dpi=500)
    plt.close()
    plt.figure()
    dis_df["source_name"].value_counts().plot(kind="bar")
    plt.title("Source distribution for diseases")
    plt.xticks(rotation=45)
    plt.xlabel("source")
    plt.ylabel("count")
    plt.savefig(IMAGES_SAVE_PATH + "/" + f"source_graph_disease_bar_{datetime.now().strftime('%H-%M-%S_%Y-%m-%d')}", bbox_inches='tight', dpi=500)
    plt.close()

    # Drug concepts
    plt.figure()
    dru_df["source_name"].value_counts().plot(kind="pie", autopct=lambda p: f"{p:.2f}% ({p*len(df)/100:.0f})", label="")
    plt.title("Source distribution for drugs")
    plt.savefig(IMAGES_SAVE_PATH + "/" + f"source_graph_drug_pie_{datetime.now().strftime('%H-%M-%S_%Y-%m-%d')}", bbox_inches='tight', dpi=500)
    plt.close()
    plt.figure()
    dru_df["source_name"].value_counts().plot(kind="bar")
    plt.title("Source distribution for drugs")
    plt.xticks(rotation=45)
    plt.xlabel("source")
    plt.ylabel("count")
    plt.savefig(IMAGES_SAVE_PATH + "/" + f"source_graph_drug_bar_{datetime.now().strftime('%H-%M-%S_%Y-%m-%d')}", bbox_inches='tight', dpi=500)
    plt.close()