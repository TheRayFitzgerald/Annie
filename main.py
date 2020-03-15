#! usr/bin/python3
import pandas as pd
import nltk
import numpy as np
import re
import data_clean
from nltk.stem import wordnet # to perform lemmitization
from sklearn.feature_extraction.text import CountVectorizer # to perform bow
from sklearn.feature_extraction.text import TfidfVectorizer # to perform tfidf
from nltk import pos_tag # for parts of speech
from nltk import word_tokenize # to create tokens
from nltk.corpus import stopwords # for stop words
import bow
from cosine_similarity import cosine_similarity
import chatbot_gui
pd.options.display.max_rows = 4000
pd.options.display.max_seq_items = 2000


def main():
    df=pd.read_csv('./corpora/conglomerate.csv')
    df['lemmatized_text']=df['context'].apply(data_clean.text_normalization)
    df_bow, cv=bow.context_bow(df)
    chatbot_gui.main()
    message = chatbot_gui.send()
    while question != 'exit':
        question_bow=bow.user_question_bow(QUESTION, cv)
        # create new column for cosine similarity
        df['similarity_bow']=cosine_similarity(df_bow, question_bow)

        # taking similarity value of responses for the reddit context questions
        df_simi = pd.DataFrame(df, columns=['text response','similarity_bow'])
        # sort the values to get answer to *most similar question*
        df_simi_sort = df_simi.sort_values(by='similarity_bow', ascending=False)
        chatbot_gui.recieve(df_simi_sort.iloc[0]['text response'])

if __name__ == '__main__':
    main()