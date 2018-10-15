import get_SOposts as stackoverflow
import simi as similarity
import get_GHissues as github
# TODO: Import retrieve bug reports from GitHub
github.get_gh_issues()

soPosts = stackoverflow.get_stackoverflow_posts()
# TODO: get bug reports


# For each stack overflow post, we compare to all bug reports and to the similarity
for post in soPosts:
	for bug in bugReports:
		# TODO: call the similarity function
