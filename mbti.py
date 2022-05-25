import pandas as pd
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

MBTI = pd.read_csv('input/MBTI 500.csv')

X = MBTI['posts'] # features
y = MBTI['type']  # labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
# Training the vectorizer:
X_train_tfidf = vectorizer.fit_transform(X_train)

# Training the classifier:
clf = LinearSVC()
clf.fit(X_train_tfidf, y_train)

# Pipelining the vectorizer and the classifier
text_clf = Pipeline([('tfidf', TfidfVectorizer()), ('clf', LinearSVC())])
text_clf.fit(X_train, y_train)

predictions = text_clf.predict(X_test)

print(text_clf.predict(["I need to do an algorithm too. I hate algorithms. I just need to solve a few with the easy ones, hahaha. Oh yeah?? Wow... huh... ah haha ​​there's no director... why do you suddenly come to bed at this hour? I'll wash up. My dog ​​slept deeply while washing his hair, and then he came to dry his hair and left."]))
print(classification_report(y_test, predictions))
print(f"Overall accuracy of the model: {round(metrics.accuracy_score(y_test, predictions),2)}")

