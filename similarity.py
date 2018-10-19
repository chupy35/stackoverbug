from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics import jaccard_similarity_score
from scipy import spatial

def tfidf (text):
	vectorizer = TfidfVectorizer(tokenizer=None, min_df=1)
	tfidf = TfidfVectorizer(tokenizer=lambda i:i, lowercase=False)
	result_train = tfidf.fit_transform(text)
	final = result_train.toarray()
	return final


def cosine_similarity (array1, array2):
	return 1 - spatial.distance.cosine(array1, array2)

# def jaccard_similarity (array1, array2):
# 	return jaccard_similarity_score (array1, array2)


