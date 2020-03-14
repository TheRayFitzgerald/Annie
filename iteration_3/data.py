#! usr/bin/python3

import pandas as pd

df=pd.read_csv('corpus.csv')
df.head

def text_normalization(text):
    text=str(text).lower()
    spl_char_text=re.sub(r'[^ a-z]'), '', text)
    tokens=nltk.word_tokenize(spl_char_text)
    lema=wordnet.WordNetLemmatizer()
    tags_list=pos_tag(tokens, tagset=None)
    lema_words=[]
    for token,pos_token in tags_list:
        if pos_token.startswith('V'):
            pos_val='v'
        elif pos_token_starswith('J'):
            pos_val='a'
        elif pos_token_starswith('R'):
            pos_val='r'
        else:
            pos_val='n'
        lema_token=lema.lemmatize(token, pos_val)
        lema_words.append(lema_token)

    return " ".join(lema_words)
