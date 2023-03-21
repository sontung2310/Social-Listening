from underthesea import sentiment
from underthesea import classify
from underthesea import ner
import openai
import json
import pandas as pd
openai.api_key = "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"
def call_api(input_string):
    with open('prompt_classify.txt', 'r') as file:
        prompt_mn = file.read().rstrip()
# prompt = (f"Act as you are text classify model. Hãy phân loại nội dung sau vào một trong 8 loại: Thể thao, Giải trí, Công nghệ, Khác, Xã hội, Kinh doanh, Thời tiết, Chiến tranh. Text: '''Nhan sắc nóng bỏng của 'tiểu tam' bị ghét phim Đừng làm mẹ cáu '''")
    prompt = "Act as you are text classify model. Hãy phân loại nội dung sau vào một trong 8 loại: Thể thao, Giải trí, Công nghệ, Khác, Xã hội, Kinh doanh, Thời tiết, Chiến tranh. Text: '''{}'''".format(input_string)
    # prompt = "Act as you are text classify model. Hãy phân loại nội dung sau vào một trong 8 loại: Thể thao, Giải trí, Công nghệ, Khác, Xã hội, Kinh doanh, Thời tiết, Chiến tranh.\n"+ prompt_mn + "\nText:'''{}'''\nClassify:".format(input_string)
    print("_________________________________________________")
    print("Complete prompt: ",prompt)
    print("_________________________________________________")
    # print(prompt)
    completions = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions["choices"][0]["text"]
    return message
# full_text = ["Tập này đáng yêu quá đội thua có 200k mà đi đâu cũng nhớ đến 4ng còn lại mua quà cho còn ước nguyện giùm. Xúc động nhất là khúc ước nguyện Chúc ctr 2N1Đ luôn được mn yêu quý luôn có nhiều sức khoẻ ra thêm nhiều tập nhiều mùa sau",
#              "Xem tập 20 ở trên trang youtube và Vieon", "Mình thích xem YouTube Trường Giang mà thấy thằng dương bảo lâm là không muốn xem, ngồi mà cái mỏ và đứng lên quậy vô duyên tắt luôn không coi",
#              "KMT thấy rất lười nhát, tránh né việc nặng, giả tạo, 1 khi đụng chạm tới lợi ích là k nể mặt ai, suốt chương trình chỉ biết cười như điên dại, đàn ông mà hay làm nét ngây thơ,  nhõng nhẽo, thật sự coi khó chịu cực kỳ",
#              "Coi mà cười muốn bệnh luôn á trời😂😂 ông nào ông đó nhây chúa luôn", "Chương trình này xem ngày càng nhạt","Nhìn Cris vừa thương vừa tội mà vừa mắc cừi ổng",
#              "Trại huấn luyện mùa đông #2Ngay1Dem tại Sơn La sẽ là một hành trình đầy 'gian nan' cho các thành viên. Biệt đội #2N1Đ sẽ phải vượt qua những thử thách nào của chương trình? Chờ xem nhé!",
#              "Riết rồi tuần nào mình cũng cười như điên", "Sản phẩm hơi nhỏ so với tưởng tượng nhưng chất lượng tốt, đóng gói cẩn thận.",
#              "hàng kém chất lg,chăn đắp lên dính lông lá khắp người. thất vọng"]

# # for text in full_text:
# #     print("Text: ",text)
# #     print("Sentiment",sentiment(text))
# #     print("_____________________________________________________")

# sentiment('Sản phẩm hơi nhỏ so với tưởng tượng nhưng chất lượng tốt, đóng gói cẩn thận.')
# classify_text = ['HLV đầu tiên ở Premier League bị sa thải sau 4 vòng đấu','Lý do Ukraine giữ đến cùng pháo đài Bakhmut trước vòng vây hỏa lực Nga','Giao tranh suốt ngày đêm, Nga mất 100 quân trong trận chiến giành Bakhmut','Mẹ đơn thân thu nhập 9 con số: Con trẻ không bao giờ là vật cản!',
#                  'Nga tuyên bố đánh chìm tàu quân sự, hạ 8 nhóm biệt kích Ukraine','ChatToday: Gửi tiết kiệm ngân hàng sao cho đúng, có nên ham lãi suất cao?','Cơ hội nào cho U20 Việt Nam khi rơi vào bảng đấu khó tại giải châu Á?',
#                  'Lady Gaga vào vai Harley Quinn trong Joker 2: Chờ đợi gã hề tái xuất','Nhan sắc đời thường ngọt ngào của Á hậu Việt có biệt danh "thần tiên tỷ tỷ"']
# for i in classify_text:
#     print("Text: ",i)
#     message = call_api(i)
#     print("Type: ",message)  

text = "Lady Gaga vào vai Harley Quinn trong Joker 2: Chờ đợi gã hề tái xuất"
lst_result = ner(text, deep=True)
for result in lst_result:
    print("Word, Entity: ",result['word'],result['entity'])
