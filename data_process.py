import pandas as pd
import data_clean as data

pickle_name='top_posts.pkl'
corpus_name='conglomerate.csv'

def main():

    df=pd.read_csv('./corpora/%s' % corpus_name)
    df['lemmatized_text']=df['context'].apply(data.text_normalization)
    df.to_pickle('./pickled_df/%s' % pickle_name)

if __name__ == '__main__':
    main()