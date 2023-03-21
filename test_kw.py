import matplotlib.pyplot as plt
from pymongo import MongoClient
import urllib
from Levenshtein import jaro
import json
import time
import pprint

# dict_kw = {}
all_topic = ["Thể thao", "Giải trí", "Công nghệ", "Khác", "Xã hội", "Kinh doanh", "Chính trị", "Chiến tranh"]

def get_database():
    username = urllib.parse.quote_plus('sontung2310')
    password = urllib.parse.quote_plus("Vmagcut99!")
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb+srv://{}:{}@cluster0.gyiy6tr.mongodb.net/?retryWrites=true&w=majority".format(username,password)
    CONNECTION_STRING = "mongodb://127.0.0.1:27017/"
    client = MongoClient(CONNECTION_STRING)
    return client['social_listening_storage']

def compare_text(tag, lst_keyword):
    if len(lst_keyword) == 0: return False, ""
    for KW in lst_keyword:
        # print("{} compare to {}, with score {}".format(tag,KW,jaro(tag,KW)))
        if jaro(tag,KW)>0.9:
            # print("Find similarity: ",tag,KW)
            return True, KW
        else:
            continue
    return False, ""

def list_KW(database, topic=""):
    list_task = ['youtube', 'news_data', 'facebook', 'forum']
    dict_kw = {}
    for task in list_task:
        if task == 'news_data':
            collection = database["news_data"]
        elif task == 'youtube':
            collection = database["youtube"]
        elif task == 'facebook':
            collection = database["facebook"]
        elif task == 'forum':
            collection = database["forum"]
        print("Topic",topic)
        if topic in all_topic:
            item_details = collection.find({"check_flag": True,"topic": topic}, batch_size=100)
        else:
            item_details = collection.find({"check_flag": True}, batch_size=100)
        for item in item_details:
            for artical_tag_dict in item["tags"]:
                artical_tag = artical_tag_dict['KW']
                if artical_tag.lower()=='none':
                    continue
                # Preprocess tag
                # artical_tag = preprocess_tag(artical_tag)
                # if artical_tag not in dict_kw:
                flag_artcile, KW_article = compare_text(artical_tag,list(dict_kw.keys()))
                if not flag_artcile:
                    dict_kw[artical_tag] = {"num_call":1,"sentiment":{"Positive":{"num":0, "text":[]},"Negative":{"num":0, "text":[]},"Neural":{"num":0, "text":[]}}}
                else:
                    dict_kw[KW_article]["num_call"] += 1
                    if task=="youtube" or task=="forum": #Title
                        dict_kw[KW_article]["sentiment"][item["title"]["sentiment"]]["num"] += 1
                        dict_kw[KW_article]["sentiment"][item["title"]["sentiment"]]["text"].append(
                            item["title"]["text"].strip())
                    elif task=="news_data" or task=="facebook": #Content
                        dict_kw[KW_article]["sentiment"][item["content"]["sentiment"]]["num"] += 1
                        dict_kw[KW_article]["sentiment"][item["content"]["sentiment"]]["text"].append(
                            item["content"]["text"].strip())

            for comment in item["comments_infor"]:
                # print(comment)
                try:
                    for cmt_tag_dict in comment["key_infor"]:
                        cmt_tag = cmt_tag_dict['KW']
                        # Preprocess tag
                        # cmt_tag = preprocess_tag(cmt_tag)

                        # If Keywords is NONE -> Only update to KW of article
                        if (len(comment["key_infor"])==1) and cmt_tag.lower()=="none":
                            for artical_tag_dict in item["tags"]:
                                artical_tag = artical_tag_dict['KW']
                                # artical_tag = preprocess_tag(artical_tag)
                                dict_kw[artical_tag]["num_call"] += 1
                                dict_kw[artical_tag]["sentiment"][comment["sentiment"]]["num"] += 1
                                dict_kw[artical_tag]["sentiment"][comment["sentiment"]]["text"].append(comment["comment"].strip())
                            continue
                        if cmt_tag.lower()=='none':
                            continue
                        # if cmt_tag not in dict_kw:
                        flag_cmt, KW_cmt = compare_text(cmt_tag, list(dict_kw.keys()))
                        if not flag_cmt:
                            dict_kw[cmt_tag] = {"num_call":1,"sentiment":{"Positive":{"num":0, "text":[]},"Negative":{"num":0, "text":[]},"Neural":{"num":0, "text":[]}}}
                            dict_kw[cmt_tag]["sentiment"][comment["sentiment"]]["num"] +=1
                            dict_kw[cmt_tag]["sentiment"][comment["sentiment"]]["text"].append(comment["comment"].strip())
                        else:
                            dict_kw[KW_cmt]["num_call"] += 1
                            dict_kw[KW_cmt]["sentiment"][comment["sentiment"]]["num"] +=1
                            dict_kw[KW_cmt]["sentiment"][comment["sentiment"]]["text"].append(comment["comment"].strip())
                except:
                    continue
    new_dict = dict(sorted(dict_kw.items(), key=lambda item: item[1]["num_call"], reverse=True))
    return new_dict

if __name__ == "__main__":
    social_db = get_database()
    new_dict = list_KW(database=social_db, topic='Giải trí')
    # # # print(dict_kw)
    print(len(new_dict.keys()))
    
    # # print("Establish table: ",time.time()-start_time)
    # # # print(new_dict)
    with open('result_test.json', 'w', encoding="utf8") as fp:
        json.dump(new_dict, fp, ensure_ascii=False)
