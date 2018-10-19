import json
import requests
import subprocess
import os

username = ["chupy35", "isabellavieira", "Maryam-El"]
api_tokens= []
api_url_base = 'https://api.github.com/'

projects = ["docker/docker.github.io", "rails/rails", "netty/netty",  "elastic/elasticsearch", "spring-projects/spring-boot", "tensorflow/tensorflow", "facebook/react", "angular/angular.js"]

labels = ['priority/P0-catastrophic', 'regression', 'defect', '">bug"', '"type: bug"', '"type:bug/performance"', '"Type: Bug"', '"type: bug"']


# projects = ["docker/docker.github.io"]
# labels = ['priority/P0-catastrophic']


proj_lab = {}
for i in range(len(projects)):
    proj_lab[projects[i]] = labels[i]

# #---------------------------------------------------------
# headers = {'Content-Type': 'application/json',
#             'Authorization': 'Bearer {0}'.format(api_token),
#             "Accept": "application/vnd.github.v3+json"}
# #---------------------------------------------------------

def check_limit_remaining(key):
    term = "X-RateLimit-Remaining:"
    urlimit ='https://api.github.com/users/' + username[key]
    #headers = {'Authorization': 'token 3f54f4dfdab70957c0827bbb1d1d26906e33d770'}
    proc = subprocess.Popen(['curl', '-H', 'Authorization: token'+api_tokens[key], '-i', 'https://api.github.com/users/'+username[key]], stdout=subprocess.PIPE)
    for line in proc.stdout:
        if line[0:22] == term:
            remaining = line[23:27]
   # print out
    return remaining

def get_gh_issues():    
    pissues = []
    issues = []
    flag = 0
    key = 0
    
    for p in projects:
        remaining = check_limit_remaining(key)
        if remaining == 1:
          key = key+1
          if key == 3:
            key = 0

        issues = []
        text = 'https://api.github.com/search/issues?q=label:'+proj_lab[p]+'+state:closed+repo:'+p
        r = requests.get(text, auth=(username[key], api_tokens[key]))
        results = r.text
        data = json.loads(results)

        print "data: ", data

        for x in data['items']:
          commentsa = ""
          c = requests.get(x['comments_url'])
          com = c.text
          comments = json.loads(com)

          for y in comments:
            print "ISSUEEEES: ", y
            commentsa = commentsa + y['body']

          bug_report_content = str(x['number']) + "\n" + x['title'] + "\n" + x['body'] + "\n" + commentsa
          issues.append(bug_report_content)
        pissues.append(issues)
    return pissues

if __name__ == '__main__':
  result = get_gh_issues()
  #check_limit_remaining()


