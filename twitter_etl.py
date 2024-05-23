import pandas as pd
import json
from datetime import datetime
import s3fs
import csv

tweet_list = []
with open('tweets.csv', encoding="utf8", mode='r') as file:
    csvFile = csv.reader(file)
    next(csvFile)  # Skip the first line (header)

    for lines in csvFile:
        refined_tweet = {"author": lines[0],
                         "content": lines[1],
                         "country": lines[2],
                         "date_time": lines[3],
                         "id": lines[4],
                         "language": lines[5],
                         "number_of_likes": lines[8],
                         "number_of_shares": lines[9],
                         }
        tweet_list.append(refined_tweet)

df = pd.DataFrame(tweet_list)
df.to_csv('tweets_refined.csv', index=False)
