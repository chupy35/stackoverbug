for filename in *.txt; do
	html2text $filename > "parsed/$filename"
done
