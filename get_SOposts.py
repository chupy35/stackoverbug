from google.cloud import bigquery
import os

"""
How to run:
1) sudo pip install --upgrade google-cloud-bigquery --ignore-installed six
2) Create Google Credentials: create the account key on google cloud: https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries#bigquery_simple_app_query-python
3) export GOOGLE_APPLICATION_CREDENTIALS="<FILE>.json"
"""

# Add the json file with the credentials here
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/isabellavieira/Downloads/bigquery-b745e90937c4.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/isabellavieira/Downloads/chupytestcom-45254619180f.json"

tags = ["docker", "angularjs", "reactjs", "tensorflow", "spring-boot", "elasticsearch", "elasticsearch-hadoop", "netty", "okhttp", "presto", "google-api-python-client", "ruby-on-rails"] 

def get_stackoverflow_posts ():
	print ">>>> GETTING STACKOVERBUG"

	client = bigquery.Client()
	allResults = []

	# get_SOPosts = """
	# SELECT p.*, pt.Type, c.Text FROM `sotorrent-org.2018_09_23.Posts` as p, 
	# `sotorrent-org.2018_09_23.PostType` as pt, `sotorrent-org.2018_09_23.Comments` as c 
	# WHERE p.PostTypeId = pt.Id and p.Id = c.PostId limit 10;
	# """

	# Query specific to Docker Project
	# get_SOPosts = """
	# SELECT DISTINCT p.*, pt.Type, c.Text, prgh.RepoName FROM `sotorrent-org.2018_09_23.Posts` as p, 
	# `sotorrent-org.2018_09_23.PostType` as pt, `sotorrent-org.2018_09_23.Comments` as c,
	# `sotorrent-org.2018_09_23.PostReferenceGH` as prgh
	# WHERE p.PostTypeId = pt.Id and p.Id = c.PostId and prgh.RepoName LIKE 'docker/docker.github.io';
	# """
	
	for tag in tags: 
		get_SOPosts = """
			SELECT p.ParentId, p.Id, p.Title, p.Body, p.Tags, p.CreationDate FROM `sotorrent-org.2018_09_23.Posts` as p 
			WHERE p.Tags LIKE '%s'
			GROUP BY 1, 2, 3, 4, 5, 6
			ORDER BY 1 desc
			LIMIT 10;
		"""

		query_job = client.query(get_SOPosts % (tag))
		results = query_job.result()

		print ">>>> DID QUERY"
		for row in results:
			allResults.append(row)
			print "ENTROU NO FOR"
			print ">>> ID: ", row.Id
			print ">>> Parent ID: ", row.ParentId
			print ">>> Title: ", row.Title.encode("utf-8")
			print ">>> Body: ", row.Body.encode("utf-8")
			print ">>> Tags: ", row.Tags.encode("utf-8")
			print ">>> Creation Date: ", row.CreationDate
			print "**********************************************************"
			print "\n\n"

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

	# for row in results:
	# 	print ">>> ID: ", row.Id
	# 	print ">>> Comment: ", row.Comment
	# 	print "\n\n"

	return results

if __name__ == '__main__':
    get_stackoverflow_posts()
   	#get_stackoverflow_posts_over_time()