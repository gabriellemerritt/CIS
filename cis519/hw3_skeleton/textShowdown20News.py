import numpy as np
from sklearn.metrics import accuracy_score, roc_curve, auc
from sklearn.cross_validation import train_test_split
from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.metrics.pairwise import cosine_similarity

if __name__ == "__main__":
    twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
    count_vect = CountVectorizer(stop_words='english', lowercase=True)
    X_train_counts = count_vect.fit_transform(twenty_train.data)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

    clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
    docs_new = ['God is love', 'OpenGL on the GPU is fast']
    X_new_counts = count_vect.transform(docs_new)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)
    predicted = clf.predict(X_new_tfidf)
    print predicted
