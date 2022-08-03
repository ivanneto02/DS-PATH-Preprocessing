from json import load
from dotenv import load_dotenv
load_dotenv()
import os

'''
Create a .env file in your ROOT directory [folder where the repository is created, IN the repository].
Add the following variables to the .env file with the format:
    VARIABLE_NAME = "STIRNG"
    VARIABLE_NAME = 100
    VARIABLE_NAME = "100"
    VARIABLE_NAME = STRING
'''

DATA_PATH = os.environ["DATA_PATH"]
FULL_TABLE_IN_FILE = os.environ["FULL_TABLE_IN_FILE"]
FULL_TABLE_OUT_FILE = os.environ["FULL_TABLE_OUT_FILE"]
BARE_TABLE_IN_FILE = os.environ["BARE_TABLE_IN_FILE"]
BARE_TABLE_OUT_FILE = os.environ["BARE_TABLE_OUT_FILE"]
BARE_TABLE_OUT_FILE_STEP_1 = os.environ["BARE_TABLE_OUT_FILE_STEP_1"]
BARE_TABLE_OUT_FILE_STEP_2 = os.environ["BARE_TABLE_OUT_FILE_STEP_2"]
BARE_TABLE_OUT_FILE_STEP_3 = os.environ["BARE_TABLE_OUT_FILE_STEP_3"]
NFILES = int(os.environ["N_FILES"]) if "None" not in os.environ["N_FILES"] else None
FEATURES = int(os.environ["FEATURES"])

MYSQL_USERNAME = os.environ["_MYSQL_USERNAME"]
MYSQL_PASSWORD = os.environ["_MYSQL_PASSWORD"]
MYSQL_PORT = os.environ["_MYSQL_PORT"]
MYSQL_HOST = os.environ["_MYSQL_HOST"]
MYSQL_DATABASE = os.environ["_MYSQL_DB"]

CONCEPT_TABLES_SAVE_PATH = os.environ["_CONCEPT_TABLES_SAVE_PATH"]
RELATION_TABLES_SAVE_PATH = os.environ["_RELATION_TABLES_SAVE_PATH"]
FULL_TABLE_SAVE_PATH = os.environ["_FULL_TABLES_SAVE_PATH"]
BARE_TABLE_SAVE_PATH = FULL_TABLE_SAVE_PATH
IMAGES_SAVE_PATH = os.environ["_IMAGES_SAVE_PATH"]