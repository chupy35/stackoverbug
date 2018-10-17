import gensim from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import re
from nltk.stem import PorterStemmer

##For cleaning html tags##
#def cleanhtml(raw_html):
#  cleanr = re.compile('<.*?>')
#  cleantext = re.sub(cleanr, '', raw_html)
#  return cleantext

##HTML CLEANED VERSION##
#so1_text = cleanhtml(open('stackoverflowpostg.txt').read().decode('utf-8'))
#so2_text = cleanhtml(open('stackoverflowpostf.txt').read().decode('utf-8'))

#we open files with correct encoding
# so1_text = open('stackoverflowpostg.txt').read().decode('utf-8')
# so2_text = open('stackoverflowpostf.txt').read().decode('utf-8')

# raw_documents = [so1_text, so2_text]

# print("Number of documents:",len(raw_documents))


# #we tokenize the documents
# gen_docs = [[w.lower() for w in word_tokenize(text)]
#             for text in raw_documents]
# print(gen_docs)


#we create de dictionary
# dictionary = gensim.corpora.Dictionary(gen_docs)
# print("Number of words in dictionary:",len(dictionary))
# for i in range(len(dictionary)):
#     print(i, dictionary[i])

#we make the corpus (word repetition)
# corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
# print(corpus)

#we generate tf_idf model
# tf_idf = gensim.models.TfidfModel(corpus)
# print(tf_idf)
# s = 0
# for i in corpus:
#     s += len(i)
# print(s)

# similarity measure object in tf-idf space.
# sims = gensim.similarities.Similarity('/home/chupy35/polymtl/dataminning/assigment',tf_idf[corpus],
#                                       num_features=len(dictionary))
# print(sims)
# print(type(sims))


# bugreport_file = open('oraclebugreport.txt', 'r')
# bugreport_txt = bugreport_file.read().decode('utf-8')

# query_doc = [w.lower() for w in word_tokenize(bugreport_txt)]
# print(query_doc)

# query_doc_bow = dictionary.doc2bow(query_doc)
# print(query_doc_bow)

# query_doc_tf_idf = tf_idf[query_doc_bow]
# print(query_doc_tf_idf)
# print("\n \n \n \n \n \n \n similarity: \n \n")
# print(sims[query_doc_tf_idf])

def read_file(input_text):
	return input_text.read().decode('utf-8')

def tokenize (text):
	return [w.lower() for w in word_tokenize(text)]

#Dictionary Creation and stemming
def stemdicreat (text):
    dictionary = gensim.corpora.Dictionary(text)
    for i in range(len(dictionary)):
        dictionary[i]=PorterStemmer().stem(dictionary[i])
    return dictionary

def map_word_to_id (text):
	return dictionary.doc2bow(text)

def preprocessing (input_file):
	print "preprocessing"
	file = read_file(input_file)
	print file
	#fileTokenized = tokenize (file)
	#fileMapped = map_word_to_id(fileTokenized)
	#return fileMapped

def tfidf (text):
	tf_idf = gensim.models.TfidfModel(text)
    return gensim.similarities.Similarity('/usr/workdir/',tf_idf[corpus],
                                      num_features=len(dictionary))

def simprint (text, tf_idf):
    query_doc_tf_idf = tf_idf[text]
    return query_doc_tf_idk

# remove punctuation and special characters
def rempunct (text):
    return cleanString = re.sub('\W+ ',' ', text )

# TODO: stemmingi
def stemmingi (text):
    for i in range(len(text)):
        return PorterStemmer().stem(text)
     # TODO: cosine similarity, jaccard, levenshtein

if __name__ == '__main__':
:q
:q
:q
	bugreport_file = open('input_files/oraclebugreport.txt', 'r')

	preProcessedText = preprocessing(bugreport_file)
	#tfidf = tfidf (preProcessedText)
