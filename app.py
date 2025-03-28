# ----------- app.py -----------
import streamlit as st
from preprocess import preprocess_text
from extract_tfidf import extract_tfidf_keywords
from extract_ner import extract_ner_keywords
from extract_bert import extract_bert_keywords
from utils import combine_keywords, build_search_query

st.set_page_config(page_title="Keyword Extraction App", layout="centered")
st.title("🔍 Automated Keyword Extractor for Job Descriptions")

job_description = st.text_area("Paste a Job Description:", height=300)

if st.button("Extract Keywords"):
    if job_description:
        st.subheader("1️⃣ Preprocessing")
        processed = preprocess_text(job_description)
        st.code(processed, language="text")

        st.subheader("2️⃣ Keyword Extraction")
        tfidf = extract_tfidf_keywords(processed)
        ner = extract_ner_keywords(job_description)
        bert = extract_bert_keywords(job_description)

        st.write("**TF-IDF Keywords:**", tfidf)
        st.write("**NER Keywords:**", ner)
        st.write("**BERT Keywords:**", bert)

        st.subheader("3️⃣ Combined Boolean Search Query")
        query = build_search_query(tfidf, ner, bert)
        st.code(query, language="text")
    else:
        st.warning("Please enter a job description to continue.")