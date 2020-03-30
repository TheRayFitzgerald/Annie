import pandas as pd
import nltk
import numpy as np
import re
import data_clean
import string
import json
from nltk.stem import wordnet # to perform lemmitization
from sklearn.feature_extraction.text import CountVectorizer # to perform bow
from sklearn.feature_extraction.text import TfidfVectorizer # to perform tfidf
from nltk import pos_tag # for parts of speech
from sklearn.metrics import pairwise_distances # to perfrom cosine similarity
from nltk import word_tokenize # to create tokens
from nltk.corpus import stopwords # for stop words

suffix_list = []
for i in list(string.ascii_lowercase):
    for t in list(string.ascii_lowercase):
        suffix_list.append('%s%s' % (i, t))
"""
for suffix in suffix_list:
    with open('./corpora/all_reddit_comments_dir/sub_section%s.json' % suffix) as data_file:
        data = json.load(data_file)

    for comment in data:
        if not (comment['subreddit'].isin(['Anxiety', 'Depression', 'CasualConversation']))
"""
for suffix in suffix_list:
    print(suffix)
    df_temp = pd.read_json('./corpora/all_reddit_comments_dir/sub_section%s.json' % suffix, lines=True)
    df_temp= df_temp.loc[df_temp['subreddit'].isin(['Anxiety', 'Depression', 'CasualConversation'])]

    with open('./corpora/all_reddit_comments_dir_cleaned/sub_section%s.json' % suffix, 'w') as cleaned_json_file:
        json.dump(df_temp.to_json(), cleaned_json_file)