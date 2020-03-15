import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords # for stop words
from data_clean import text_normalization
#Return Bag Of Words(BOW) implemtation for Lemmatized Context(lemmatized_text)
def context_bow(df):
    cv = CountVectorizer()
    X = cv.fit_transform(df['lemmatized_text']).toarray()
    features = cv.get_feature_names()
    df_bow = pd.DataFrame(X, columns = features)
    return df_bow, cv

def user_question_bow(user_question, cv):

    stop = stopwords.words('english')

    # checking for stop words

    Q=[]
    a=user_question.split()
    for i in a:
        if i in stop:
            continue
        else:
            Q.append(i)
        b=" ".join(Q)
    # applying the function that we created for text normalizing
    question_lemma = text_normalization(b)
    question_bow = cv.transform([question_lemma]).toarray() # applying bow
    return question_bow