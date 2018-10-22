for each filename in . do
	cat filename ; x=$(cat filename)
	for each filename in comparing do
		cat filename ; y=$(cat filename)
		curl -X POST --include 'https://twinword-text-similarity-v1.p.mashape.com/similarity/' \
		  -H 'X-Mashape-Key: tHqjP9Ll4amshbsKSmIxyaYOUnRsp1DoHPAjsngXK0YWTGoqCD' \
		  -H 'Content-Type: application/x-www-form-urlencoded' \
		  -H 'Accept: application/json' \
		  -d 'text1=$x' \
		  -d 'text2=$y
  end if
end for
'
