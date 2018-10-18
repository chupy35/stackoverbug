import json
import requests

api_token = ""
api_url_base = 'https://api.github.com/'

projects = ["docker/docker.github.io", "rails/rails", "googleapis/google-api-python-client", "prestodb/presto", "square/okhttp", "netty/netty", "elastic/elasticsearch-hadoop", "elastic/elasticsearch", "spring-projects/spring-boot", "tensorflow/tensorflow", "facebook/react", "angular/angular.js"]
labels = ['priority/P0-catastrophic', 'regression', '"type: bug"', 'bug', 'bug', 'defect', 'bug', '"type: bug"', '"type: bug"', '"type:bug/performance"', '"Type: Bug"', '"type: bug"']

proj_lab = {}
for i in range(len(projects)):
    proj_lab[projects[i]] = labels[i]

#---------------------------------------------------------
# headers = {'Content-Type': 'application/json',
#            'Authorization': 'Bearer {0}'.format(api_token)}
headers = {'Content-Type': 'application/json',
           'Authorization': str(api_token)}
#---------------------------------------------------------
def get_gh_issues(projects):
    
    pissues = []
    issues = []
    
    for p in projects:

        text = 'https://api.github.com/search/issues?q=label:'+proj_lab[p]+'+state:closed+repo:'+p
        print "TEEEEXT: ", text
        #r = requests.get(text, headers)
        r = requests.get(text)
        results = r.text
        data = json.loads(results)

        print "proj_lab[p]: ", proj_lab[p]
        print "p: ", p
        print "DAAAATAAAAA: ", data
        print "\n\n"

        # for x in data['items']:
        #    c = requests.get(x['comments_url'])
        #    com=c.text
        #    comments = json.loads(com)

        #    for y in comments:
        #        commentsa = y['body'] + "\n"
        #    issues.append(str(x['number']) + "\n" + x['title'] + "\n" + x['body'] + "\n" + commentsa)
        # pissues.append(issues)
    return pissues

if __name__ == '__main__':
    result = get_gh_issues(projects)

