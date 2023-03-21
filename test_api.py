
import openai
import json
import pandas as pd
openai.api_key = "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"
import py_vncorenlp
import torch
from transformers import RobertaForSequenceClassification, AutoTokenizer
from vsa import *
import time
# openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>
# with open ("sentiment_data.jsonl", 'r', encoding='utf-8') as f:
#     prompt = [json.loads(line) for line in f.readlines()]
#     # prompt = f.readlines()
# print(prompt)

# csv_prompt = pd.DataFrame(prompt)
# csv_prompt = csv_prompt.to_json()
# prompt = (f"Act as you are text sentiment classify model. Hãy phân loại nội dung sau vào một trong 3 loại: Positive, Negative, Neural. Text: '''KMT thấy rất lười nhát, tránh né việc nặng, giả tạo, 1 khi đụng chạm tới lợi ích là k nể mặt ai, suốt chương trình chỉ biết cười như điên dại, đàn ông mà hay làm nét ngây thơ,  nhõng nhẽo, thật sự coi khó chịu cực kỳ''' ")
# for pmt in prompt:
#     print(pmt["prompt"])
rdrsegmenter = py_vncorenlp.VnCoreNLP(annotators=["wseg"], save_dir='./')

def call_api(input_string):
    with open('prompt_script.txt', 'r') as file:
        prompt_mn = file.read().rstrip()
    prompt = prompt_mn + "\nTweet: '{}'\nSentiment: ".format(input_string)
    print("_________________________________________________")
    print("Complete prompt: ",prompt)
    print("_________________________________________________")
    # print(prompt)
    completions = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt,
        max_tokens=10,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions["choices"][0]["text"]
    return message
def sentiment_bert(input_string):
    model = RobertaForSequenceClassification.from_pretrained("wonrax/phobert-base-vietnamese-sentiment")

    tokenizer = AutoTokenizer.from_pretrained("wonrax/phobert-base-vietnamese-sentiment", use_fast=True)
    output = rdrsegmenter.word_segment(input_string)
    # print(" ".join(output))
    # Just like PhoBERT: INPUT TEXT MUST BE ALREADY WORD-SEGMENTED!
    sentence = "".join(output) 
    # print(sentence)
    input_ids = torch.tensor([tokenizer.encode(sentence)])
    class_data = ['Negative','Positive','Neural']
    with torch.no_grad():
        out = model(input_ids)
        # print(out.logits.softmax(dim=1).tolist())
        index = torch.argmax(out.logits.softmax(dim=1)).item()
        
    return class_data[index]

if __name__ == "__main__":
    # message = call_api("Crawl data của Facebook khó điên")
    input_string = "Khuy Áo may ẩu, chỉ dư rất nhiều!"
    for i in range(0,5):
        start_time = time.time()
        message = sentiment_bert(input_string)
        print("Time: ",time.time()-start_time)
        print(message)
    # another_message = process_tweet(input_string)
    # print(another_message)
    print(message)
    # text = "Ông Nguyễn Khắc Chúc  đang làm việc tại Đại học Quốc gia Hà Nội. Bà Lan, vợ ông Chúc, cũng làm việc tại đây."
    
    
    