import json
import requests
import os

def get_gh_issues():
    r = requests.get('https://api.github.com/search/issues?q=bug+state:closed+repo:docker/docker.github.io')
    results=r.text
    data = json.loads(results)

   # for x in data['items']:
   #     print(x['created_at'])
   #     print(x['comments_url'])
   #     print(x['title'])
   #     print(x['body'])
    return data

