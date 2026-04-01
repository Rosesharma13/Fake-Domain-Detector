import numpy as np
from src.features import extract_domain, domain_length, count_digits, entropy

def predict(domain_input, model, vectorizer):
    d = extract_domain(domain_input)

    features = [
        domain_length(d),
        count_digits(d),
        entropy(d)
    ]

    ngram_features = vectorizer.transform([d]).toarray()
    final_features = np.hstack([features, ngram_features[0]])

    prediction = model.predict([final_features])[0]

    return "FAKE 🚨" if prediction == 1 else "LEGIT ✅"
