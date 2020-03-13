#! usr/bin/python3
import praw
from praw.models import MoreComments
import pandas as pd
import datetime as dt
#import config
import json

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
top_subreddit = subreddit.top(limit=3)

for submission in top_subreddit:
    print(submission.title)
    submission.comment_sort = 'best'
    # Limit to, at most, 5 top level comments
    submission.comment_limit = 1
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        print("### " + top_level_comment.body)

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)
    print(submission.selftext)

topics_data = pd.DataFrame(topics_dict)
