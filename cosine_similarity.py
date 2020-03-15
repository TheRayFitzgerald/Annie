from sklearn.metrics import pairwise_distances # to perfrom cosine similarity

# get cosine similarity for the user question and stored context questions
def cosine_similarity(df_bow, question_bow):

    cosine_value = 1- pairwise_distances(df_bow, question_bow, metric = 'cosine' )
    return cosine_value