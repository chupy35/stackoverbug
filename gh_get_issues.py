import json
import requests
import subprocess
import os

username = "isabellavieira"
api_token = ""
api_url_base = 'https://api.github.com/'

# projects = ["docker/docker.github.io", "rails/rails", "googleapis/google-api-python-client", "prestodb/presto", "square/okhttp", "netty/netty", "elastic/elasticsearch-hadoop", "elastic/elasticsearch", "spring-projects/spring-boot", "tensorflow/tensorflow", "facebook/react", "angular/angular.js"]
# labels = ['priority/P0-catastrophic', 'regression', '"type: bug"', 'bug', 'bug', 'defect', 'bug', '">bug"', '"type: bug"', '"type:bug/performance"', '"Type: Bug"', '"type: bug"']


projects = ["docker/docker.github.io"]
labels = ['priority/P0-catastrophic']


proj_lab = {}
for i in range(len(projects)):
    proj_lab[projects[i]] = labels[i]

#---------------------------------------------------------
headers = {'Content-Type': 'application/json',
            'Authorization': 'Bearer {0}'.format(api_token),
            "Accept": "application/vnd.github.v3+json"}
#---------------------------------------------------------

def check_limit_remaining ():
  result = subprocess.check_output("curl -i https://api.github.com/users/isabellavieira?acess_token="+api_token, shell=True)
  result = result.split("\n")
  return result[7].split(":")[1]

def get_gh_issues():    
    pissues = []
    issues = []
    
    for p in projects:
        issues = []
        text = 'https://api.github.com/search/issues?q=label:'+proj_lab[p]+'+state:closed+repo:'+p
        r = requests.get(text, auth=(username, api_token))
        results = r.text
        data = json.loads(results)

        for x in data['items']:
          commentsa = ""
          c = requests.get(x['comments_url'])
          com = c.text
          comments = json.loads(com)

          if comments["documentation_url"]:
            print "Limit exceeded"
            pass
          else:
            for y in comments:
              print "ISSUEEEES: ", y
              commentsa = commentsa + y['body']

          bug_report_content = str(x['number']) + "\n" + x['title'] + "\n" + x['body'] + "\n" + commentsa
          issues.append(bug_report_content)
        pissues.append(issues)
    return pissues

if __name__ == '__main__':
  #result = get_gh_issuelis(projects)
  check_limit_remaining()


