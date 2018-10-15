import json

#curl 'https://api.github.com/search/issues?q=bug+language:javascript+state:closed&sort=created&order=asc' > tmp.txt

with open("java.txt") as f:
	data = json.load(f)

dictionary = {}
for x in data["items"]:
	if x["repository_url"] in dictionary:
		dictionary[x["repository_url"]] += 1
	else:
		dictionary[x["repository_url"]] = 1

for key, value in dictionary.items():
	print key," ", value
