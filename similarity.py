import os
import unirest
# These code snippets use an open-source library. http://unirest.io/python
for filename in os.listdir('/home/chupy35/polymtl/dataminning/assigment/finalex/springboot/files/parsed/'):
    f = open('/home/chupy35/polymtl/dataminning/assigment/finalex/springboot/files/parsed/' + filename, 'r')
    greaded = f.read().replace('\n', ' ')
    gcsv = filename.split('_')
    gproject = gcsv[0]
    gbugid = gcsv[1].split('.')
    gbugid = gbugid[0]

    for filename in os.listdir('/home/chupy35/polymtl/dataminning/assigment/finalex/springboot/files/comparing/'):
        csv = filename.split('_')
        project = csv[0]
        sbugid = csv[1].split('.')
        sbugid = sbugid[0]
        fy = open('/home/chupy35/polymtl/dataminning/assigment/finalex/springboot/files/comparing/' + filename, 'r')
        readedy = fy.read().replace('\n', ' ')
        response = unirest.post("https://twinword-text-similarity-v1.p.mashape.com/similarity/",
        #response = unirest.post("https://rxnlp-core.p.mashape.com/computeSimilarity",
          headers={
            "X-Mashape-Key": "tHqjP9Ll4amshbsKSmIxyaYOUnRsp1DoHPAjsngXK0YWTGoqCD",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
          },
          params={
            "text1": greaded,
            "text2": readedy
          }
        )
        print gbugid + ';' + sbugid + ';'  +  gproject + ';' + project + ';' + str(response.body['similarity'])
