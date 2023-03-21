from test_api import *
import pandas as pd

chatgpt_score = 0
bert_score = 0
vote_score = 0

df = pd.read_csv("new_data.csv")
for index, row in df[600:605].iterrows():
    # print(row)
    result_gpt = call_api(row['content'])
    print("Text: ",row['content'])
    result_bert = sentiment_bert(row['content'])
    result_vote = process_tweet(row['content'])
    
    print("ChatGPT: ",result_gpt)
    print("Bert: ",result_bert)
    print("Tweet vote: ",result_vote)
    print("Sentiment GT: ",row['label'])
    
    if result_gpt.strip(" ") == row['label']:
        chatgpt_score+=1
    if result_bert.strip(" ") == row['label']:
        bert_score+=1
    if result_vote.strip(" ") == row['label']:
        vote_score+=1

print("Score of ChatGPT: ",chatgpt_score/5)
print("Score of Bert: ",bert_score/5)
print("Score of Vote: ",vote_score/5)