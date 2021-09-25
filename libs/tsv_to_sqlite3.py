import pandas as pd
import sqlite3

# Load tsv
df = pd.read_csv("./recipelist_utf8.tsv", delimiter="\t")
# print(df)

# Create database
file_sqlite3 = "./recipelist.db"
conn = sqlite3.connect(file_sqlite3)

# Output recipe
df.to_sql("recipe", conn, if_exists="replace", index=None)

# Close connection
conn.close()