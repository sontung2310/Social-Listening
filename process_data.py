import pandas as pd

# df = pd.read_csv("Test.csv")
# # print(df[df['n_star']==2])
# df['sentiment'] = [0 for i in range(0,len(df))]
# for index, row in df.iterrows():
#     if (row['n_star'] > 3):
#         df.at[index, 'sentiment'] = 'Positive'
#         # row['sentiment'] = 'Positive'
#     elif (row['n_star'] < 3):
#         df.at[index, 'sentiment'] = 'Negative'
#         # row['sentiment'] = 'Negative'
#     else:
#         df.at[index, 'sentiment'] = 'Neural'
#         # row['sentiment'] = 'Neural'

# print(df.head(30))
# df = df.drop('date_time', axis=1)
# df = df.drop('label', axis=1)
# df.to_csv("processed_data.csv",index=False)

df = pd.read_csv("data.csv")
for index, row in df.iterrows():
    # print(row['label'])
    if (row['label'] == 'POS'):
        df.at[index, 'label'] = 'Positive'
    elif (row['label'] == 'NEG'):
        df.at[index, 'label'] = 'Negative'
    else:
        df.at[index, 'label'] = 'Neural'

df.to_csv("new_data.csv")