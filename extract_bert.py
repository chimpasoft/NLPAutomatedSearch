# ----------- extract_bert.py -----------
import spacy
nlp_bert = spacy.load("en_core_web_sm")

def extract_bert_keywords(text, top_n=5):
    doc = nlp_bert(text.lower())
    noun_chunks = [chunk.text.lower() for chunk in doc.noun_chunks]
    return noun_chunks[:top_n]