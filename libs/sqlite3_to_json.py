import json
import pandas as pd
import sqlite3


def db_to_json():
    """ Load database and create json files
    """

    # Read sqlite3 database
    file_sqlite3 = "./recipelist.db"
    conn = sqlite3.connect(file_sqlite3)
    df = pd.read_sql_query("SELECT * FROM recipe", conn)
    conn.close()

    # Create jsons
    for row in df.itertuples():

        # Load values from db
        taskname = str(row.taskname)
        title = str(row.title)
        thumbnail = str(row.thumbnail)
        description = str(row.description)
        tags = str(row.tags)
        totalTime = str(row.totalTime)
        steps = [str(row.step1), str(row.step2), str(row.step3), str(row.step4), str(row.step5)]
        times = [str(row.time1), str(row.time2), str(row.time3), str(row.time4), str(row.time5)]

        # Create recipe_simple
        with open("./static/json/recipe_simple.json", "r", encoding="utf-8") as f:
            template_simple = json.load(f)

            # imagepath
            template_simple["hero"]["url"] = template_simple["hero"]["url"].replace(r"{imagePath}", str(thumbnail))

            # title
            template_simple["body"]["contents"][1]["text"] = template_simple["body"]["contents"][1]["text"].replace(r"{title}", str(title))

            # description
            template_simple["body"]["contents"][2]["text"] = template_simple["body"]["contents"][2]["text"].replace(r"{description}", str(description))

            # totalTime
            template_simple["body"]["contents"][3]["text"] = template_simple["body"]["contents"][3]["text"].replace(r"{totalTime}", str(totalTime))

            # Create json filename
            filename_json = "/recipe_simple_" + str(taskname) + ".json"
            with open(filename_json, "w", encoding="utf-8") as o:
                print(json.dumps(template_simple, indent=2, ensure_ascii=False), file=o)

        # Create recipe detail
        with open("./static/json/recipe_detail.json", "r", encoding="utf-8") as f:
            template_detail = json.load(f)

            # imagepath
            template_detail["hero"]["url"] = template_detail["hero"]["url"].replace(r"{imagePath}", str(thumbnail))

            # title
            template_detail["body"]["contents"][0]["text"] = template_detail["body"]["contents"][0]["text"].replace(r"{title}", str(title))

            # description
            template_detail["body"]["contents"][1]["text"] = template_detail["body"]["contents"][1]["text"].replace(r"{description}", str(description))

            # steps and times
            template_detail["body"]["contents"][3]["contents"][0]["contents"][1]["text"] = template_detail["body"]["contents"][3]["contents"][0]["contents"][1]["text"].replace(r"{step1}", steps[0])
            template_detail["body"]["contents"][3]["contents"][0]["contents"][2]["text"] = template_detail["body"]["contents"][3]["contents"][0]["contents"][2]["text"].replace(r"{time1}", times[0])

            template_detail["body"]["contents"][3]["contents"][1]["contents"][1]["text"] = template_detail["body"]["contents"][3]["contents"][1]["contents"][1]["text"].replace(r"{step2}", steps[1])
            template_detail["body"]["contents"][3]["contents"][1]["contents"][2]["text"] = template_detail["body"]["contents"][3]["contents"][1]["contents"][2]["text"].replace(r"{time2}", times[1])

            template_detail["body"]["contents"][3]["contents"][2]["contents"][1]["text"] = template_detail["body"]["contents"][3]["contents"][2]["contents"][1]["text"].replace(r"{step3}", steps[2])
            template_detail["body"]["contents"][3]["contents"][2]["contents"][2]["text"] = template_detail["body"]["contents"][3]["contents"][2]["contents"][2]["text"].replace(r"{time3}", times[2])

            template_detail["body"]["contents"][3]["contents"][3]["contents"][1]["text"] = template_detail["body"]["contents"][3]["contents"][3]["contents"][1]["text"].replace(r"{step4}", steps[3])
            template_detail["body"]["contents"][3]["contents"][3]["contents"][2]["text"] = template_detail["body"]["contents"][3]["contents"][3]["contents"][2]["text"].replace(r"{time4}", times[3])

            template_detail["body"]["contents"][3]["contents"][4]["contents"][1]["text"] = template_detail["body"]["contents"][3]["contents"][4]["contents"][1]["text"].replace(r"{step5}", steps[4])
            template_detail["body"]["contents"][3]["contents"][4]["contents"][2]["text"] = template_detail["body"]["contents"][3]["contents"][4]["contents"][2]["text"].replace(r"{time5}", times[4])

            # totalTime
            totalTime
            template_detail["body"]["contents"][5]["text"] = template_detail["body"]["contents"][5]["text"].replace(r"{totalTime}", str(totalTime))

            # Create json filename
            filename_json = "./recipe_detail_" + str(taskname) + ".json"
            with open(filename_json, "w", encoding="utf-8") as o:
                print(json.dumps(template_detail, indent=2, ensure_ascii=False), file=o)


# def get_recipe_simple(taskname):
#     """
#     Args:
#         taskname (str): unique name of task
#     Returns:
#         json.: Recipe if succeed to find taskname, otherwise None
#     """

#     recipe = None

#     # Read sqlite3 database
#     file_sqlite3 = "./recipelist.db"
#     conn = sqlite3.connect(file_sqlite3)
#     df = pd.read_sql_query("SELECT * FROM recipe", conn)
#     conn.close()

#     # Search for matching task
#     row = df[df["taskname"]==taskname]
#     if row.empty:
#         recipe = None

#     # Load values from db
#     taskname = row.taskname
#     title = row.title
#     thumbnail = row.thumbnail
#     description = row.description
#     tags = row.tags
#     totalTime = row.totalTime
#     steps = [row.step1, row.step2, row.step3, row.step4, row.step5]
#     times = [row.time1, row.time2, row.time3, row.time4, row.time5]

#     # Create recipe_simple
#     with open("./static/json/recipe_simple.json", "r", encoding="utf-8") as f:
#         template_simple = json.load(f)

#         # imagepath
#         template_simple["hero"]["url"] = thumbnail

#         # title
#         template_simple["body"]["contents"][1]["text"] = title

#         # description
#         template_simple["body"]["contents"][2]["text"] = description

#         # totalTime
#         template_simple["body"]["contents"][3]["text"] = totalTime

#         recipe = template_simple

#     return recipe


# recipe_simple =  get_recipe_simple("toilet")
# print(type(recipe_simple), recipe_simple)
# dumpfile = json.dumps(recipe_simple, indent=2, ensure_ascii=False)
# print(dumpfile)


# ''' recipe_simple '''
# print(f"--- Load template of recipe_simple ---")
# with open("./example_recipe_simple.json", "r", encoding="utf-8") as f:
#     template_simple = json.load(f)
#     # print('json_dict:{}'.format(type(json_dict)))
#     # pprint(template_simple)
#     # print(json.dumps(template_simple, indent=2))
#     # print(json_dict["body"]["action"]["uri"])

#     # imagepath
#     print(template_simple["hero"]["url"])

#     # title
#     print(template_simple["body"]["contents"][1]["text"])

#     # description
#     print(template_simple["body"]["contents"][2]["text"])

#     # totalTime
#     print(template_simple["body"]["contents"][3]["text"])


# ''' recipe_detail '''
# print(f"\n---Load template of recipe_detail ---")
# with open("D:\Data\Programs\Git\SUKKARI_YahooHackDay2021\docs-private\json\example_recipe_detail.json", "r", encoding="utf-8") as f:
#     template_detail = json.load(f)
#     # print('json_dict:{}'.format(type(json_dict)))
#     # pprint(json_dict)
#     # print(json_dict["body"]["action"]["uri"])

#     # imagepath
#     print(template_detail["hero"]["url"])

#     # title
#     print(template_detail["body"]["contents"][0]["text"])

#     # description
#     print(template_detail["body"]["contents"][1]["text"])

#     # steps and times
#     for content in template_detail["body"]["contents"][3]["contents"]:
#         # step
#         print(content["contents"][1]["text"])
#         content["contents"][1]["text"] = "This is STEP X"

#         # time
#         print(content["contents"][2]["text"])
#         content["contents"][2]["text"] = "It takes N minutes"

#     # totalTime
#     print(template_detail["body"]["contents"][5]["text"])
