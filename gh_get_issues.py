import json
import requests
from pprint import pprint
import os
api_token = '6b29e7c228306634d4617dab25ad6788b5adecb0'
api_url_base = 'https://api.github.com/'
projets=['docker/docker.github.io']

#---------------------------------------------------------
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}
#---------------------------------------------------------
def get_gh_issues(projects):
    for p in projects:
        r = requests.get('https://api.github.com/search/issues?q=bug+state:closed+repo:'+p)
        results=r.text
        data = json.loads(results)
        for x in data['items']:
            
           c = requests.get(x['comments_url'])
           com=c.text
           comments = json.loads(com)
        
           print(x['created_at'])
           print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
           print(comments)
           print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
           print(x['title'])
           print(x['body'])
           print(x['id'])
        print('*******************************************************************************************************')

if __name__ == '__main__':
    get_gh_issues(projets)