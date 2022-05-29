import pandas as pd
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from collections import Counter

def predict(inputList):
    MBTI = pd.read_csv('input/MBTI 500.csv')
    input = ""

    for i in inputList:
        input += i

    X = MBTI['posts'] # features
    Y = MBTI['type']  # labels
    vectorizer = TfidfVectorizer()
    # Training the vectorizer:
    X_train_tfidf = vectorizer.fit_transform(X)

    # Training the classifier:
    clf = LinearSVC()
    clf.fit(X_train_tfidf, Y)

    # Pipelining the vectorizer and the classifier
    text_clf = Pipeline([('tfidf', TfidfVectorizer()), ('clf', LinearSVC())])
    text_clf.fit(X, Y)
    return text_clf.predict([input])