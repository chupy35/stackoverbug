import json
import requests
import subprocess
import os

username = ["chupy35", "isabellavieira", "Maryam-El"]
api_tokens= ["1e3e1158bc1a6530cf25f6125218d5cf28570fb7", "522441e225bd6e9eaef6bdcd59e3bfd87d561b69", "fe4ec3c573ab49409d11d055028af34f97e8b23d"]
#username = ["mpcrocha", "solencio123", "arkhoninfaustus"]
#api_tokens= ["b117803b4fea20b21f33108b9f3f163b45e61ddc", "57f2916b3a193302f2e9e60c30262527041e0068", "0c6cc4799d1a1817fa337cff7897d9abbd030626"]
api_url_base = 'https://api.github.com/'

projects = ["square/okhttp"]
#projects = ["docker/docker.github.io", "rails/rails", "netty/netty",  "elastic/elasticsearch", "spring-projects/spring-boot", "tensorflow/tensorflow", "facebook/react", "angular/angular.js"]

# labels = ['priority/P0-catastrophic', 'regression', 'defect', '">bug"', '"type: bug"', '"type:bug/performance"', '"Type: Bug"', '"type: bug"']
labels = ['bug']

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
    proc = subprocess.Popen(['curl', '-H', 'Authorization: token '+ api_tokens[key], '-i', 'https://api.github.com/users/'+username[key]], stdout=subprocess.PIPE)
    for line in proc.stdout:
        print line
        if line[0:22] == term:
            remaining = line[23:27]
    print "REMAINING: \n", remaining
    return remaining

def get_gh_issues():
    pissues = []
    issues = []
    flag = 0
    key = 0

    for p in projects:
        remaining = check_limit_remaining(key)
        print "Remaining: ", remaining
        if remaining == 1:
          key = key+1
          if key == 3:
            key = 0

        issues = []
        text = 'https://api.github.com/search/issues?q=label:'+proj_lab[p]+'+state:closed+repo:'+p
        r = requests.get(text, auth=(username[key], api_tokens[key]))
        results = r.text
        data = json.loads(results)

        # print "*******************************************************\n"
        # print "GITHUB ISSUE: ", data
        # print "*******************************************************\n"

        for x in data['items']:
          commentsa = ""
          c = requests.get(x['comments_url'], auth=(username[key], api_tokens[key]))
          com = c.text
          comments = json.loads(com)

          for y in comments:
            #print "ISSUEEEES: ", y
            commentsa = commentsa + y['body'].encode('utf-8')

          brnum = x['number']
          print "State: ", x["state"]
          print "Created date: ", x["created_at"]
          print "Closed date: ", x["closed_at"]
          print "*******************************************************\n"

          bug_report_content = str(x['number']) + "\n" + x['title'].encode('utf-8') + "\n" + x['body'].encode('utf-8') + "\n" + commentsa
          f = open(projects + "_" + brnum + '.txt', 'w')
          f.write(bug_report_content)

          #issues.append(bug_report_content)
        #pissues.append(issues)
    return bug_report_content

if __name__ == '__main__':
  result = get_gh_issues()
  #check_limit_remaining()


