from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def tfidf (text):
	vectorizer = TfidfVectorizer(tokenizer=None, min_df=1)
	# for i in range(len(text)):
	# 	for j in range(len(text[i])):
	# 		X = vectorizer.fit_transform(text[i][j])
	# 		idf = vectorizer.idf_
	# 		print "result: ", dict(zip(vectorizer.get_feature_names(), idf))
	tfidf = TfidfVectorizer(tokenizer=lambda i:i, lowercase=False)
	result_train = tfidf.fit_transform(text)
	print(vectorizer.get_feature_names())
	print "\n\n\n>>>>>>>>>>>>>>>>>>>>resultado_train:\n\n ", result_train



# train_data = [["the","sun","is","bright"],["blue","is","the","sky"]]









# TODO: cosine similarity, jaccard, levenshtein


