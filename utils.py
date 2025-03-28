# ----------- utils.py -----------
def flatten_keywords(keywords_list):
    tokens = set()
    for phrase in keywords_list:
        for word in phrase.lower().split():
            tokens.add(word.strip())
    return list(tokens)

def combine_keywords(tfidf, ner, bert):
    return list(set(tfidf) | set(ner) | set(bert))

def build_search_query(tfidf, ner, bert):
    all_keywords = combine_keywords(tfidf, ner, bert)
    query_parts = [f'"{kw}"' for kw in all_keywords]
    return " OR ".join(query_parts)
