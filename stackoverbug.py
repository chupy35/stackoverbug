import get_SOposts as stackoverflow
import get_gh_issues as github
import similarity as similarity
import preprocessing as preprocessing

# Get issues from GitHub
#git_issues = github.get_gh_issues()

# Get Stack Overflow posts from BigQuery
#so_posts = stackoverflow.get_stackoverflow_posts()

# Preprocess issues
#preprocessed_git_issues = preprocessing.preprocessing(git_issues)

# Preprocess Stack Overflow posts
#preprocessed_so_posts = preprocessing.preprocessing(so_posts)


teste = [["Buying! bug1. of", "Buyed? the bug2", "I bug3 bBg3"], ["BUG bug4", "bug5 bug5", "bug6 bug6"]]
text = preprocessing.preprocessing(teste)

# Similarity
similarity.tfidf(text)