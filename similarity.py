def tfidf (text):
	return gensim.models.TfidfModel(text)

# def simmes(corpus, tf_idf, dic)
#     gensim.similarities.Similarity('/usr/workdir/',tf_idf[corpus],
#                                       num_features=len(dic))

def simprint (text, tf_idf):
    query_doc_tf_idf = tf_idf[text]
    return query_doc_tf_idk


# TODO: cosine similarity, jaccard, levenshtein