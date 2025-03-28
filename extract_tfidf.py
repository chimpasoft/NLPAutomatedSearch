# ----------- extract_tfidf.py -----------
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_tfidf_keywords(text, top_n=5):
    vectorizer = TfidfVectorizer(max_features=top_n)
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    return [word.lower() for word in feature_names]