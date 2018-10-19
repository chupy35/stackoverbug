import json
import requests
import subprocess
import os

username = "chupy35"
api_token = "3f54f4dfdab70957c0827bbb1d1d26906e33d770"
api_url_base = 'https://api.github.com/'

projects = ["docker/docker.github.io", "rails/rails", "googleapis/google-api-python-client", "prestodb/presto", "square/okhttp", "netty/netty", "elastic/elasticsearch-hadoop", "elastic/elasticsearch", "spring-projects/spring-boot", "tensorflow/tensorflow", "facebook/react", "angular/angular.js"]
labels = ['priority/P0-catastrophic', 'regression', '"type: bug"', 'bug', 'bug', 'defect', 'bug', '">bug"', '"type: bug"', '"type:bug/performance"', '"Type: Bug"', '"type: bug"']

proj_lab = {}
for i in range(len(projects)):
    proj_lab[projects[i]] = labels[i]

##---------------------------------------------------------
#headers = {'Content-Type': 'application/json',
#            'Authorization': 'Bearer {0}'.format(api_token),
#            "Accept": "application/vnd.github.v3+json"}
##---------------------------------------------------------

def check_limit_remaining ():
    urlimit ='https://api.github.com/users/chupy35'
    #headers = {'Authorization': 'token 3f54f4dfdab70957c0827bbb1d1d26906e33d770'}
    proc = subprocess.Popen(['curl', '-H', 'Authorization: token 3f54f4dfdab70957c0827bbb1d1d26906e33d770', '-i', 'https://api.github.com/users/chupy35'], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    print out

#    result = subprocess.check_output('curl -H "Authorization: token 3f54f4dfdab70957c0827bbb1d1d26906e33d770" -i https://api.github.com/users/chupy35', shell=True)
   # result = result.split("\n")
   # return result[7].split(":")[1]

def get_gh_issues(projects):
    pissues = []
    issues = []

    for p in projects:
        text = 'https://api.github.com/search/issues?q=label:'+proj_lab[p]+'+state:closed+repo:'+p
        r = requests.get(text, auth=(username, api_token))
        results = r.text
        data = json.loads(results)

        for x in data['items']:
          commentsa = ""
          c = requests.get(x['comments_url'])
          com = c.text
          comments = json.loads(com)

          for y in comments:
            commentsa = commentsa + y['body']

          bug_report_content = str(x['number']) + "\n" + x['title'] + "\n" + x['body'] + "\n" + commentsa
          issues.append(bug_report_content)
        pissues.append(issues)
    return pissues

if __name__ == '__main__':
  #result = get_gh_issues(projects)
  check_limit_remaining()


