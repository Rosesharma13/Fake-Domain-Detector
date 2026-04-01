import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

from src.features import extract_domain, domain_length, count_digits, entropy
from src.model import get_model

def train_model():
    df = pd.read_csv("data/dataset.csv")

    df['domain'] = df['url'].apply(extract_domain)

    df['length'] = df['domain'].apply(domain_length)
    df['digits'] = df['domain'].apply(count_digits)
    df['entropy'] = df['domain'].apply(entropy)

    vectorizer = CountVectorizer(analyzer='char', ngram_range=(2,3))
    X_ngrams = vectorizer.fit_transform(df['domain'])

    X_numeric = df[['length','digits','entropy']].values
    X = np.hstack([X_numeric, X_ngrams.toarray()])
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = get_model()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))

    return model, vectorizer
