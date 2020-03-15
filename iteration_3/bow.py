from sklearn.feature_extraction.text import CountVectorizer

def bow(df):
    cv = CountVectorizer()
    X = cv.fit_transform(df['lemmatized_text']).toarray()
    features = cv.get_feature_names()
    df_bow = pd.DataFrame(X, columns = features)
    return df_bow