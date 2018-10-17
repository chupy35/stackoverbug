#import get_SOposts as stackoverflow
import simi as similarity
import gh_get_issues as github
#soPosts = stackoverflow.get_stackoverflow_posts()

gitissues=github.get_gh_issues()
readed = similarity.read_file(gitissues)
tokenized = similarity.tokenize(readed)
stemdicted = similarity.stemdicreat(tokenized)
corpused = similarity.map_word_to_id(stemdicted)
tfidfed = similarity.tfidf(corpused)
simed = similarity.simmes(corpused, tfidfed, stemdicted)
# For each stack overflow post, we compare to all bug reports and to the similarity
#for post in soPosts:
#	for bug in gitissues['items']:
#            print(bug['created_at'])
#            print(bug['comments_url'])
#            print(bug['title'])
#            print(bug['body'])
#
