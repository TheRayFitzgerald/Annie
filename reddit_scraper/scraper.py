#! usr/bin/python3
import praw
from praw.models import MoreComments
import pandas as pd
import datetime as dt
#import config
import json
import csv

corpus = dict()

with open('../config/config.json') as json_data_file:
    data = json.load(json_data_file)['details']

reddit = praw.Reddit(client_id=data['client_id'], \
                     client_secret=data['client_secret'], \
                     user_agent=data['user_agent'], \
                     username=data['username'], \
                     password=data['password'])

topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], \
                "comms_num": [], \
                "created": [], \
                "body":[]}

data_dict = { "context":[], \
                "text response":[]}

subreddit_list = [reddit.subreddit('depression'), reddit.subreddit('anxiety'), reddit.subreddit('stress'), reddit.subreddit('CasualConversation'), reddit.subreddit('AnxietyDepression')]
top_subreddit_list=[]
for i in subreddit_list:
    top_subreddit_list.append(i.top(limit=1000))

with open('../corpora/conglomerate.csv', mode='w') as csv_file:
    fieldnames=['context', 'text response']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for top_subreddit in top_subreddit_list:
        for submission in top_subreddit:
            submission.comment_sort = 'best'
            submission.comment_limit = 1
            for top_level_comment in submission.comments:
                if isinstance(top_level_comment, MoreComments):
                    continue
                writer.writerow({'context': submission.title, 'text response': top_level_comment.body})


