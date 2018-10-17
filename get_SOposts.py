from google.cloud import bigquery
import os

"""
How to run:
1) sudo pip install --upgrade google-cloud-bigquery --ignore-installed six
2) Create Google Credentials: create the account key on google cloud: https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries#bigquery_simple_app_query-python
3) export GOOGLE_APPLICATION_CREDENTIALS="<FILE>.json"
"""

# Add the json file with the credentials here
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/isabellavieira/Downloads/My Project-559e49148db1.json"

tags = ["angularjs", "reactjs", "tensorflow", "spring-boot", "elasticsearch", "elasticsearch-hadoop", "netty", "okhttp", "presto", "google-api-python-client", "ruby-on-rails"] 

def get_stackoverflow_posts ():
	client = bigquery.Client()
	allResults = []
	
	for tag in tags: 
		get_SOPosts = "SELECT p.Id, p.ParentId, p.Title, p.Body, p.Tags FROM `sotorrent-org.2018_09_23.Posts` as p  WHERE p.Tags LIKE '<"+ tag +">' AND p.ParentId IS NULL ORDER BY p.Id ASC;"
		query_job = client.query(get_SOPosts)
		results = query_job.result()

		for row in results:
			complete_post = ""
			complete_post = str(row.Id) + "\n" + str(row.Title.encode("utf-8")) + "\n" + str(row.Body.encode("utf-8"))

			get_comments = "SELECT p.Id, p.ParentId, p.Title, p.Body, p.Tags FROM `sotorrent-org.2018_09_23.Posts` as p WHERE p.parentId = "+ str(row.Id) +" ORDER BY p.Id ASC;"
			query_job = client.query(get_comments)
			results_comments = query_job.result()

			for comment in results_comments:
				complete_post = complete_post + "\n" + str(comment.Body.encode("utf-8"))
			
			# print ">>> Complete post: ", complete_post
			# print "**********************************************************"
			# print "\n\n"

			allResults.append(complete_post)
	return allResults

	
def get_stackoverflow_posts_over_time ():
	client = bigquery.Client()

	get_SOPostsOverTime = """
		SELECT ph.*, pht.Type, tv.Title, pbv.Content FROM `sotorrent-org.2018_09_23.PostHistory` as ph, `sotorrent-org.2018_09_23.PostHistoryType` as pht, 
		`sotorrent-org.2018_09_23.TitleVersion` as tv, `sotorrent-org.2018_09_23.PostVersion` as pv, 
		`sotorrent-org.2018_09_23.PostBlockVersion` as pbv, `sotorrent-org.2018_09_23.PostBlockType` as pbt
		WHERE ph.PostHistoryTypeId = pht.Id and 
		ph.PostId = tv.PostHistoryId and
		ph.PostId = pv.PostHistoryId and
		ph.PostId = pbv.PostHistoryId and
		pbv.PostBlockTypeId = pbt.Id;
	"""

	query_job = client.query(get_SOPostsOverTime)
	results = query_job.result()

	return results

if __name__ == '__main__':
    get_stackoverflow_posts()
   	#get_stackoverflow_posts_over_time()