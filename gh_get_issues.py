import json
import requests
api_token = '6b29e7c228306634d4617dab25ad6788b5adecb0'
api_url_base = 'https://api.github.com/'
projects = ["docker/docker.github.io", "rails/rails", "googleapis/google-api-python-client", "prestodb/presto", "square/okhttp", "netty/netty", "elastic/elasticsearch-hadoop", "elastic/elasticsearch", "spring-projects/spring-boot", "tensorflow/tensorflow", "facebook/react", "angular/angular.js"]
labels = ['priority/P0-catastrophic', 'regression', '"type: bug"', 'bug', 'bug', 'defect', 'bug', '"type: bug"', '"type: bug"', 'type:bug/performance', '"Type: Bug"', '"type: bug"']

proj_lab = {}
for i in range(len(projects)):
    proj_lab[projects[i]] = labels[i]

#---------------------------------------------------------
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}
#---------------------------------------------------------
def get_gh_issues(projects):
    pissues = []
    issues = []
    for p in projects:
        r = requests.get('https://api.github.com/search/issues?q=label:'+proj_lab[p]+'bug+state:closed+repo:'+p)
        results=r.text
        data = json.loads(results)
        for x in data['items']:

           c = requests.get(x['comments_url'])
           com=c.text
           comments = json.loads(com)

           for y in comments:
               commentsa = y['body'] + "\n"
        issues[x] = x['number'] + "\n" + x['title'] + "\n" + x['body'] + "\n" + commentsa
    pissues[p] = issues
    return pissues

#           print("CREATED IN ---->   ", x['created_at'])
#           print("CLOSED IN ---->   ", x['closed_at'])
#           print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
#           for y in comments:
#               print(y['body'])
#               print('\n')
#           print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
#           print(x['title'])
#           print(x['body'])
#           print("THE ID is   ----->   ", x['number'])
#           print('*******************************************************************************************************')

if __name__ == '__main__':
    get_gh_issues(projects)
