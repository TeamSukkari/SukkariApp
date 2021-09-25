import pandas as pd
import sqlite3
import lib


def init_db():
    ret = True

    print(lib.DATABASE_LOCATION)
    connection = sqlite3.connect(lib.DATABASE_LOCATION)

    coursor = connection.cursor()
    connection.execute("CREATE TABLE IF NOT EXISTS users (userid TEXT PRIMARY KEY NOT NULL, fkrecipeid INTLIST NOT NULL)")
    connection.execute("CREATE TABLE IF NOT EXISTS recipes (id INTEGER PRIMARY KEY AUTOINCREMENT, taskname TEXT NOT NULL, title TEXT NOT NULL, thumbnail TEXT NOT NULL, description TEXT NOT NULL, tags TEXT, totalTime TEXT, step1 TEXT, time1 TEXT, step2 TEXT, time2 TEXT, step3 TEXT, time3 TEXT, step4 TEXT, time4 TEXT, step5 TEXT, time5 TEXT)")

    result = coursor.execute("SELECT MAX(id) From recipes").fetchall()
    print(result)

    if result[0][0] is None:
        print("### Loading from static tsv...")
        df = pd.read_csv("C:\\Users\\admlocal\\Desktop\\SukkariApp\\static\\data\\recipelist_copy.tsv", delimiter="\t")

        for index, row in df.iterrows():
            connection.execute("INSERT INTO recipes (taskname, title, thumbnail, description, tags, totalTime, step1, time1, step2, time2, step3, time3, step4, time4, step5, time5) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )", (row["taskname"], row["title"], row["thumbnail"], row["description"], row["tags"], row["totalTime"], row["step1"], row["time1"], row["step2"], row["time2"], row["step3"], row["time3"], row["step4"], row["time4"], row["step5"], row["time5"]))
        connection.commit()
    
    else:
        print("### Data is exist.")

    return ret

def select_recipe_json(taskname: str):
    init_db()

    connection = sqlite3.connect(lib.DATABASE_LOCATION)

    coursor = connection.cursor()
    result = connection.execute("SELECT * from recipes where taskname='" + taskname + "'").fetchall()
    
    print(result)

    #TODO: json file への追加
    #return jsondata


# TODO: userid から recipeid を特定し応答する Function.
# def select_user_recipes(userid: str):
#     init_db()
#     ret = True
#     connection = sqlite3.connect(lib.DATABASE_LOCATION)
#     coursor = connection.cursor()
#     connection.execute("CREATE TABLE IF NOT EXISTS users (userid TEXT PRIMARY KEY NOT NULL, fkrecipeid INTLIST NOT NULL)")
#     return ret
