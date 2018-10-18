import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import gh_get_issues as github
from nltk.corpus import stopwords
import re
from nltk.stem import PorterStemmer

nltk.download('stopwords')

def tokenize (text):
	result = []
	for i in range(len(text)):
		for j in range(len(text[i])):
			word_tokenized = word_tokenize(text[i][j])
			result.append(word_tokenized)
	return result

def to_lowercase(text):
	"""Convert all characters to lowercase from list of tokenized words"""
	new_words = []
	final_result = []    
	for i in range(len(text)):
		new_words = []
		for j in range(len(text[i])):
			new_word = text[i][j].lower()
			new_words.append(new_word)
		final_result.append(new_words)
	return final_result

def remove_punctuation(text):
	"""Remove punctuation from list of tokenized words"""
	new_words = []
	final_result = []
	for i in range(len(text)):
		new_words = []
		for j in range(len(text[i])):
			new_word = re.sub(r'[^\w\s]', '', text[i][j])
			if new_word != '':
				new_words.append(new_word)
		final_result.append(new_words)
	return final_result

def remove_stopwords(text):
	"""Remove stop words from list of tokenized words"""
	new_words = []
	final_result = []
	for i in range(len(text)):
		new_words = []
		for j in range(len(text[i])):
			if text[i][j] not in stopwords.words('english'):
				new_words.append(text[i][j])	
		final_result.append(new_words)
	return final_result

def stem_words(text):
	"""Stem words in list of tokenized words"""
	stemmer = PorterStemmer()
	new_words = []
	final_result = []
	for i in range(len(text)):
		new_words = []
		for j in range(len(text[i])):
			stem = stemmer.stem(text[i][j])
			new_words.append(stem)	
		final_result.append(new_words)
	return final_result

def preprocessing (text):
	words_tokenized = tokenize (text)
	words_lower_case = to_lowercase(words_tokenized)
	words_without_punctuation = remove_punctuation(words_lower_case)
	words_without_stopwords = remove_stopwords(words_without_punctuation)
	words_stemmed = stem_words(words_without_stopwords)
	return words_stemmed

if __name__ == '__main__':
	gitissues = github.get_gh_issues()
	#teste = [["Buying! bug1. of", "Buyed? the bug2", "I bug3 bBg3"], ["BUG bug4", "bug5 bug5", "bug6 bug6"]]
	text_pre_processed = preprocessing(gitissues)
	print "TEXT PRE PROCESSED: ", text_pre_processed


