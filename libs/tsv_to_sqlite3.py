import pandas as pd
import sqlite3

def init_db():
    """ Load tsv and create database

    Rertuns:
        bool: True if succeed to create db
        """

    ret = None

    try:
        # Load tsv
        df = pd.read_csv("./recipelist.tsv", delimiter="\t")

        # Create database
        file_sqlite3 = "./recipelist.db"
        conn = sqlite3.connect(file_sqlite3)

        # Output recipe
        df.to_sql("recipe", conn, if_exists="replace", index=None)
        conn.close()

        ret = True
    except:
        ret = False

    return ret