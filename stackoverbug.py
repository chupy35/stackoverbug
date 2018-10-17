#import get_SOposts as stackoverflow
#import simi as similarity
import get_GHissues as github

gitissues=github.get_gh_issues()


soPosts = stackoverflow.get_stackoverflow_posts()


# For each stack overflow post, we compare to all bug reports and to the similarity
for post in soPosts:
	for bug in gitissues['items']:
            print(bug['created_at'])
            print(bug['comments_url'])
            print(bug['title'])
            print(bug['body'])

