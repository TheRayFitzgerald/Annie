import pandas as pd
import nltk
import numpy as np
import re
import data_clean as data
from nltk.stem import wordnet # to perform lemmitization
from sklearn.feature_extraction.text import CountVectorizer # to perform bow
from sklearn.feature_extraction.text import TfidfVectorizer # to perform tfidf
from nltk import pos_tag # for parts of speech
from sklearn.metrics import pairwise_distances # to perfrom cosine similarity
from nltk import word_tokenize # to create tokens
from nltk.corpus import stopwords # for stop words
pd.options.display.max_rows = 4000
pd.options.display.max_seq_items = 2000


def main():

    def process_df(df):
        df= df.loc[df['subreddit'].isin(['Anxiety', 'Depression', 'CasualConversation', 'stress', 'AnxietyDepression'])]
        df_2 = df
        df = pd.merge(df, df_2, left_on='parent_id', right_on='name')
        df= df[['body_x','body_y']]
        df.columns = ['context', 'text response']
        df['lemmatized_text']=df['context'].apply(data.text_normalization)
        return df

    suffix_list = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                suffix_list.append('%s%s%s' % (i, j, k))

    main_df = pd.DataFrame()
    for suffix in suffix_list:
        print(suffix)
        temp_df=pd.read_json('./corpora/all_comments_dir/sub_section%s.json' % suffix, lines=True)
        main_df = pd.concat([main_df, process_df(temp_df)])
    main_df.to_pickle('./pickled_df/main_df.pkl')

if __name__ == '__main__':
    main()