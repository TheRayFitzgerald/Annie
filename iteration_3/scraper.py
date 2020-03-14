#! usr/bin/python3
import praw
from praw.models import MoreComments
import pandas as pd
import datetime as dt
#import config
import json
import csv

corpus = dict()

with open('config.json') as json_data_file:
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

subreddit = reddit.subreddit('anxiety')
top_subreddit = subreddit.top(limit=1000)

with open('corpus.csv', mode='w') as csv_file:
    fieldnames=['context', 'text response']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for submission in top_subreddit:
        submission.comment_sort = 'best'
        submission.comment_limit = 1
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
            writer.writerow({'context': submission.title, 'text response': top_level_comment.body})


