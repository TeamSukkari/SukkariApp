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
    index_row = 0
    for row in df.itertuples():

        # Load values from db
        index = index_row
        taskname = row.taskname
        title = row.title
        thumbnail = row.thumbnail
        description = row.description
        tags = row.tags
        totalTime = row.totalTime
        steps = [row.step1, row.step2, row.step3, row.step4, row.step5]
        times = [row.time1, row.time2, row.time3, row.time4, row.time5]

        # print(index, taskname, title, thumbnail, description, tags, totalTime, steps, times, sep="\n")

        # Create recipe_simple
        with open("./recipe_simple.json", "r", encoding="utf-8") as f:
            template_simple = json.load(f)

            # imagepath
            template_simple["hero"]["url"] = thumbnail

            # title
            template_simple["body"]["contents"][1]["text"] = title

            # description
            template_simple["body"]["contents"][2]["text"] = description

            # totalTime
            template_simple["body"]["contents"][3]["text"] = totalTime

            # Create json filename
            filename_json = "./recipe_simple_" + str(taskname) + ".json"
            with open(filename_json, "w", encoding="utf-8") as o:
                print(json.dumps(template_simple, indent=2, ensure_ascii=False), file=o)

        # Create recipe detail
        with open("recipe_detail.json", "r", encoding="utf-8") as f:
            template_detail = json.load(f)

            # imagepath
            template_detail["hero"]["url"] = thumbnail

            # title
            template_detail["body"]["contents"][0]["text"] = title

            # description
            template_detail["body"]["contents"][1]["text"] = description

            # steps and times
            count = 0
            for content in template_detail["body"]["contents"][3]["contents"]:

                # step
                # print(content["contents"][1]["text"])
                content["contents"][1]["text"] = steps[count]

                # time
                # print(content["contents"][2]["text"])
                content["contents"][2]["text"] = times[count]

                count += 1

            # totalTime
            template_detail["body"]["contents"][5]["text"] = totalTime

            # Create json filename
            filename_json = "./recipe_detail_" + str(taskname) + ".json"
            with open(filename_json, "w", encoding="utf-8") as o:
                print(json.dumps(template_detail, indent=2, ensure_ascii=False), file=o)

        index_row += 1


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
