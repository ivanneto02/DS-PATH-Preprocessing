from json import load
from dotenv import load_dotenv
load_dotenv()
import os

'''
Create a .env file in your ROOT directory (folder where the repository is created, IN the repository).
Add the following variables to the .env file with the format:
    VARIABLE_NAME = "STIRNG"
    VARIABLE_NAME = 100
    VARIABLE_NAME = "100"
    VARIABLE_NAME = STRING
'''

DATA_PATH = os.environ("DATA_PATH")
OUT_FILE = os.environ("OUT_FILE")
NFILES = int(os.environ("N_FILES")) if "None" not in os.environ("N_FILES") else None
FEATURES = int(os.environ("FEATURES"))