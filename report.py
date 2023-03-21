# import streamlit as st
import matplotlib.pyplot as plt
from pymongo import MongoClient
import urllib
from Levenshtein import jaro
import json
import time
import pprint
from datetime import datetime, timedelta

# dict_kw = {}
# dict_kw_topic = {}
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
        if jaro(tag,KW)>0.8:
            # print("Find similarity: ",tag,KW)
            return True, KW
        else:
            continue
    return False, ""

def draw_piechart(database,weight_comment=0.5):
    collection = database['youtube']
    pipeline_comment = [
        {"$match":{"check_flag": True}},
        ]

    cur_list = list(collection.aggregate([
        *pipeline_comment,
        {"$unionWith": { "coll": "news_data", "pipeline": pipeline_comment } },
        {"$unionWith": { "coll": "facebook", "pipeline": pipeline_comment } },
        {"$group": {"_id": "$topic", "count": { "$sum": { "$sum": [ {"$multiply":["$num_comments_get",weight_comment]}, 1 ] } }}},
    ]))
        
    return cur_list

def total_count(database, task):
    if task == 'news_data':
        collection = database["news_data"]
    elif task == 'youtube':
        collection = database["youtube"]
    elif task == 'facebook':
        collection = database["facebook"]
    elif task == 'forum':
        collection = database["forum"]
    
    # count_comment = 0
    
    count_analysis = collection.aggregate( [
        {"$match": {"check_flag": True}},
        { "$count": "count" },
    ] )
    
    count_comment = collection.aggregate( [
        {"$unwind": "$comments_infor"},
        {"$match": {"comments_infor.check_flag": True}},
        { "$count": "count" },
    ] )
    return list(count_analysis)[0]['count'], list(count_comment)[0]['count']

def append_url_task(url_array,item,task):
    url_array.append([item,task])
       
def list_KW(database, topic="", time_delta=7):
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
        
        margin_time = (datetime.now() - timedelta(days=time_delta)).timestamp()
        
        if topic in all_topic:
            item_details = collection.find({"check_flag": True,"topic": topic,"time_upload":{"$gte":margin_time}}, batch_size=100)
        else:
            item_details = collection.find({"check_flag": True,"time_upload":{"$gte":margin_time}}, batch_size=100)
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
                    dict_kw[artical_tag] = {"num_call":1,"url":[],"sentiment":{"Positive":{"num":0, "text":[]},"Negative":{"num":0, "text":[]},"Neural":{"num":0, "text":[]}}}
                    append_url_task(dict_kw[artical_tag]['url'], item["_id"], task=task)
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
                    append_url_task(dict_kw[KW_article]['url'], item["_id"], task=task)
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
                                append_url_task(dict_kw[artical_tag]['url'], item["_id"], task=task)
                            continue
                        if cmt_tag.lower()=='none':
                            continue
                        # if cmt_tag not in dict_kw:
                        flag_cmt, KW_cmt = compare_text(cmt_tag, list(dict_kw.keys()))
                        if not flag_cmt:
                            dict_kw[cmt_tag] = {"num_call":1,"type":task,"sentiment":{"Positive":{"num":0, "text":[]},"Negative":{"num":0, "text":[]},"Neural":{"num":0, "text":[]}}}
                            dict_kw[cmt_tag]["sentiment"][comment["sentiment"]]["num"] +=1
                            dict_kw[cmt_tag]["sentiment"][comment["sentiment"]]["text"].append(comment["comment"].strip())
                            append_url_task(dict_kw[cmt_tag]['url'], item["_id"], task=task)
                        else:
                            dict_kw[KW_cmt]["num_call"] += 1
                            dict_kw[KW_cmt]["sentiment"][comment["sentiment"]]["num"] +=1
                            dict_kw[KW_cmt]["sentiment"][comment["sentiment"]]["text"].append(comment["comment"].strip())
                            append_url_task(dict_kw[KW_cmt]['url'], item["_id"], task=task)
                except:
                    continue
    new_dict = dict(sorted(dict_kw.items(), key=lambda item: item[1]["num_call"], reverse=True))
    return new_dict

def list_KW_url(database):
    list_task = ['facebook','youtube', 'news_data', 'forum']
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
                    # print(item["title"]["sentiment"])
                    dict_kw[artical_tag] = {task:{"url":[],"sentiment":{"Positive":0,"Negative":0,"Neural":0}}}
                    # print("alooo: ",dict_kw)
                    # print("artical_tag: ",artical_tag)
                    print("task: ",task)
                    dict_kw[artical_tag][task]['url'].append(item['_id'])
                    if task=="youtube" or task=="forum": #Title
                        dict_kw[artical_tag][task]["sentiment"][item["title"]["sentiment"]] += 1

                    elif task=="news_data" or task=="facebook": #Content
                        dict_kw[artical_tag][task]["sentiment"][item["content"]["sentiment"]] += 1

                else:
                    dict_kw[KW_article][task]['url'].append(item['_id'])
                    if task=="youtube" or task=="forum": #Title
                        dict_kw[KW_article][task]["sentiment"][item["title"]["sentiment"]] += 1

                    elif task=="news_data" or task=="facebook": #Content
                        dict_kw[KW_article][task]["sentiment"][item["content"]["sentiment"]] += 1

            for comment in item["comments_infor"]:
                # print(comment)
                try:
                    for cmt_tag_dict in comment["key_infor"]:
                        cmt_tag = cmt_tag_dict['KW']
                        # Preprocess tag
                        # cmt_tag = preprocess_tag(cmt_tag)

                        # If Keywords is NONE -> Only update to KW of article
                        # if (len(comment["key_infor"])==1) and cmt_tag.lower()=="none":
                        #     for artical_tag_dict in item["tags"]:
                        #         artical_tag = artical_tag_dict['KW']
                        #         # artical_tag = preprocess_tag(artical_tag)
                        #         dict_kw[artical_tag]["num_call"] += 1
                        #         dict_kw[artical_tag]["sentiment"][comment["sentiment"]]["num"] += 1
                        #         dict_kw[artical_tag]["sentiment"][comment["sentiment"]]["text"].append(comment["comment"].strip())
                        #     continue
                        if cmt_tag.lower()=='none':
                            continue
                        # if cmt_tag not in dict_kw:
                        flag_cmt, KW_cmt = compare_text(cmt_tag, list(dict_kw.keys()))
                        if not flag_cmt:
                            dict_kw[cmt_tag] = {task:{"url":[],"sentiment":{"Positive":0,"Negative":0,"Neural":0}}}
                            dict_kw[cmt_tag][task]['url'].append(item['_id'])
                            dict_kw[cmt_tag][task]["sentiment"][comment["sentiment"]] += 1
                            # dict_kw[cmt_tag] = {"num_call":1,"type":task,"sentiment":{"Positive":{"num":0, "text":[]},"Negative":{"num":0, "text":[]},"Neural":{"num":0, "text":[]}}}
                            # dict_kw[cmt_tag]["sentiment"][comment["sentiment"]]["num"] +=1
                            # dict_kw[cmt_tag]["sentiment"][comment["sentiment"]]["text"].append(comment["comment"].strip())
                        else:
                            dict_kw[KW_cmt][task]['url'].append(item['_id'])
                            dict_kw[KW_cmt][task]["sentiment"][comment["sentiment"]] += 1
                            # dict_kw[KW_cmt]["num_call"] += 1
                            # dict_kw[KW_cmt]["sentiment"][comment["sentiment"]]["num"] +=1
                            # dict_kw[KW_cmt]["sentiment"][comment["sentiment"]]["text"].append(comment["comment"].strip())
                except:
                    continue
    # new_dict = dict(sorted(dict_kw.items(), key=lambda item: item[1]["num_call"], reverse=True))
    return dict_kw

def query_channel(database, channel_url):
    collection = database['youtube']
    pipeline = [
        
        {"$match": {"check_flag": True, "channel_url":channel_url}},
        # {"$match": {"time_upload" : { "$type" : "int" }}},
        {"$unwind": "$comments_infor"},
        {"$match": {"$comments_infor.check_flag": True}},
        # {"$unwind": "$comments_infor.key_infor"},
        # {"$unwind": "$tags"},

        ]
    return list(collection.aggregate([
    *pipeline,
    # {"$unionWith": { "coll": "news_data", "pipeline": pipeline } },
    {"$unionWith": { "coll": "facebook", "pipeline": pipeline } }, 
    # {"$unionWith": { "coll": "forum", "pipeline": pipeline } }, 
    {
        "$group": {     
        "_id" :  { 
            "sentiment": "$comments_infor.sentiment",
            "comment": "$comments_infor.comment",
        },
        # "total": { "$sum" : 1 },
        }
    },
    #2
    {
        "$group" : { 
        "_id" :  {
            "sentiment":"$_id.sentiment",
            },
        "count": {
            "$sum": 1
        },
        "comment": { 
            "$push": { 
                "comment": "$_id.comment",
                }
            },
        
        }
    },
    #3
    {
        "$group" : { 
        "_id" : "$_id.sentiment",
        "list_comments": { 
            "$push": { 
                "comments": "$comment",
                "count":"$count"
                }
            }
        }
    },
    {"$sort": {"list_comments.count": 1}},
    ]      
    ))

def query_keywords(database, topic):
    collection = database['youtube']
    pipeline = [
        
        {"$match": {"check_flag": True,"topic":topic}},
        # {"$match": {"time_upload" : { "$type" : "int" }}},
        {"$unwind": "$comments_infor"},
        {"$unwind": "$comments_infor.key_infor"},
        {"$unwind": "$tags"},
        
        ]
    pprint.pprint(list(collection.aggregate([
    *pipeline,
    {"$unionWith": { "coll": "news_data", "pipeline": pipeline } },
    {"$unionWith": { "coll": "facebook", "pipeline": pipeline } }, 
    {"$unionWith": { "coll": "forum", "pipeline": pipeline } }, 
    {
        "$group": {     
        "_id" :  { 
            "KW": "$comments_infor.key_infor.KW",
            "sentiment_cmt": "$comments_infor.sentiment",
            "comment": "$comments_infor.comment",
        },
        }
    },
    #2
    {
        "$group" : { 
        "_id" :  {
            "KW":"$_id.KW",
            "sentiment_cmt": "$_id.sentiment_cmt",
            },
        "count": {
            "$sum": 1
        },
        "comment": { 
            "$push": { 
                "comment": "$_id.comment",
                }
            }
        }
    },
    #3
    {
        "$group" : { 
        "_id" : "$_id.KW",
        "sentiments": { 
            "$push": { 
                "sentiment_cmt": "$_id.sentiment_cmt",
                "comments": "$comment",
                "count":"$count"
                }
            }
        }
    },

    {"$sort": {"sentiments.count": 1}},
    ]      
    )))
    
def search_by_KW(database, keyword):
    collection = database['youtube']
    pipeline = [
        
        {"$match": {"check_flag": True}},
        # {"$match": {"time_upload" : { "$type" : "int" }}},
        {"$unwind": "$comments_infor"},
        {"$unwind": "$comments_infor.key_infor"},
        {"$unwind": "$tags"},
        
        ]
    return collection.aggregate([
    *pipeline,
    # {"$unionWith": { "coll": "news_data", "pipeline": pipeline } },
    # {"$unionWith": { "coll": "facebook", "pipeline": pipeline } }, 
    {"$match": 
        {
            "comments_infor.key_infor.KW": keyword
            # "comments_infor":
            #     { "$elemMatch":
            #         {
            #             "key_infor.KW":"None",
            #         }
            #     }
        }
    },
    #1
    {
        "$group": {     
        "_id" :  { 
            "KW": "$comments_infor.key_infor.KW",
            "sentiment_cmt": "$comments_infor.sentiment",
            "comment": "$comments_infor.comment",
        },
        }
    },
    #2
    {
        "$group" : { 
        "_id" :  {
            "KW":"$_id.KW",
            "sentiment_cmt": "$_id.sentiment_cmt",
            },
        "count": {
            "$sum": 1
        },
        "comment": { 
            "$push": { 
                "comment": "$_id.comment",
                }
            }
        }
    },
    #3
    {
        "$group" : { 
        "_id" : "$_id.KW",
        "sentiments": { 
            "$push": { 
                "sentiment_cmt": "$_id.sentiment_cmt",
                "comments": "$comment",
                "count":"$count"
                }
            }
        }
    },

    {"$sort": {"sentiments.count": 1}},
    ]      
    )

def keyword_report(collection, keyword, time_delta=60):
    
    margin_time = (datetime.now() - timedelta(days=time_delta)).timestamp()
    
    pipeline = [
        {"$match": {"check_flag": True,"time_upload":{"$gte":margin_time}}},
        # {"$match": {"time_upload" : { "$type" : "int" }}},
        {"$unwind": "$comments_infor"},
        # {"$unwind": "$comments_infor.key_infor"},
        # {"$unwind": "$tags"},
        
        ]
    
    list_ids = list(collection.aggregate([
    *pipeline,
    {"$unionWith": { "coll": "news_data", "pipeline": pipeline } },
    {"$unionWith": { "coll": "facebook", "pipeline": pipeline } },
    {"$unionWith": { "coll": "forum", "pipeline": pipeline } }, 
    {"$match": 
        {
            "comments_infor.check_flag":True,
            "$or":[{"$expr": {"$in": [{"KW":keyword}, "$tags"]}},{"$expr": {"$in": [{"KW":keyword}, "$comments_infor.key_infor"]}}],
        }
    },
    {"$group":
        {
            "_id" : "$_id",
        }},
    ]))
    pprint.pprint(list_ids)
    # print(len(list_ids))
    
    search_ids = list(collection.aggregate([
        
    {"$unionWith": { "coll": "news_data" } },
    {"$unionWith": { "coll": "facebook" } },
    {"$unionWith": { "coll": "forum"} }, 
    # {"list_ids" : list(list_ids[i]['_id'] for i in range(len(list_ids)))},
    {"$match": {"check_flag": True}},
    {"$match": 
        {
            # "comments_infor.check_flag":True,
            "_id": {"$in": list(list_ids[i]['_id'] for i in range(len(list_ids)))}
            # "$or":[{"$expr": {"$in": [{"KW":keyword}, "$tags"]}},{"$expr": {"$in": [{"KW":keyword}, "$comments_infor.key_infor"]}}],
        }
    },
    ]))
    # pprint.pprint(search_ids)
    
    
def keyword_tree(collection, keyword, time_delta=7):
    # all_items = collection.find({"check_flag":True,"tags": {"$elemMatch":{"KW":keyword}}})
    # for item in all_items:
    #     print(item)
    
    margin_time = (datetime.now() - timedelta(days=time_delta)).timestamp()

    pipeline = [
        {"$match": {"check_flag": True,"time_upload":{"$gte":margin_time}}},
        # {"$match": {"time_upload" : { "$type" : "int" }}},
        {"$unwind": "$comments_infor"},
        # {"$unwind": "$comments_infor.key_infor"},
        # {"$unwind": "$tags"},
        
        ]
    pprint.pprint(list(collection.aggregate([
    *pipeline,
    {"$unionWith": { "coll": "news_data", "pipeline": pipeline } },
    {"$unionWith": { "coll": "facebook", "pipeline": pipeline } },
    {"$unionWith": { "coll": "forum", "pipeline": pipeline } }, 
    {"$match": 
        {
            "comments_infor.check_flag":True,
            "$or":[{"$expr": {"$in": [{"KW":keyword}, "$tags"]}},{"$expr": {"$in": [{"KW":keyword}, "$comments_infor.key_infor"]}}],
        }
    },
    { "$project": { "total_KW": {"$concatArrays": [ "$tags", "$comments_infor.key_infor" ] } } },
    {"$unwind": "$total_KW"},
    #1
    {
        "$group": {     
        "_id" :  {
            "query_keyword": keyword,
            "KW": "$total_KW.KW",
        },
        "total": { "$sum" : 1 } 
        }, 
    },
    {"$sort": {"total": 1}},
    ])))
def group_kw(collection, keyword, time_delta=7):
    margin_time = (datetime.now() - timedelta(days=time_delta)).timestamp()
    # collection = database['youtube']
    pipeline = [
        {"$match": {"check_flag": True, "time_upload":{"$gte":margin_time}}},
        # {"$match": {"time_upload" : { "$type" : "int" }}},
        {"$unwind": "$comments_infor"},
        {"$unwind": "$comments_infor.key_infor"},
        {"$unwind": "$tags"},
        
        ]
    pprint.pprint(list(collection.aggregate([
    *pipeline,
    {"$unionWith": { "coll": "news_data", "pipeline": pipeline } },
    {"$unionWith": { "coll": "facebook", "pipeline": pipeline } },
    {"$unionWith": { "coll": "forum", "pipeline": pipeline } }, 
    {"$match": 
        {
            "tags.KW": keyword
        }
    },
    #1
    {
        "$group": {     
        "_id" :  { 
            "KW_article": "$tags.KW",
            "KW_cmt": "$comments_infor.key_infor.KW",
            # "comment": "$comments_infor.comment",
        },
        "total": { "$sum" : 1 } 
        },
        
    },
    
    #2
    { "$group" : { 
        "_id" :  "$_id.KW_article", 
        "related_kw": { 
            "$push": { 
                "KW": "$_id.KW_cmt",
                "total":"$total"
            }
        }
        }
    },
    {"$unwind": "$related_kw"},
    {"$sort": {"related_kw.total": 1}},
    ])))
    
def trend_line(database, time_delta=7):
    margin_time = (datetime.now() - timedelta(days=time_delta)).timestamp()
    pipeline = [
        {"$match": {"check_flag": True, "time_upload":{"$gte":margin_time}}},
        {"$match": {"time_upload" : { "$type" : "int" }}},
        {"$unwind": "$comments_infor"},
        {"$unwind": "$comments_infor.key_infor"},
        ]
    
    collection = database['youtube']
        

    list_trend =  list(collection.aggregate([
    *pipeline,
    {"$unionWith": { "coll": "news_data", "pipeline": pipeline } },
    {"$unionWith": { "coll": "facebook", "pipeline": pipeline } },
    
    { 
        "$group": { 
        "_id" :  { 
            "KW": "$comments_infor.key_infor.KW",
            "day": { "$floor": { "$divide": [ "$time_upload", 60*60*24 ] } },
        },
        "total": { "$sum" : 1 } 
    }
    },
    { "$group" : { 
        "_id" :  "$_id.KW", 
        "dates": { 
            "$push": { 
                "day": "$_id.day",
                "total":"$total"
            }
        }
    }
    },
    {"$sort": {"dates.total": 1}},
    ]      
    ))
    return list_trend

def trend_line_tag(database, time_delta=7):
    margin_time = (datetime.now() - timedelta(days=time_delta)).timestamp()
    
    pipeline = [
        {"$match": {"check_flag": True, "time_upload":{"$gte":margin_time}}},
        {"$match": {"time_upload" : { "$type" : "int" }}},
        {"$unwind": "$tags"},
        # {"$unwind": "$comments_infor"},
        # {"$unwind": "$comments_infor.key_infor"},
        ]
    
    collection = database['youtube']
        

    list_trend_tag =  list(collection.aggregate([
    *pipeline,
    {"$unionWith": { "coll": "news_data", "pipeline": pipeline } },
    {"$unionWith": { "coll": "facebook", "pipeline": pipeline } },
    
    { 
        "$group": { 
        "_id" :  { 
            "KW": "$tags.KW",
            "day": { "$floor": { "$divide": [ "$time_upload", 60*60*24 ] } },
        },
        # "total": { "$sum" : "$num_comments_get" } 
        "total": { "$sum" : 1 } 
    }
    },
    { "$group" : { 
        "_id" :  "$_id.KW", 
        "dates": { 
            "$push": { 
                "day": "$_id.day",
                "total":"$total"
            }
        }
    }
    },
    {"$sort": {"dates.total": 1}},
    ]      
    ))
    return list_trend_tag
        
def group_keywords(collection_temp):
    pipeline = [
        {"$unwind": "$dates"},
        {
            "$group" : { 
                "_id" :  {
                    "kw":"$kw",
                    "dates": "$dates.day",
                    },
                "total": {
                    "$sum": "$dates.total"
                },
            }
        },
        {
            "$group" : { 
                "_id" :  "$_id.kw",
                "dates": {
                    "$push": { 
                        "day": "$_id.dates",
                        "total":"$total"
                        }
                }
            }
        },     
    ]
    return list(collection_temp.aggregate(pipeline))

def get_trend_kw(candidate_kw, temp_db, list_trend_cmt, list_trend_tag):
    temp_db.remove({}) #REMOVE
    
    list_trend = list_trend_cmt + list_trend_tag
    for dict_list_trend in list_trend:
        try:
            if jaro(candidate_kw.lower(),dict_list_trend['_id'].lower())>0.8:
                print(dict_list_trend)
                new_dict = {"kw":candidate_kw,"dates":dict_list_trend['dates']}
                temp_db.insert_one(new_dict)
        except:
            continue
    temp_kw = group_keywords(temp_db)
    return temp_kw
    # for dict_kw in temp_kw:
    #     if dict_kw['_id']==candidate_kw:
    #         return dict_kw

if __name__ == "__main__":
    social_db = get_database()
    list_collection = ['youtube']
    collection_ytb = social_db["youtube"]
    
    # lstcmt = query_channel(social_db,channel_url='hhsb.vn')
    # pprint.pprint(list(lstcmt))
    # group_kw(collection_ytb,keyword='phim')
    # result = search_by_KW(social_db,keyword='vinfast')
    # pprint.pprint(list(result))
    # keyword_tree(collection_ytb,keyword='jav', time_delta=30)
    keyword_report(collection_ytb,'arsenal')
    # pprint.pprint(list(trend_line(social_db))) 
    
    # count_analysis, count_cmt = total_count(social_db,task='facebook')
    # print(count_analysis, count_cmt)
    # kw_url = list_KW_url(social_db)
    # with open('result_kw_url.json', 'w', encoding="utf8") as fp:
    #     json.dump(kw_url, fp, ensure_ascii=False)
    # temp_db = social_db["temp"]
    # list_trend = trend_line(social_db)
    # list_trend_tag = trend_line_tag(social_db)
    # pprint.pprint(list_trend_tag)
    # # vehinh_time = time.time()
    # search_by_KW(social_db, keyword='Potter')
    # final = get_trend_kw(social_db=social_db, candidate_kw='Việt Nam', temp_db=temp_db)
    # print(final)
    # print(time.time()-vehinh_time)
    # new_dict = {'KW':candidate_kw,''}

    
            # print(new_dict)
            # temp_db.insert_one(new_dict)
    # temp_db.insert_one({'kw': 'Tùng Bùi', 'dates': [{'day': 19422.0, 'total': 7}]})
    # temp_db.insert_one({'kw': 'Tùng Bùi', 'dates': [{'day': 19411.0, 'total': 8}]})
    
    
    
    
    # topic_dict = draw_piechart(social_db)
    # # print(topic_dict)
    # # # print("Collection: {} Dict: {}".format(clts,topic_dict))
    # fig1, ax1 = plt.subplots()
    # # print(list([topic_dict[i]['_id'] for i in range(len(topic_dict))]))
    # # print(list([topic_dict[i]['count'] for i in range(len(topic_dict))]))
    # ax1.pie(list([topic_dict[i]['count'] for i in range(len(topic_dict))]), labels=list([topic_dict[i]['_id'] for i in range(len(topic_dict))]), autopct='%1.1f%%',
    #         shadow=True, startangle=90)
    # ax1.axis('equal')
    # # plt.legend()
    # # plt.show()
    # plt.savefig('piechart.png')
    # #Keyword
    # print("Ve hinh time: ",time.time()-vehinh_time)
    # start_time = time.time()
    # list_KW(database=social_db)
    # # # print(dict_kw)
    
    # # print("Establish table: ",time.time()-start_time)
    # # # print(new_dict)
    # with open('result_kw_new.json', 'w', encoding="utf8") as fp:
    #     json.dump(new_dict, fp, ensure_ascii=False)
    