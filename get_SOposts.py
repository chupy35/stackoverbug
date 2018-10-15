from google.cloud import bigquery
import os


# sudo pip install --upgrade google-cloud-bigquery --ignore-installed six
# Create Google Credentials: create the account key on google cloud: https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries#bigquery_simple_app_query-python
# export GOOGLE_APPLICATION_CREDENTIALS="<FILE>.json"

# Add the json file with the credentials here
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""

def get_stackoverflow_posts ():
	client = bigquery.Client()

	# get_SOPosts = """
	# SELECT p.*, pt.Type, c.Text FROM `sotorrent-org.2018_09_23.Posts` as p, 
	# `sotorrent-org.2018_09_23.PostType` as pt, `sotorrent-org.2018_09_23.Comments` as c 
	# WHERE p.PostTypeId = pt.Id and p.Id = c.PostId limit 10;
	# """

	get_SOPosts = """
	SELECT DISTINCT p.*, pt.Type, c.Text, prgh.RepoName FROM `sotorrent-org.2018_09_23.Posts` as p, 
	`sotorrent-org.2018_09_23.PostType` as pt, `sotorrent-org.2018_09_23.Comments` as c,
	`sotorrent-org.2018_09_23.PostReferenceGH` as prgh
	WHERE p.PostTypeId = pt.Id and p.Id = c.PostId and prgh.RepoName LIKE 'docker/docker.github.io';
	"""

	query_job = client.query(get_SOPosts)
	results = query_job.result()

	for row in results:
		print ">>> ID: ", row.Id
		print ">>> Title: ", row.Title.encode("utf-8")
		print ">>> Body: ", row.Body.encode("utf-8")
		print ">>> Comments: ", row.Text.encode("utf-8"):
		print ">>> RepoName: ", row.RepoName
		print "\n\n"
	
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

	for row in results:
		print ">>> ID: ", row.Id
		print ">>> Comment: ", row.Comment
		print "\n\n"


if __name__ == '__main__':
    get_stackoverflow_posts()
   #get_stackoverflow_posts_over_time()