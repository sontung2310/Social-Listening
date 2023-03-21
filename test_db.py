from pymongo import MongoClient
import pymongo
import urllib
from dateutil import parser
from datetime import datetime
import pandas as pd
import time
import json
now = datetime.now()
current_time = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
print("Current Time =", current_time)
current_time = parser.parse(current_time)
# expiry_date = '2021-07-13T00:00:00.000Z'
print(current_time)

def to_datetime(text_time: str):
    
    dt_time = datetime.strptime(text_time, '%H:%M %d/%m/%Y')
    return dt_time

def get_database():
    username = urllib.parse.quote_plus('sontung2310')
    password = urllib.parse.quote_plus("Vmagcut99!")
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb+srv://{}:{}@cluster0.gyiy6tr.mongodb.net/?retryWrites=true&w=majority".format(username, password)
    CONNECTION_STRING = "mongodb://127.0.0.1:27017/"
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    
    # db = client['social_listening_storage']
    
    # for db in client.list_databases():
    #     print(db)
    # Create the database for our example (we will use the same database throughout the tutorial
    # return client['user_shopping_list']
    return client['social_listening_storage']

def insert_db(collection, data):
    #Input: data: array
    #Collection:  
    # collection_news = dbname["news_data"]
    # collection_fb = dbname["facebook"]
    # collection_forum = dbname["forum"]
    # collection_ytb = dbname["youtube"]
    # if len(total_data)==100:
    #     print("Save data:")
    try:
        collection.find()
        collection.insert_many(data,ordered=False)
        # collection_name.update_one()
    except pymongo.errors.BulkWriteError as e:
        dict_error = e.details['writeErrors']
        # print(dict_error)
        for i in range(0,len(dict_error)):
            print(dict_error[i]['keyValue']['_id'])
            # Get duplicated ID
            duplicated_id = dict_error[i]['keyValue']['_id']
            # Filter
            filter = {'_id': duplicated_id}
            index = dict_error[i]['index']
            # Get current data in array
            current_data = data[index]
            # Get comment of current data
            current_array_cmt = current_data['comments_infor']
            # For cmt in cmts, if cmt_time > crawl_time: update comment
            # print("Comment time: ", current_cmt['Time'])
            #Get comment which already had saved in database
            # saved_comment_array : [{'Text': '', 'Sentiment': '', 'Time': '', 'check_flag': False},{'Text': '', 'Sentiment': '', 'Time': '', 'check_flag': False}]
            saved_comment_array = collection.find({"_id": duplicated_id})[0]['comments_infor']
            # Get saved_comment
            saved_comment = [(cmts['author'],cmts['comment']) for cmts in saved_comment_array]
            # Voi tung cmt trong array_cmt
            # current_array_cmt : [{'Text': '', 'Sentiment': '', 'Time': '', 'check_flag': False},{'Text': '', 'Sentiment': '', 'Time': '', 'check_flag': False}]
            for current_cmt in current_array_cmt:
                # Neu cmt co Time -> so sanh time cua cmt voi time crawl -> time cmt > time crawl: push cmt moi vao
                if current_cmt['time_comment'] != "":
                    current_cmt_time = to_datetime(current_cmt['time_comment'])
                    last_crawl_time = to_datetime(current_data['time_crawl'])
                    if current_cmt_time > last_crawl_time:
                        newcomment = {"$push": {'comments_infor': current_cmt}}
                        collection.update_one(filter, newcomment)
                    # else:
                    #     print("Khong co gi de update")
                # Neu cmt khong co Time -> check xem cmt da co trong database chua -> chua -> push cmt moi vao
                else:
                    if (current_cmt['author'],current_cmt['comment']) not in saved_comment:
                        newcomment = {"$push": {'comments_infor': current_cmt}}
                        collection.update_one(filter, newcomment)
            # Set flag of article to False
            update_database(filter, collection, False, 'check_flag')
            #Update time crawl
            update_database(filter, collection, datetime.now().strftime('%H:%M %d/%m/%Y'), 'time_crawl')
    print("Done save data")

def load_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as r:
        data = r.readlines()
        data = [json.loads(x.strip('\n')) for x in data]

    return data
def update_database(filter,collection, update_var, update_position):
    #Update update_var in update position
    newvalue = { "$set": { update_position: update_var } }
    collection.update_one(filter, newvalue)
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
    # Get the database
    dbname = get_database()
    # collection_fb = dbname["facebook_data"]
    # collection_news = dbname["news_data"]
    collection_ytb = dbname["youtube"]
    # item_details = collection_ytb.find({"check_flag":True})
    collection_ytb.remove({"check_flag":True})
    # data_arr = load_file("/mnt/data/tungbs/Crawl_data/test_case.json")
    # print(data_arr)
    # collection_ytb.insert_many(data_arr)
    # insert_db(collection_ytb,data_arr)
    # item_details = collection_news.find()
    # item_details = collection_news.find({"_id":"https://genk.vn/chatgpt-phan-hoi-ra-sao-khi-bi-ceo-bkav-nguyen-tu-quang-noi-hoc-lom-20230216160625765.chn"})
    # for i,item in enumerate(item_details):
    #     filter = {'_id': item['_id'] }
    # #     # print(item['Content'][''])
        
    #     for j,comment in enumerate(item['Comment']):
    #         print(j,comment)
    #         update_database(filter, "Anh Quảng nói gì cũng tuyệt", 'Comment.'+str(j)+'.Text')
    #         update_database(filter, "11:42 21/2/2023", 'Comment.'+str(j)+'.Time')
            # item['Content']['Sentiment'] = { "$set": { 'Content.Sentiment': "Neural" } }
            # collection_news.update_one(filter, item['Content']['Sentiment'])
            # update_database(filter, False, 'Comment.'+str(j)'.check_flag')
        # print(item['Comment'][i]['Text'])
        # filter = {'_id': item['_id'] }
        # newvalues = { "$set": {"check_process":False}}
        # collection_news.update_one(filter,newvalues)
    #     for i,comment in enumerate(item['Comment']):
    #         print(i,comment)
    #         print(comment['Sentiment'])
            # newvalues = { "$set": { 'Comment.'+str(i)+'.Sentiment': 'Positive' } }
            # collection_news.update_one(filter, newvalues)
        # newvalues = { "$set": { 'Comment.0.Sentiment': 'Negative' } }
        # newvalues = { "$set": { 'Comment': [{'Text':"Anh Quảng hay quá trời",'Sentiment':'Positive','Time':'15/02/2023T10:13:02'}] } }
        # # newvalues = { "$push": { 'Comment': {'Text':"resigned, distressed, midst of chaos in the world",'Sentiment':'Negative','Time':'15/02/2023T10:13:02'} } }
        # # collection_name.update_one({'_id':item['_id']},
        # #                            {'$set':{'tag':["Football","Movie","Entertainment"]}})
        
        
    # collection_ytb.remove({}) #REMOVE
    # 
    # collection_fb.insert_many([item_1,item_2])
    # process_index = collection_news.create_index("check_process")
    
    # item_details = collection_name.find()
    
    
    # for item in item_details:
    #     print("id: ",item['_id'])
    #     filter = {'_id': item['_id'] }
    #     newvalues = { "$set": { 'Comment': [{'Text':"I suppose that, I imagine that, apparently",'Sentiment':'Positive','Time':'15/02/2023T10:13:02'}] } }
    #     # newvalues = { "$push": { 'Comment': {'Text':"resigned, distressed, midst of chaos in the world",'Sentiment':'Negative','Time':'15/02/2023T10:13:02'} } }
    #     # collection_name.update_one({'_id':item['_id']},
    #     #                            {'$set':{'tag':["Football","Movie","Entertainment"]}})
    #     collection_name.update_one(filter, newvalues)
        # print(item["Comment"])
        
        
    # item_df = pd.DataFrame(item_details)
    # print(item_df)
    # for item in item_details:
    #     # This does not give a very readable output
    #     print("result",item['expiry_date'], item['category'])