#! usr/bin/python3
import praw
from praw.models import MoreComments
import pandas as pd
import datetime as dt
#import config
import json

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

subreddit = reddit.subreddit('anxiety')
top_subreddit = subreddit.top(limit=1500)

for submission in top_subreddit:
    #print(submission.title)
    corpus[submission.title]=''
    submission.comment_sort = 'best'
    # Limit to, at most, 5 top level comments
    submission.comment_limit = 1
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        corpus[submission.title]=top_level_comment.body
        #print("### " + top_level_comment.body)

with open('corpus.txt', 'w') as outfile:
    json.dump(corpus, outfile)

