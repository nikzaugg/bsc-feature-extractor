import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

dir_path = os.path.dirname(os.path.realpath(__file__))

def generate():
    inputData = dir_path+'/data/dataset.csv'
    df = pd.read_csv(inputData,
                     encoding="ISO-8859-1")

    col = ['changeId', 'commitMessage']
    df = df[col]
    df = df[pd.notnull(df['commitMessage'])]
    df['category_id'] = df['changeId'].factorize()[0]
    df = df[['changeId', 'commitMessage']].drop_duplicates()

    keys = df.index.values
    values = df['changeId']
    index_to_changeid = dict(zip(keys, values))

    tfidf = TfidfVectorizer(sublinear_tf=True, min_df=1, norm='l2',
                            encoding='latin-1', ngram_range=(1, 2), stop_words='english')
    features = tfidf.fit_transform(df.changeId).toarray()
    print(features.shape)
    doc = pd.DataFrame(data=features, index=index_to_changeid.values())
    
    return doc


def extract(data, row):
    data_row = data.loc[[row[4]]]
    data_row = data_row.values.tolist()
    return data_row