#! usr/bin/python3
import pandas as pd
import nltk
import numpy as np
import re
import data_clean
import tkinter
from tkinter import *
from nltk.stem import wordnet # to perform lemmitization
from sklearn.feature_extraction.text import CountVectorizer # to perform bow
from sklearn.feature_extraction.text import TfidfVectorizer # to perform tfidf
from nltk import pos_tag # for parts of speech
from nltk import word_tokenize # to create tokens
from nltk.corpus import stopwords # for stop words
import bow
from cosine_similarity import cosine_similarity


pickle_name='top_posts.pkl'



def main():
    print('reading pickle')
    df = pd.read_pickle('./pickled_df/%s' % pickle_name)
    print('read pickle')
    print('getting df_bow')
    df_bow, cv=bow.context_bow(df)
    print('done df_bow\nWaiting on a question')

    ######
    def send():
        msg = EntryBox.get("1.0",'end-1c').strip()
        EntryBox.delete("0.0",END)

        if msg != '':
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "You: " + msg + '\n\n')
            ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
            print('doing question bow')
            question_bow=bow.user_question_bow(msg, cv)
            print('done question bow')
            # create new column for cosine similarity
            print('doing cosine')
            df['similarity_bow']=cosine_similarity(df_bow, question_bow)
            print('done cosine')

            # taking similarity value of responses for the reddit context questions
            print('doing df simi')
            df_simi = pd.DataFrame(df, columns=['context', 'text response','similarity_bow'])
            print('done df simi')

            # sort the values to get answer to *most similar question*
            print('doing df simi_sort')
            df_simi_sort = df_simi.sort_values(by='similarity_bow', ascending=False)
            print('done df simi_sort')
            print('doing text response')
            res = df_simi_sort.iloc[0]['text response']
            print('done text response')
            print(df_simi_sort.iloc[0]['context'])
            ChatLog.insert(END, "Annie: " + res + '\n\n')

            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)


    base = Tk()
    base.title("Annie, the Anxiety Bot.")
    base.geometry("400x500")
    base.resizable(width=FALSE, height=FALSE)

    #Create Chat window
    ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)


    #Bind scrollbar to Chat window
    scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
    ChatLog['yscrollcommand'] = scrollbar.set

    #Create the box to enter message
    EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
    EntryBox.bind("<Return>", send)

    #Create Button to send message
    SendButton = Button(base, bg='red', font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                        bd=0, fg='black', command= send )


    #Place all components on the screen
    scrollbar.place(x=376,y=6, height=386)
    ChatLog.place(x=6,y=6, height=386, width=370)
    EntryBox.place(x=128, y=401, height=90, width=265)
    SendButton.place(x=6, y=401, height=90)
    ChatLog.insert(END, "Annie: Welcome. My name is Annie, the Anxiety Bot. Just say whatever comes to mind." + '\n\n')

    ChatLog.config(state=DISABLED)
    base.mainloop()
    #####

    message = chatbot.send()
    while question != 'exit':
        question_bow=bow.user_question_bow(QUESTION, cv)
        # create new column for cosine similarity
        df['similarity_bow']=cosine_similarity(df_bow, question_bow)

        # taking similarity value of responses for the reddit context questions
        df_simi = pd.DataFrame(df, columns=['text response','similarity_bow'])
        # sort the values to get answer to *most similar question*
        df_simi_sort = df_simi.sort_values(by='similarity_bow', ascending=False)
        chatbot.recieve(df_simi_sort.iloc[0]['text response'])

if __name__ == '__main__':
    main()

