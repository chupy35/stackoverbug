from google.cloud import bigquery
import io
import html2text

"""
How to run:
1) sudo pip install --upgrade google-cloud-bigquery --ignore-installed six
2) Create Google Credentials: create the account key on google cloud: https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries#bigquery_simple_app_query-python
3) export GOOGLE_APPLICATION_CREDENTIALS="<FILE>.json"
"""

# Add the json file with the credentials here
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/isabellavieira/Downloads/My Project-559e49148db1.json"
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/isabellavieira/Downloads/chupytestcom-8a09729c6510.json"

# Explicitly use service account credentials by specifying the private
# key file. All clients in google-cloud-python have this helper.
#clx00-\x7fient = bigquery.Client.from_service_account_json('/home/chupy35/polymtl/dataminning/assigment/test2/stackoverbug/chupytestcom-dfe002fa9cf6.json')

tags = "reactjs"
#, "ruby-on-rails", "netty", "elasticsearch","spring-boot",  "tensorflow", "reactjs", "angularjs"]

client = bigquery.Client()
allResults = []
tmpResult = []

i = 0
tmpResult = []

get_SOPosts = "SELECT p.Id, p.ParentId, p.Title, p.Body, p.CreationDate, p.Tags FROM `sotorrent-org.2018_09_23.Posts` as p  WHERE p.Tags LIKE '<"+ tags +">' AND p.ParentId IS NULL ORDER BY p.Id ASC;"
query_job = client.query(get_SOPosts)
results = query_job.result()

for row in results:

    complete_post = ""
    complete_post = str(row.Id) + "\n" + row.Title.encode("utf-8") + "\n" + row.Body.encode("utf-8")
    i = i + 1
    get_comments = "SELECT p.Id, p.ParentId, p.Title, p.Body, p.Tags FROM `sotorrent-org.2018_09_23.Posts` as p WHERE p.parentId = "+ str(row.Id) +" ORDER BY p.Id ASC;"
    query_job = client.query(get_comments)
    results_comments = query_job.result()

    for comment in results_comments:
        complete_post = complete_post + "\n" + comment.Body.encode("utf-8")

    f = open(tags + "_" + str(row.Id) + '.txt', 'w')
    f.write(complete_post)
    #print "Post id: ", row.Id
    #print "Parent id: ", row.ParentId
    #print "TAGS: ", tag
    #print "Creation Date: ", row.CreationDate
    #print "*******************************************************\n"
	#allResults.append(tmpResult)
#	return sos


#def get_stackoverflow_posts_over_time ():
#	client = bigquery.Client()
#
#	get_SOPostsOverTime = """
#		SELECT ph.*, pht.Type, tv.Title, pbv.Content FROM `sotorrent-org.2018_09_23.PostHistory` as ph, `sotorrent-org.2018_09_23.PostHistoryType` as pht,
#		`sotorrent-org.2018_09_23.TitleVersion` as tv, `sotorrent-org.2018_09_23.PostVersion` as pv,
#		`sotorrent-org.2018_09_23.PostBlockVersion` as pbv, `sotorrent-org.2018_09_23.PostBlockType` as pbt
#		WHERE ph.PostHistoryTypeId = pht.Id and
#		ph.PostId = tv.PostHistoryId and
#		ph.PostId = pv.PostHistoryId and
#		ph.PostId = pbv.PostHistoryId and
#		pbv.PostBlockTypeId = pbt.Id;
#	"""
#
#	query_job = client.query(get_SOPostsOverTime)
#	results = query_job.result()
#
#	return results
#
#if __name__ == '__main__':
#	allResults = get_stackoverflow_posts()
#   	#get_stackoverflow_posts_over_time()
