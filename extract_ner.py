# ----------- extract_ner.py -----------
import spacy
nlp_ner = spacy.load("en_core_web_sm")

def extract_ner_keywords(text, top_n=5):
    doc = nlp_ner(text)
    keywords = [ent.text.lower() for ent in doc.ents if ent.label_ in ["ORG", "PRODUCT", "GPE", "PERSON"]]
    return keywords[:top_n]