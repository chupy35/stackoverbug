import get_SOposts as stackoverflow
import get_gh_issues as github
import similarity as similarity
import preprocessing as preprocessing

#Get issues from GitHub
git_issues = github.get_gh_issues()

#Get Stack Overflow posts from BigQuery
so_posts = stackoverflow.get_stackoverflow_posts()

#Preprocess issues
preprocessed_git_issues = preprocessing.preprocessing(git_issues)

#Preprocess Stack Overflow posts
preprocessed_so_posts = preprocessing.preprocessing(so_posts)

#Similarity
tfidf_posts = similarity.tfidf(preprocessed_so_posts)
tfidf_issues = similarity.tfidf(preprocessed_git_issues)

for post in tfidf_posts:
    for issue in tfidf_issues:
        cosine_result = similarity.cosine_similarity(post, issue)
        print ">>> Cosine: ", cosine_result



# TO TEST
# teste1 = [["Buying! fdsfsfsd. of", "Buyed? the bug2", "I bug3 bBg3"], ["BUG bug4", "abs bug5", "bug6 bug6"]]
# teste2 = [["Buying! fdsfsfsd. of", "Buyed? the bug2", "I bug3 bBg3"], ["BUG bug4", "abs bug5", "bug6 bug6"]]
# text1 = preprocessing.preprocessing(teste1)
# text2 = preprocessing.preprocessing(teste2)
# print "preproceesded 1: ", text1
# print "preproceesded 2: ", text2

# # Similarity
# result1 = similarity.tfidf(text1)
# result2 = similarity.tfidf(text2)

# for post in result1:
#     for issue in result2:
#         cosine_result = similarity.cosine_similarity(post, issue)
#         print ">>> Cosine: ", cosine_result



