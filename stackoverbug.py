import get_SOposts as stackoverflow
import simi as similarity
import gh_get_issues as github

gitissues = github.get_gh_issues()
soPosts = stackoverflow.get_stackoverflow_posts()

# def traverse(o, tree_types=(list, tuple)):
#     if isinstance(o, tree_types):
#         for value in o:
#             for subvalue in traverse(value, tree_types):
#                 yield subvalue
#     else:
#         yield o

# For processing text
def processText(text):
    for value in traverse(text):
        #readed = similarity.read_file(text)
        tokenized = similarity.tokenize(readed)
        return tokenized



for i in soPosts:
    for j in soPosts:
        print i



# tokBugs = processText(gitissues)
# for value in traverse(tokBugs):
#     stemdicted = similarity.stemdicreat(tokBugs)
#     corpused = similarity.map_word_to_id(stemdicted)
#     tfidfed = similarity.tfidf(corpused)
#     simed = similarity.simmes(corpused, tfidfed, stemdicted)

# processSo = processText(soPosts)
# for value in traverse(processSo):
#     query_doc_bow = similarity.stemdicreat(processSo)
#     query_doc_tf_idf = tfidfed[query_doc_bow]

# print(simed[query_doc_tf_idf])


# ###Process stackoverlow posts
# #for value in traverse(soPosts):
# #    sreaded = similarity.read_file(soPosts)
# #    stokenized = similarity.tokenize(sreaded)
# #    sstemdicted = similarity.stemdicreat(stokenized)
# #    scorpused = similarity.map_word_to_id(sstemdicted)
# #    stfidfed = similarity.tfidf(scorpused)

# ##Comparing
# for value in traverse(gitissues):
#     ssimed = similarity.simmes(corpused, tfidfed, stemdicted)


# # For each stack overflow post, we compare to all bug reports and to the similarity
# #for post in soPosts:
# #	for bug in gitissues['items']:
# #            print(bug['created_at'])
# #            print(bug['comments_url'])
# #            print(bug['title'])
# #            print(bug['body'])
# #
